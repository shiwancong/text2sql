---
name: simple-query
description: 处理单表查询，支持简单的筛选和排序
---

# 单表查询 Skill

## 能力范围

处理涉及单张表的简单查询，包括：
- 查询单个表的全部或部分数据
- 简单的 WHERE 条件筛选
- 基础的 ORDER BY 排序
- LIMIT 结果数量限制

## 可用 MCP 工具

| 工具 | 说明 | 参数 |
|------|------|------|
| mcp__oracle__list_tables | 列出所有可访问的表 | 无 |
| mcp__oracle__describe_table | 获取表结构（字段名、类型、注释） | table_name: string |
| mcp__oracle__execute_query | 执行 SELECT 查询 | query: string (仅 SELECT) |
| mcp__ragflow__search | 在 RAGFlow 知识库中搜索相关表和字段 | query: string, dataset: string, top_k: int |
| mcp__ragflow__get_schema | 获取表结构详情 | table_name: string |
| mcp__ragflow__get_examples | 获取相似查询示例 | query: string, category: string, top_k: int |

## 执行流程

### 单问题处理

```
1. 接收用户问题
    │
    ▼
2. 调用 ragflow_search 检索相关表
    │
    ▼
3. 调用 ragflow_get_schema 获取表结构
    │
    ▼
4. 生成单表 SELECT 语句
    │
    ▼
5. 【重要】先展示生成的 SQL（不执行）
    │
    ▼
6. 使用 execute_query() 执行 SQL
    │
    ▼
7. 展示查询结果
```

### 批量问题处理

```
1. 识别用户输入中的多个问题（多个?、。、；分隔）
    │
    ▼
2. 使用 TodoWrite 创建任务列表
    │
    ▼
3. 循环处理每个问题：
   - 标记当前问题为 in_progress
   - 执行单问题处理流程（步骤2-7）
   - 确保输出完整的"执行sql"和"查询结果"
   - 标记当前问题为 completed
    │
    ▼
4. 所有问题处理完毕，清理任务列表
```

**重要：批量问题必须为每个问题都完整输出**
- ❌ 禁止：省略某些问题的输出
- ❌ 禁止：只显示结果不显示SQL
- ✅ 必须：每个问题都有"## 执行sql："和"查询结果"部分

## 输出格式规范

### 标准输出模板

```markdown
## 正在分析您的问题...

**用户问题**：{用户输入的问题}

**检索到的表**：{表名} - {表说明}

---

## 执行sql：

SELECT ...
FROM ...
WHERE ...
───────────────────────────
- 查询结果
   ┌──────────┬───────────┐
   │  字段1   │   值1     │
   ├──────────┼───────────┤
   │  字段2   │   值2     │
   └──────────┴───────────┘
   备注/说明

---
```

### 输出示例

```markdown
## 正在分析您的问题...

**用户问题**：闫亚君

**检索到的表**：HQ_XS_STU - 学生基本信息表

---

## 执行sql：

SELECT NAME_ AS 姓名, STU_NO AS 学号, PHONE AS 联系电话, CLASS_ID AS 班级ID, MAJOR_CODE AS 专业代码
FROM HQ_XS_STU
WHERE NAME_ = '闫亚君'
───────────────────────────
- 查询结果
   ┌──────────┬───────────────────────┐
   │   项目   │         信息          │
   ├──────────┼───────────────────────┤
   │ 姓名     │ 闫亚君                │
   ├──────────┼───────────────────────┤
   │ 学号     │ 201004120225          │
   ├──────────┼───────────────────────┤
   │ 联系电话 │ -                     │
   ├──────────┼───────────────────────┤
   │ 班级     │ 普专2010软件技术P02班 │
   ├──────────┼───────────────────────┤
   │ 专业     │ 软件技术              │
   └──────────┴───────────────────────┘
   注意：闫亚君是学生，不是教师。

---
```

## SQL 生成规则

### 基础模板

```sql
SELECT field1, field2, ...
FROM table_name
WHERE condition
ORDER BY field
FETCH FIRST n ROWS ONLY;
```

### 注意事项

- **表名和字段名必须大写**（Oracle 约定）
- **精确匹配优先**：当用户指定了明确的名称/条件时，优先使用精确匹配而非模糊匹配
- **避免过度拆分关键词**：用户输入的完整名称（如"线控底盘实训室"）应作为整体匹配，不要拆分成多个 OR 条件
- 优先使用有注释的字段，用户友好性更好
- 添加适当的 WHERE 条件避免返回过多数据
- 如果用户没有指定排序，按主键或默认字段排序
- Oracle 使用 `FETCH FIRST n ROWS ONLY` 而不是 `LIMIT`
- 对于单条记录查询，使用 `ROWNUM = 1` 或 `FETCH FIRST 1 ROW ONLY`

### WHERE 条件生成规则

#### 优先级 1：精确匹配（用户指定了完整名称）

当用户问题中包含明确的实体名称时：
```
用户问题："线控底盘实训室有多少个座位？"
→ WHERE NAME_ = '线控底盘实训室'
或 WHERE NAME_ LIKE '%线控底盘实训室%'

用户问题："李德声老师的联系方式"
→ WHERE NAME_ = '李德声'
或 WHERE NAME_ LIKE '%李德声%'
```

**错误示例**（禁止）：
```sql
-- 不要把完整名称拆分成多个 OR 条件
WHERE NAME_ LIKE '%线控底盘%' OR NAME_ LIKE '%底盘%' OR NAME_ LIKE '%实训%'
```

#### 优先级 2：模糊匹配（用户使用描述性词汇）

当用户使用描述性或类别性词汇时：
```
用户问题："实训室有哪些？"
→ WHERE JSLX_MC = '实训室'

用户问题："新能源汽车相关的实训室"
→ WHERE NAME_ LIKE '%新能源汽车%'
```

#### 优先级 3：范围查询（用户指定范围或条件）

当用户指定数量、时间等范围时：
```
用户问题："座位数大于50的实训室"
→ WHERE ZW_COUNT > 50 AND JSLX_MC = '实训室'
```

### 禁止使用硬编码ID原则

⚠️ **重要**：生成的SQL必须直接使用用户输入的名称，不要先查ID再用ID查询

```
❌ 错误：分两步查询
第一步：SELECT ID FROM HQ_CODE_DEPT WHERE NAME_ LIKE '%建工%'  → '10035'
第二步：SELECT NAME_ FROM HQ_CODE_DEPT_JYS WHERE DEPT_ID = '10035'

✅ 正确：一步到位，直接用名称
SELECT j.NAME_ AS 教研室名称
FROM HQ_CODE_DEPT_JYS j
JOIN HQ_CODE_DEPT d ON j.DEPT_ID = d.ID
WHERE d.NAME_ LIKE '%建工%'  -- 直接使用用户输入
```

**对比示例**：

| 用户问题 | ❌ 错误做法（用ID） | ✅ 正确做法（用名称） |
|---------|------------------|-------------------|
| 建工院有哪些教研室？ | `WHERE DEPT_ID = '10035'` | `WHERE d.NAME_ LIKE '%建工%'` |
| 闫静静所属的教研室？ | `WHERE TEA_NO = '10437'` | `WHERE t.NAME_ = '闫静静'` |
| 陶瓷琉璃艺术系有哪些专业？ | `WHERE DEPT_ID = '10047'` | `WHERE d.NAME_ LIKE '%陶瓷琉璃%'` |

### ISTRUE有效性检查（必须）

⚠️ **极重要**：所有查询都必须检查 ISTRUE 字段，确保只查询有效数据

```
❌ 错误：没有检查ISTRUE
SELECT COUNT(*) FROM HQ_CODE_MAJOR

✅ 正确：检查ISTRUE
SELECT COUNT(*) FROM HQ_CODE_MAJOR WHERE ISTRUE = 1

❌ 错误：子查询中忘记ISTRUE
SELECT COUNT(*) FROM HQ_CODE_MAJOR m WHERE m.ISTRUE = 1
AND NOT EXISTS (SELECT 1 FROM HQ_CODE_MAJOR_MAPPER mp WHERE mp.MAJOR_CODE = m.CODE_)

✅ 正确：所有表都检查ISTRUE
SELECT COUNT(*) FROM HQ_CODE_MAJOR m WHERE m.ISTRUE = 1
AND NOT EXISTS (
    SELECT 1 FROM HQ_CODE_MAJOR_MAPPER mp
    WHERE mp.MAJOR_CODE = m.CODE_ AND mp.ISTRUE = 1
)
```

**ISTRUE = 1 的常见场景**：
- 专业查询：`WHERE m.ISTRUE = 1`
- 课程查询：`WHERE c.ISTRUE = 1`
- 教研室查询：`WHERE j.ISTRUE = 1`
- 部门查询：`WHERE d.ISTRUE = 1`
- 班级查询：`WHERE cl.ISTRUE = 1`

### RAG 检索策略

当用户提出问题时：

1. **首先使用 RAG 检索相关表**
   ```
   调用 ragflow_search(query="用户问题关键词", dataset="ddl")
   ```

2. **获取表结构详情**
   ```
   调用 ragflow_get_schema(table_name="检索到的表名")
   ```

3. **可选：获取相似示例**
   ```
   调用 ragflow_get_examples(query="用户问题", category="simple")
   ```

4. **结合业务术语验证**
   - 参考 business-glossary.md 中的术语映射
   - 确保理解用户使用的业务词汇

### 示例映射

| 用户问题 | RAG 检索 | 生成 SQL |
|----------|----------|----------|
| "我们学校的名字是什么？" | 搜索"学校"、"学校信息" | `SELECT NAME_ FROM HQ_JC_XX WHERE ROWNUM = 1` |
| "我们今年的学期范围是几号到几号？" | 搜索"学期"、"学年" | `SELECT TEACH_BEGIN_DATE, TEACH_END_DATE FROM HQ_CODE_XNXQ WHERE BEGIN_DATE <= SYSDATE AND END_DATE >= SYSDATE` |
| "学校有哪些部门？" | 搜索"部门"、"学院" | `SELECT NAME_ FROM HQ_CODE_DEPT ORDER BY NAME_` |
| "有哪些核心课程？" | 搜索"课程"、"核心课" | `SELECT NAME_, COURSE_TYPE_CODE, CREDIT FROM HQ_CODE_COURSE WHERE IS_CORE = 1 ORDER BY NAME_` |
| "理实一体课有哪些？" | 搜索"理实一体"、"课程类型" | `SELECT NAME_, CREDIT FROM HQ_CODE_COURSE WHERE COURSE_TYPE_CODE IN (...) ORDER BY NAME_` |
| **"线控底盘实训室有多少个座位？"** | 搜索"线控底盘实训室" | `SELECT NAME_, ZW_COUNT FROM HQ_JC_JS_ZZJG WHERE NAME_ = '线控底盘实训室'` |
| **"李德声老师的联系方式"** | 搜索"李德声"、"教师" | `SELECT NAME_, PHONE FROM HQ_RS_TEA WHERE NAME_ = '李德声'` |

### 常见错误对比

| 用户问题 | ❌ 错误 SQL | ✅ 正确 SQL |
|----------|------------|------------|
| "线控底盘实训室有多少座位？" | `WHERE NAME_ LIKE '%线控底盘%' OR NAME_ LIKE '%底盘%' OR NAME_ LIKE '%实训%'` | `WHERE NAME_ = '线控底盘实训室'` |
| "李德声老师的电话" | `WHERE NAME_ LIKE '%李%' OR NAME_ LIKE '%德%' OR NAME_ LIKE '%声%'` | `WHERE NAME_ = '李德声'` |
| "新能源汽车实训室有哪些？" | `WHERE NAME_ LIKE '%新%' OR NAME_ LIKE '%能源%' OR NAME_ LIKE '%汽车%'` | `WHERE NAME_ LIKE '%新能源汽车%'` |

## 常见表名映射

| 业务概念 | RAG 搜索关键词 | 实际表名 |
|----------|---------------|----------|
| 学校信息 | 学校、学校信息、基本信息 | HQ_JC_XX |
| 学期 | 学期、学年、开学 | HQ_CODE_XNXQ |
| 部门 | 部门、学院、组织 | HQ_CODE_DEPT |
| 教师 | 教师、教工、教职工 | HQ_RS_TEA |
| 学生 | 学生、学员、在校生 | HQ_XS_STU |
| 课程 | 课程、科目、课表 | HQ_CODE_COURSE |
| 专业 | 专业、学科 | HQ_CODE_MAJOR |
| 班级 | 班级、行政班 | HQ_CODE_CLASSES |
| 教学班 | 教学班、课头 | HQ_JX_TEACHCLASS |
| 课程表 | 排课、上课安排 | HQ_JX_KCB |

## 时间相关查询处理

对于涉及"本学期"、"今年"等时间表达的查询：

1. **判断当前学期**
   - 使用 RAG 检索学期表的相关信息
   - 查询条件: `BEGIN_DATE <= SYSDATE AND END_DATE >= SYSDATE`

2. **检查数据是否存在**
   - 如果查询结果为空，明确告知用户"暂无当前学期数据"

3. **常用时间模式**
   ```sql
   -- 本学期
   WHERE BEGIN_DATE <= SYSDATE AND END_DATE >= SYSDATE

   -- 指定学年
   WHERE SCHOOL_YEAR = '2024-2025'

   -- 指定学期
   WHERE TERM_CODE = '01'  -- 01:上学期, 02:下学期
   ```

## 错误处理

| 错误 | 处理方式 |
|------|----------|
| 找不到相关表 | 尝试使用 ragflow_search 扩大搜索范围，或告知用户"没有找到相关数据" |
| SQL 执行失败 | 检查语法和字段名，使用 describe_table 确认字段，调整后重试 |
| 结果为空 | 告知用户"没有找到相关数据"，不要编造结果 |
| RAG 服务不可用 | 回退到直接使用 describe_table 和 list_tables |

## RAG 集成最佳实践

1. **优先使用 RAG**：对于所有查询，首先使用 RAG 检索相关表和字段
2. **验证结果**：结合业务术语知识库验证 RAG 返回的结果
3. **参考示例**：对于复杂查询，参考 RAG 检索到的相似示例
4. **友好提示**：如果 RAG 返回的结果不完整，主动向用户澄清需求
