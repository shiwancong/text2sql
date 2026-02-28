#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
简化版本地 RAG 系统

无需 Docker，使用 Python 原生库实现：
- sentence-transformers: 文本嵌入
- faiss-cpu: 向量检索
- 本地 JSON 存储
"""

import os
import sys
import json
import asyncio
import argparse
from pathlib import Path
from typing import Any, Optional, List, Dict
import hashlib

import mcp.types as types
from mcp.server import Server, NotificationOptions
from mcp.server.models import InitializationOptions
import mcp.server.stdio

from pydantic import BaseModel

# ============================================================================
# 配置
# ============================================================================
class Config(BaseModel):
    """本地 RAG 配置"""
    knowledge_dir: str = ""
    embedding_model: str = "sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2"
    chunk_size: int = 500
    chunk_overlap: int = 50

def load_config() -> Config:
    """加载配置"""
    knowledge_dir = Path(__file__).parent.parent / "ragflow" / "knowledge"
    return Config(
        knowledge_dir=str(knowledge_dir),
        embedding_model=os.getenv("RAG_EMBEDDING_MODEL", "sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2"),
        chunk_size=int(os.getenv("RAG_CHUNK_SIZE", "500")),
        chunk_overlap=int(os.getenv("RAG_CHUNK_OVERLAP", "50"))
    )

# ============================================================================
# 简化版 RAG 引擎
# ============================================================================
try:
    from sentence_transformers import SentenceTransformer
    import faiss
    import numpy as np
    SENTENCE_TRANSFORMERS_AVAILABLE = True
except ImportError:
    SENTENCE_TRANSFORMERS_AVAILABLE = False

class SimpleRAGEngine:
    """简化版 RAG 引擎"""

    def __init__(self, config: Config):
        self.config = config
        self.model = None
        self.indexes = {}
        self.documents = {}
        self.knowledge_dir = Path(config.knowledge_dir)

        if SENTENCE_TRANSFORMERS_AVAILABLE:
            print(f"Loading embedding model: {config.embedding_model}")
            try:
                self.model = SentenceTransformer(config.embedding_model)
                print("Embedding model loaded successfully")
            except Exception as e:
                print(f"Failed to load model: {e}")
                self.model = None
        else:
            print("Warning: sentence-transformers not installed. RAG search will use keyword matching.")

    def _load_documents(self) -> Dict[str, List[Dict]]:
        """加载知识库文档"""
        docs = {
            'ddl': [],
            'description': [],
            'examples': []
        }

        # 加载 DDL 知识库
        ddl_dir = self.knowledge_dir / "ddl"
        if ddl_dir.exists():
            for json_file in ddl_dir.glob("*.json"):
                try:
                    with open(json_file, encoding='utf-8') as f:
                        data = json.load(f)
                        if isinstance(data, dict):
                            # tables.json
                            for table_name, table_data in data.items():
                                docs['ddl'].append({
                                    'id': f"ddl_{table_name}",
                                    'content': json.dumps(table_data, ensure_ascii=False),
                                    'metadata': {
                                        'type': 'ddl',
                                        'table': table_name,
                                        'source': json_file.name
                                    }
                                })
                        elif isinstance(data, list):
                            # relationships.json
                            docs['ddl'].append({
                                'id': f"ddl_relationships",
                                'content': json.dumps(data, ensure_ascii=False),
                                'metadata': {'type': 'relationships', 'source': json_file.name}
                            })
                except Exception as e:
                    print(f"Error loading {json_file}: {e}")

        # 加载描述知识库
        desc_dir = self.knowledge_dir / "descriptions"
        if desc_dir.exists():
            for md_file in desc_dir.glob("*.md"):
                try:
                    with open(md_file, encoding='utf-8') as f:
                        content = f.read()
                        docs['description'].append({
                            'id': f"desc_{md_file.stem}",
                            'content': content,
                            'metadata': {'type': 'description', 'source': md_file.name}
                        })
                except Exception as e:
                    print(f"Error loading {md_file}: {e}")

        # 加载示例知识库
        ex_dir = self.knowledge_dir / "examples"
        if ex_dir.exists():
            for md_file in ex_dir.glob("*.md"):
                try:
                    with open(md_file, encoding='utf-8') as f:
                        content = f.read()
                        docs['examples'].append({
                            'id': f"ex_{md_file.stem}",
                            'content': content,
                            'metadata': {'type': 'example', 'source': md_file.name}
                        })
                except Exception as e:
                    print(f"Error loading {md_file}: {e}")

        return docs

    def _chunk_text(self, text: str, chunk_size: int = 500, overlap: int = 50) -> List[str]:
        """将文本分块"""
        chunks = []
        start = 0
        while start < len(text):
            end = start + chunk_size
            chunk = text[start:end]
            if chunk:
                chunks.append(chunk)
            start = end - overlap
        return chunks

    def _build_index(self, documents: List[Dict]):
        """构建向量索引"""
        if not self.model:
            return None

        texts = [doc['content'] for doc in documents]
        if not texts:
            return None

        try:
            embeddings = self.model.encode(texts, show_progress_bar=False)
            dimension = embeddings.shape[1]
            index = faiss.IndexFlatL2(dimension)
            index.add(embeddings.astype('float32'))
            return index
        except Exception as e:
            print(f"Error building index: {e}")
            return None

    def initialize(self):
        """初始化 RAG 引擎"""
        print("Loading documents...")
        all_docs = self._load_documents()

        for category, docs in all_docs.items():
            if docs:
                self.documents[category] = docs
                if self.model:
                    self.indexes[category] = self._build_index(docs)

        print(f"Loaded {sum(len(d) for d in self.documents.values())} documents")

    def _keyword_search(self, query: str, documents: List[Dict], top_k: int = 5) -> List[Dict]:
        """关键词搜索（回退方案）"""
        query_lower = query.lower()
        scored_docs = []

        for doc in documents:
            content = doc['content'].lower()
            # 简单的关键词匹配计分
            score = 0
            for word in query_lower.split():
                if word in content:
                    score += content.count(word)

            if score > 0:
                scored_docs.append({**doc, 'score': score})

        scored_docs.sort(key=lambda x: x['score'], reverse=True)
        return scored_docs[:top_k]

    def search(self, query: str, category: str = 'all', top_k: int = 5) -> List[Dict]:
        """搜索相关文档"""
        results = []

        categories_to_search = []
        if category == 'all':
            categories_to_search = list(self.documents.keys())
        else:
            mapping = {
                'ddl': 'ddl',
                'description': 'description',
                'examples': 'examples'
            }
            categories_to_search = [mapping.get(category, category)]

        for cat in categories_to_search:
            if cat not in self.documents:
                continue

            docs = self.documents[cat]

            if self.model and cat in self.indexes and self.indexes[cat]:
                try:
                    query_embedding = self.model.encode([query], show_progress_bar=False)
                    distances, indices = self.indexes[cat].search(query_embedding.astype('float32'), top_k)

                    for i, (dist, idx) in enumerate(zip(distances[0], indices[0])):
                        if idx < len(docs) and idx >= 0:
                            results.append({
                                **docs[idx],
                                'score': float(1 / (1 + dist))  # 转换为相似度分数
                            })
                except Exception as e:
                    print(f"Vector search error: {e}, falling back to keyword search")
                    results.extend(self._keyword_search(query, docs, top_k))
            else:
                results.extend(self._keyword_search(query, docs, top_k))

        # 排序并去重
        seen_ids = set()
        unique_results = []
        for r in sorted(results, key=lambda x: x.get('score', 0), reverse=True):
            if r['id'] not in seen_ids:
                seen_ids.add(r['id'])
                unique_results.append(r)

        return unique_results[:top_k]

    def get_schema(self, table_name: str) -> Optional[Dict]:
        """获取表结构"""
        for doc in self.documents.get('ddl', []):
            if table_name.lower() in doc['id'].lower():
                try:
                    data = json.loads(doc['content'])
                    if isinstance(data, dict) and table_name in data:
                        return data[table_name]
                except:
                    pass
        return None

    def health_check(self) -> bool:
        """健康检查"""
        return bool(self.documents)

# ============================================================================
# 全局 RAG 引擎
# ============================================================================
rag_engine: Optional[SimpleRAGEngine] = None
config: Optional[Config] = None

# ============================================================================
# MCP 服务器
# ============================================================================
server = Server("local-rag-mcp-server")

@server.list_resources()
async def handle_list_resources() -> list[types.Resource]:
    """列出可用资源"""
    return [
        types.Resource(
            uri="rag:/datasets",
            name="本地知识库",
            description="本地 RAG 知识库",
            mimeType="application/json",
        )
    ]

@server.read_resource()
async def handle_read_resource(uri: str) -> str:
    """读取资源"""
    if uri == "rag:/datasets":
        summary = {}
        for cat, docs in rag_engine.documents.items():
            summary[cat] = len(docs)
        return json.dumps(summary, ensure_ascii=False, indent=2)
    raise ValueError(f"未知资源 URI: {uri}")

@server.list_tools()
async def handle_list_tools() -> list[types.Tool]:
    """列出可用工具"""
    return [
        types.Tool(
            name="ragflow_search",
            description="在本地知识库中搜索相关表和字段。根据自然语言查询，检索相关的数据库表、字段和业务描述。",
            inputSchema={
                "type": "object",
                "properties": {
                    "query": {
                        "type": "string",
                        "description": "搜索查询，例如：'学生表'、'课程信息'、'教师相关字段'"
                    },
                    "dataset": {
                        "type": "string",
                        "enum": ["all", "ddl", "description", "examples"],
                        "default": "all",
                        "description": "要搜索的知识库类型"
                    },
                    "top_k": {
                        "type": "integer",
                        "default": 5,
                        "description": "返回结果数量"
                    }
                },
                "required": ["query"]
            }
        ),
        types.Tool(
            name="ragflow_get_schema",
            description="获取指定表的结构详情，包括字段名、数据类型、注释、主键、外键等信息。",
            inputSchema={
                "type": "object",
                "properties": {
                    "table_name": {
                        "type": "string",
                        "description": "表名，例如：HQ_XS_STU、HQ_CODE_COURSE"
                    }
                },
                "required": ["table_name"]
            }
        ),
        types.Tool(
            name="ragflow_get_examples",
            description="获取与查询相似的 SQL 示例。根据用户问题，检索相关的 SQL 查询示例作为参考。",
            inputSchema={
                "type": "object",
                "properties": {
                    "query": {
                        "type": "string",
                        "description": "用户问题，例如：'每个专业有多少学生？'、'教师课程安排'"
                    },
                    "category": {
                        "type": "string",
                        "enum": ["all", "simple", "join", "aggregate"],
                        "default": "all",
                        "description": "查询类别"
                    },
                    "top_k": {
                        "type": "integer",
                        "default": 3,
                        "description": "返回示例数量"
                    }
                },
                "required": ["query"]
            }
        ),
        types.Tool(
            name="ragflow_health",
            description="检查本地 RAG 服务健康状态。",
            inputSchema={
                "type": "object",
                "properties": {}
            }
        )
    ]

@server.call_tool()
async def handle_call_tool(name: str, arguments: dict) -> list[types.TextContent]:
    """处理工具调用"""

    if name == "ragflow_search":
        query = arguments.get("query", "")
        dataset = arguments.get("dataset", "all")
        top_k = arguments.get("top_k", 5)

        if not query:
            return [types.TextContent(type="text", text="错误: query 参数不能为空")]

        results = rag_engine.search(query, category=dataset, top_k=top_k)

        output = []
        for i, r in enumerate(results[:top_k], 1):
            output.append(f"## 结果 {i} [{r.get('metadata', {}).get('type', 'unknown')}]\n")
            output.append(r.get('content', '')[:500])  # 限制长度
            output.append(f"\n(相关性: {r.get('score', 0):.2f})\n")

        return [types.TextContent(
            type="text",
            text="\n".join(output) if output else "未找到相关结果"
        )]

    elif name == "ragflow_get_schema":
        table_name = arguments.get("table_name", "")

        if not table_name:
            return [types.TextContent(type="text", text="错误: table_name 参数不能为空")]

        schema = rag_engine.get_schema(table_name)
        if schema:
            output = []
            output.append(f"## 表名: {schema.get('table_name', table_name)}\n")
            if schema.get('comment'):
                output.append(f"**说明**: {schema['comment']}\n")
            output.append("\n### 字段列表\n")
            output.append("| 字段名 | 类型 | 可空 | 说明 |\n")
            output.append("|--------|------|------|------|\n")
            for col in schema.get('columns', []):
                nullable = "是" if col.get('nullable') else "否"
                output.append(f"| {col['name']} | {col['type']} | {nullable} | {col.get('comment', '')} |\n")
            return [types.TextContent(type="text", text="\n".join(output))]

        # 回退到搜索
        results = rag_engine.search(f"{table_name} 表结构", category="ddl", top_k=1)
        if results:
            return [types.TextContent(type="text", text=results[0].get('content', ''))]

        return [types.TextContent(type="text", text=f"未找到表 {table_name} 的结构信息")]

    elif name == "ragflow_get_examples":
        query = arguments.get("query", "")
        category = arguments.get("category", "all")
        top_k = arguments.get("top_k", 3)

        if not query:
            return [types.TextContent(type="text", text="错误: query 参数不能为空")]

        results = rag_engine.search(query, category="examples", top_k=top_k)

        output = []
        for i, r in enumerate(results[:top_k], 1):
            content = r.get('content', '')
            output.append(f"## 示例 {i}\n")
            output.append(f"```\n{content[:1000]}\n```\n")
            output.append(f"(相关性: {r.get('score', 0):.2f})\n")

        return [types.TextContent(
            type="text",
            text="\n".join(output) if output else "未找到相关示例"
        )]

    elif name == "ragflow_health":
        healthy = rag_engine.health_check()
        status = "正常" if healthy else "异常"
        output = f"本地 RAG 服务状态: {status}\n"

        if healthy:
            for cat, docs in rag_engine.documents.items():
                output += f"  {cat}: {len(docs)} 个文档\n"

        return [types.TextContent(type="text", text=output)]

    else:
        return [types.TextContent(type="text", text=f"未知工具: {name}")]

# ============================================================================
# 主函数
# ============================================================================
async def main():
    global rag_engine, config

    parser = argparse.ArgumentParser(description="本地 RAG MCP Server")
    parser.add_argument("--knowledge-dir",
                       default=str(Path(__file__).parent.parent / "ragflow" / "knowledge"),
                       help="知识库目录")
    args = parser.parse_args()

    # 加载配置
    config = load_config()
    if args.knowledge_dir:
        config.knowledge_dir = args.knowledge_dir

    # 初始化 RAG 引擎
    print("初始化本地 RAG 引擎...")
    rag_engine = SimpleRAGEngine(config)
    rag_engine.initialize()

    # 运行服务器
    async with mcp.server.stdio.stdio_server() as (read_stream, write_stream):
        await server.run(
            read_stream,
            write_stream,
            InitializationOptions(
                server_name="local-rag-mcp-server",
                server_version="1.0.0",
                capabilities=server.get_capabilities(
                    notification_options=NotificationOptions(),
                    experimental_capabilities={}
                )
            )
        )

if __name__ == "__main__":
    asyncio.run(main())
