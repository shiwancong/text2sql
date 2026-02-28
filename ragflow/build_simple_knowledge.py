#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
简化版知识库构建脚本

不连接数据库，基于现有业务知识库生成 RAG 知识库
"""

import json
import os
from pathlib import Path
from datetime import datetime

# 输出目录
OUTPUT_DIR = Path(__file__).parent / 'knowledge'
DDL_DIR = OUTPUT_DIR / 'ddl'
DESC_DIR = OUTPUT_DIR / 'descriptions'
EX_DIR = OUTPUT_DIR / 'examples'

# ============================================================================
# 从 business-glossary.md 构建知识库
# ============================================================================
def build_from_glossary():
    """从业务术语库构建知识库"""
    print("正在从业务术语库构建知识库...")

    glossary_file = Path(__file__).parent.parent / '.claude' / 'knowledge' / 'business-glossary.md'
    if not glossary_file.exists():
        print(f"  未找到业务术语库: {glossary_file}")
        return False

    with open(glossary_file, encoding='utf-8') as f:
        content = f.read()

    # 1. 提取表名映射
    tables_info = {}
    lines = content.split('\n')
    i = 0
    while i < len(lines):
        line = lines[i]
        if '| 业务概念 | 实际表名 |' in line:
            # 进入表映射区域
            i += 2
            while i < len(lines) and lines[i].startswith('|'):
                parts = [p.strip() for p in lines[i].split('|')]
                if len(parts) >= 4 and parts[1] and parts[2]:
                    concept = parts[1]
                    table_name = parts[2]
                    desc = parts[3] if len(parts) > 3 else ''
                    tables_info[table_name] = {
                        'concept': concept,
                        'description': desc
                    }
                i += 1
        i += 1

    # 2. 构建表结构知识库（基于已知表信息）
    tables_data = {}
    for table_name, info in tables_info.items():
        tables_data[table_name] = {
            'table_name': table_name,
            'comment': info['description'],
            'business_concept': info['concept'],
            'columns': [],  # 简化版，不包含详细字段
            'primary_keys': [],
            'foreign_keys': []
        }

    # 保存表结构
    (DDL_DIR / 'tables.json').write_text(
        json.dumps(tables_data, ensure_ascii=False, indent=2),
        encoding='utf-8'
    )

    # 保存表关系（从 table-relationships.md 提取）
    relationships_file = Path(__file__).parent.parent / '.claude' / 'knowledge' / 'table-relationships.md'
    relationships = []

    if relationships_file.exists():
        with open(relationships_file, encoding='utf-8') as f:
            rel_content = f.read()

        # 提取关联关系
        for table_name in tables_info.keys():
            # 简化版关系提取
            for line in rel_content.split('\n'):
                if table_name in line and '→' in line:
                    # 这是一个关系行
                    relationships.append({
                        'source': table_name,
                        'relation': 'related_to',
                        'description': line.strip()
                    })

    (DDL_DIR / 'relationships.json').write_text(
        json.dumps(relationships, ensure_ascii=False, indent=2),
        encoding='utf-8'
    )

    print(f"  已生成表结构: {len(tables_data)} 个表")
    print(f"  已生成表关系: {len(relationships)} 条")
    return True

# ============================================================================
# 构建业务描述知识库
# ============================================================================
def build_description_knowledge():
    """构建业务描述知识库"""
    print("正在构建业务描述知识库...")

    # 从 business-glossary.md 提取业务描述
    glossary_file = Path(__file__).parent.parent / '.claude' / 'knowledge' / 'business-glossary.md'

    if not glossary_file.exists():
        print(f"  未找到业务术语库")
        return False

    with open(glossary_file, encoding='utf-8') as f:
        content = f.read()

    # 生成表描述
    tables_md = []
    tables_md.append("# 表业务描述\n\n")
    tables_md.append("## 核心业务表\n\n")

    # 从 content 中提取表信息
    core_tables = {
        'HQ_JC_XX': '学校基本信息',
        'HQ_JC_XQ': '校区信息',
        'HQ_CODE_XNXQ': '学年学期配置',
        'HQ_JX_KCB': '课程排课信息',
        'HQ_CODE_COURSE': '课程基本信息',
        'HQ_JX_TEACHCLASS': '教学班信息',
        'HQ_XS_STU': '学生基本信息',
        'HQ_RS_TEA': '教师基本信息',
        'HQ_CODE_MAJOR': '专业信息',
        'HQ_CODE_DEPT': '组织机构(部门/学院/专业)',
        'HQ_CODE_CLASSES': '班级信息'
    }

    for table, desc in core_tables.items():
        tables_md.append(f"### {table}\n\n")
        tables_md.append(f"**业务说明**: {desc}\n\n")

    (DESC_DIR / 'tables.md').write_text(
        ''.join(tables_md),
        encoding='utf-8'
    )

    # 生成字段描述
    fields_md = []
    fields_md.append("# 字段业务说明\n\n")

    # 提取字段映射
    sections = {
        '学生相关字段': ['学号', '姓名', '性别', '民族', '班级', '专业', '学院'],
        '教师相关字段': ['教工号', '姓名', '职称', '学历', '学位', '入职日期'],
        '课程相关字段': ['课程代码', '课程名称', '课程类型', '课程性质', '学分', '课时'],
        '学期相关字段': ['学年', '学期代码', '开学时间', '结课时间', '教学开始', '教学结束']
    }

    for section, fields in sections.items():
        fields_md.append(f"## {section}\n\n")
        for field in fields:
            # 从 content 中查找字段说明
            for line in content.split('\n'):
                if field in line and '|' in line:
                    fields_md.append(f"{line}\n")
                    break
        fields_md.append("\n")

    (DESC_DIR / 'fields.md').write_text(
        ''.join(fields_md),
        encoding='utf-8'
    )

    print("  已生成表描述和字段说明")
    return True

# ============================================================================
# 构建查询示例知识库
# ============================================================================
def build_examples_knowledge():
    """构建查询示例知识库"""
    print("正在构建查询示例知识库...")

    # 直接使用预先定义的示例
    simple_examples = """# 单表查询示例 (C级)

## 学校信息查询

**问题**: 我们学校的名字是什么？
```sql
SELECT NAME_ FROM HQ_JC_XX WHERE ROWNUM = 1;
```

**问题**: 学校有哪些校区？
```sql
SELECT NAME_ FROM HQ_JC_XQ ORDER BY NAME_;
```

## 学期查询

**问题**: 我们今年的学期范围是几号到几号？
```sql
SELECT
    SCHOOL_YEAR AS 学年,
    TERM_CODE AS 学期,
    TEACH_BEGIN_DATE AS 教学开始日期,
    TEACH_END_DATE AS 教学结束日期
FROM HQ_CODE_XNXQ
ORDER BY BEGIN_DATE DESC
FETCH FIRST 1 ROW ONLY;
```

## 部门/学院查询

**问题**: 学校有哪些部门？
```sql
SELECT NAME_ FROM HQ_CODE_DEPT ORDER BY NAME_;
```

## 课程查询

**问题**: 有哪些核心课程？
```sql
SELECT NAME_, COURSE_TYPE_CODE, CREDIT
FROM HQ_CODE_COURSE
WHERE IS_CORE = 1
ORDER BY NAME_;
```

## 专业查询

**问题**: 有哪些专业？
```sql
SELECT CODE_, NAME_, PYCC_CODE
FROM HQ_CODE_MAJOR
ORDER BY CODE_;
```

## 教师查询

**问题**: 有多少教师？
```sql
SELECT COUNT(*) AS 教师总数 FROM HQ_RS_TEA;
```

## 学生查询

**问题**: 有多少在校学生？
```sql
SELECT COUNT(*) AS 学生总数 FROM HQ_XS_STU WHERE STU_STATE_CODE = '01';
```

**问题**: 有多少少数民族学生？
```sql
SELECT COUNT(*) AS 少数民族学生数
FROM HQ_XS_STU
WHERE NATION_CODE != '01' AND STU_STATE_CODE = '01';
```
"""

    join_examples = """# 多表联查示例 (B级)

## 学生-班级-专业联查

**问题**: 2024级学生属于哪些班级和专业？
```sql
SELECT
    s.STU_NO AS 学号,
    s.NAME_ AS 姓名,
    c.NAME_ AS 班级,
    m.NAME_ AS 专业,
    d.NAME_ AS 学院
FROM HQ_XS_STU s
LEFT JOIN HQ_CODE_CLASSES c ON s.CLASS_ID = c.NO_
LEFT JOIN HQ_CODE_MAJOR m ON s.MAJOR_CODE = m.CODE_
LEFT JOIN HQ_CODE_DEPT d ON s.DEPT_ID = d.ID
WHERE s.ENROLL_YEAR = '2024'
ORDER BY s.STU_NO;
```

## 教师-部门联查

**问题**: 专业负责人名单
```sql
SELECT
    m.NAME_ AS 专业名称,
    m.FZR_NO AS 负责人工号,
    t.NAME_ AS 负责人姓名,
    t.ZW_NAME AS 职称
FROM HQ_CODE_MAJOR m
LEFT JOIN HQ_RS_TEA t ON m.FZR_NO = t.TEA_NO
ORDER BY m.NAME_;
```

**问题**: 部门负责人名单
```sql
SELECT
    d.NAME_ AS 部门名称,
    d.FZR_NO AS 负责人工号,
    t.NAME_ AS 负责人姓名,
    t.ZW_NAME AS 职称
FROM HQ_CODE_DEPT d
LEFT JOIN HQ_RS_TEA t ON d.FZR_NO = t.TEA_NO
ORDER BY d.NAME_;
```

## 课程-教师-教室联查

**问题**: 查询课程安排的上课地点
```sql
SELECT
    cr.NAME_ AS 课程,
    t.NAME_ AS 教师,
    k.CLASSROOM_ID AS 教室,
    k.DAY_OF_WEEK AS 星期,
    k.PERIOD AS 节次
FROM HQ_JX_KCB k
JOIN HQ_CODE_COURSE cr ON k.COURSE_ID = cr.CODE_
JOIN HQ_RS_TEA t ON k.TEACHER_ID = t.TEA_NO
ORDER BY k.DAY_OF_WEEK, k.PERIOD;
```
"""

    aggregate_examples = """# 聚合查询示例 (A/S级)

## 计数统计

**问题**: 每个专业有多少学生？
```sql
SELECT
    m.NAME_ AS 专业名称,
    COUNT(s.STU_NO) AS 学生人数
FROM HQ_CODE_MAJOR m
LEFT JOIN HQ_XS_STU s ON m.CODE_ = s.MAJOR_CODE AND s.STU_STATE_CODE = '01'
GROUP BY m.NAME_
ORDER BY COUNT(s.STU_NO) DESC;
```

**问题**: 各学院的学生人数
```sql
SELECT
    d.NAME_ AS 学院名称,
    COUNT(s.STU_NO) AS 学生人数
FROM HQ_CODE_DEPT d
LEFT JOIN HQ_CODE_MAJOR m ON d.ID = m.DEPT_ID
LEFT JOIN HQ_XS_STU s ON m.CODE_ = s.MAJOR_CODE AND s.STU_STATE_CODE = '01'
GROUP BY d.NAME_
ORDER BY COUNT(s.STU_NO) DESC;
```

## 比例统计

**问题**: 少数民族学生比例
```sql
SELECT
    COUNT(CASE WHEN s.NATION_CODE != '01' THEN 1 END) AS 少数民族人数,
    COUNT(*) AS 总人数,
    ROUND(COUNT(CASE WHEN s.NATION_CODE != '01' THEN 1 END) * 100.0 / COUNT(*), 2) AS 比例百分比
FROM HQ_XS_STU s
WHERE s.STU_STATE_CODE = '01';
```

**问题**: 男女学生比例
```sql
SELECT
    COUNT(CASE WHEN s.SEX_CODE = '1' THEN 1 END) AS 男生人数,
    COUNT(CASE WHEN s.SEX_CODE = '2' THEN 1 END) AS 女生人数,
    COUNT(*) AS 总人数,
    ROUND(COUNT(CASE WHEN s.SEX_CODE = '1' THEN 1 END) * 100.0 / COUNT(*), 2) AS 男生比例,
    ROUND(COUNT(CASE WHEN s.SEX_CODE = '2' THEN 1 END) * 100.0 / COUNT(*), 2) AS 女生比例
FROM HQ_XS_STU s
WHERE s.STU_STATE_CODE = '01';
```

**问题**: 各培养层次学生比例
```sql
SELECT
    CASE s.PYCC_CODE
        WHEN '1' THEN '博士'
        WHEN '2' THEN '硕士'
        WHEN '3' THEN '本科'
        WHEN '4' THEN '专科'
        ELSE '其他'
    END AS 培养层次,
    COUNT(*) AS 人数,
    ROUND(COUNT(*) * 100.0 / SUM(COUNT(*)) OVER(), 2) AS 比例
FROM HQ_XS_STU s
WHERE s.STU_STATE_CODE = '01'
GROUP BY s.PYCC_CODE
ORDER BY COUNT(*) DESC;
```

## 排名统计

**问题**: 专业学生人数排名
```sql
SELECT
    m.NAME_ AS 专业名称,
    COUNT(s.STU_NO) AS 学生人数,
    RANK() OVER (ORDER BY COUNT(s.STU_NO) DESC) AS 排名
FROM HQ_CODE_MAJOR m
LEFT JOIN HQ_XS_STU s ON m.CODE_ = s.MAJOR_CODE AND s.STU_STATE_CODE = '01'
GROUP BY m.NAME_
ORDER BY COUNT(s.STU_NO) DESC;
```
"""

    # 保存示例文件
    (EX_DIR / 'simple.md').write_text(simple_examples, encoding='utf-8')
    (EX_DIR / 'join.md').write_text(join_examples, encoding='utf-8')
    (EX_DIR / 'aggregate.md').write_text(aggregate_examples, encoding='utf-8')

    print("  已生成查询示例")
    return True

# ============================================================================
# 主函数
# ============================================================================
def main():
    """主函数"""
    print("=" * 60)
    print("RAGFlow 知识库构建脚本 (简化版)")
    print("=" * 60)
    print(f"输出目录: {OUTPUT_DIR}")
    print()

    # 确保目录存在
    DDL_DIR.mkdir(parents=True, exist_ok=True)
    DESC_DIR.mkdir(parents=True, exist_ok=True)
    EX_DIR.mkdir(parents=True, exist_ok=True)

    # 构建三类知识库
    success = True
    if not build_from_glossary():
        success = False
    print()
    if not build_description_knowledge():
        success = False
    print()
    if not build_examples_knowledge():
        success = False
    print()

    if success:
        print("=" * 60)
        print("知识库构建完成！")
        print("=" * 60)
        print()
        print("下一步：")
        print("1. 重启 Claude Code")
        print("2. 测试查询，例如：'学校有哪些部门？'")
    else:
        print("部分知识库构建失败，请检查文件路径")

if __name__ == "__main__":
    main()
