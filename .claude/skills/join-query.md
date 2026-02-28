---
name: join-query
description: 处理 2-3 张表的 JOIN 查询，不涉及复杂聚合
---

# 多表联查 Skill

## 能力范围

处理需要关联 2-3 张表的查询：
- INNER JOIN / LEFT JOIN 表关联
- 多表 WHERE 条件筛选
- 跨表字段查询
- 不涉及复杂的 GROUP BY 聚合

## 可用 MCP 工具

| 工具 | 说明 | 参数 |
|------|------|------|
| mcp__oracle__list_tables | 列出所有可访问的表 | 无 |
| mcp__oracle__describe_table | 获取表结构（字段名、类型、注释） | table_name: string |
| mcp__oracle__execute_query | 执行 SELECT 查询 | query: string (仅 SELECT) |
| mcp__ragflow__search | 在 RAGFlow 知识库中搜索相关表和关系 | query: string, dataset: string, top_k: int |
| mcp__ragflow__get_schema | 获取表结构详情 | table_name: string |
| mcp__ragflow__get_examples | 获取相似 JOIN 查询示例 | query: string, category: string, top_k: int |

## 执行流程

### 单问题处理

```
1. 接收用户问题
    │
    ▼
2. 调用 ragflow_search 检索涉及的所有表
    │
    ▼
3. 调用 ragflow_get_examples 获取类似 JOIN 示例
    │
    ▼
4. 调用 ragflow_get_schema 获取各表结构
    │
    ▼
5. 参考 table-relationships.md 确定关联关系
    │
    ▼
6. 生成 JOIN 查询语句
    │
    ▼
7. 【重要】先展示生成的 SQL（不执行）
    │
    ▼
8. 使用 execute_query() 执行 SQL
    │
    ▼
9. 展示查询结果
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
   - 执行单问题处理流程（步骤2-9）
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

**检索到的表**：
- {表1} - {说明}
- {表2} - {说明}

**关联关系**：{表1}.{字段1} = {表2}.{字段2}

---

## 执行sql：

SELECT ...
FROM ... JOIN ...
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

## SQL 生成规则

### JOIN 模板

```sql
SELECT
    a.field1,
    b.field2,
    c.field3
FROM table_a a
INNER JOIN table_b b ON a.id = b.a_id
LEFT JOIN table_c c ON b.id = c.b_id
WHERE a.condition = 'value'
ORDER BY a.sort_field;
```

### JOIN 类型选择

| 场景 | JOIN 类型 | 说明 |
|------|-----------|------|
| 双方必须匹配 | INNER JOIN | 只返回关联上的记录 |
| 一方可能为空 | LEFT JOIN | 保留左表全部记录 |
| 查询条件可选 | LEFT JOIN | 允许关联字段为空 |

### RAG 检索策略

当用户提出涉及多个实体的问题时：

1. **识别涉及的实体**
   - 从问题中提取关键词（如"学生的课程"、"教师的排课"）
   - 调用 `ragflow_search(query="实体1 实体2 关系", dataset="all")`

2. **获取表关系**
   - 调用 `ragflow_search(query="表1 表2 关联", dataset="ddl")`
   - 参考 table-relationships.md 中的表关系定义

3. **获取相似示例**
   - 调用 `ragflow_get_examples(query="用户问题", category="join")`
   - 参考示例中的 JOIN 模式

### 关联字段推断

常见关联模式：
- 主键-外键：`a.ID = b.PARENT_ID`
- 业务关联：`a.CODE_ = b.CODE_`
- 中间表：`a.ID = ab.A_ID AND b.ID = ab.B_ID`

### 禁止使用硬编码ID原则

⚠️ **重要**：多表联查时，WHERE条件必须使用用户输入的名称，不要先查ID再用ID查询

```
❌ 错误：使用硬编码ID
SELECT j.NAME_ AS 教研室名称
FROM HQ_CODE_DEPT_JYS j
WHERE j.DEPT_ID = '10035'  -- 硬编码的ID

✅ 正确：使用名称匹配
SELECT j.NAME_ AS 教研室名称
FROM HQ_CODE_DEPT_JYS j
JOIN HQ_CODE_DEPT d ON j.DEPT_ID = d.ID
WHERE d.NAME_ LIKE '%建工%'  -- 直接使用用户输入
```

**对比示例**：

| 用户问题 | ❌ 错误做法 | ✅ 正确做法 |
|---------|-----------|-----------|
| 闫静静所属的教研室？ | `WHERE c.TEA_NO = '10437'` | `WHERE t.NAME_ = '闫静静'` |
| 专业负责人名单？ | `WHERE m.FZR_NO = '10437'` | `WHERE t.NAME_ = '李德声'` |
| 某学院教师名单？ | `WHERE DEPT_ID = '10035'` | `WHERE d.NAME_ LIKE '%建工%'` |

### ISTRUE有效性检查（必须）

⚠️ **极重要**：多表联查时，每个表都要检查 ISTRUE 字段

```
❌ 错误：没有检查ISTRUE
SELECT j.NAME_ AS 教研室名称
FROM HQ_CODE_DEPT_JYS j
JOIN HQ_CODE_DEPT d ON j.DEPT_ID = d.ID
WHERE d.NAME_ LIKE '%建工%'

✅ 正确：每个表都检查ISTRUE
SELECT j.NAME_ AS 教研室名称
FROM HQ_CODE_DEPT_JYS j
JOIN HQ_CODE_DEPT d ON j.DEPT_ID = d.ID
WHERE d.NAME_ LIKE '%建工%'
AND j.ISTRUE = 1
AND d.ISTRUE = 1
```

**ISTRUE = 1 的常见场景**：
- 教研室查询：`WHERE j.ISTRUE = 1`
- 部门查询：`WHERE d.ISTRUE = 1`
- 教师查询：`WHERE t.ISTRUE = 1`（如果表有此字段）
- 专业查询：`WHERE m.ISTRUE = 1`

## 实际表名关联关系

### 学生相关关联

| 源表 | 字段 | 目标表 | 关联字段 |
|------|------|--------|----------|
| HQ_XS_STU | CLASS_ID | HQ_CODE_CLASSES | NO_ |
| HQ_XS_STU | MAJOR_CODE | HQ_CODE_MAJOR | CODE_ |
| HQ_XS_STU | DEPT_ID | HQ_CODE_DEPT | ID |

### 教师相关关联

| 源表 | 字段 | 目标表 | 关联字段 |
|------|------|--------|----------|
| HQ_RS_TEA | DEPT_ID | HQ_CODE_DEPT | ID |
| HQ_CODE_MAJOR | FZR_NO | HQ_RS_TEA | TEA_NO |
| HQ_CODE_DEPT | FZR_NO | HQ_RS_TEA | TEA_NO |

### 课程相关关联

| 源表 | 字段 | 目标表 | 关联字段 |
|------|------|--------|----------|
| HQ_CODE_COURSE | MAJOR_ID | HQ_CODE_MAJOR | CODE_ |
| HQ_CODE_COURSE | DEPT_ID | HQ_CODE_DEPT | ID |
| HQ_CODE_MAJOR | DEPT_ID | HQ_CODE_DEPT | ID |
| HQ_CODE_CLASSES | MAJOR_ID | HQ_CODE_MAJOR | CODE_ |

### 示例映射

| 用户问题 | 涉及表 | SQL 示例 |
|----------|--------|----------|
| "专业负责人名单" | HQ_CODE_MAJOR, HQ_RS_TEA | `SELECT m.NAME_ AS 专业, t.NAME_ AS 负责人 FROM HQ_CODE_MAJOR m LEFT JOIN HQ_RS_TEA t ON m.FZR_NO = t.TEA_NO` |
| "部门负责人名单" | HQ_CODE_DEPT, HQ_RS_TEA | `SELECT d.NAME_ AS 部门, t.NAME_ AS 负责人 FROM HQ_CODE_DEPT d LEFT JOIN HQ_RS_TEA t ON d.FZR_NO = t.TEA_NO` |
| "学生的班级和专业信息" | HQ_XS_STU, HQ_CODE_CLASSES, HQ_CODE_MAJOR | `SELECT s.NAME_, c.NAME_, m.NAME_ FROM HQ_XS_STU s LEFT JOIN HQ_CODE_CLASSES c ON s.CLASS_ID = c.NO_ LEFT JOIN HQ_CODE_MAJOR m ON s.MAJOR_CODE = m.CODE_` |
| "教师所属学院" | HQ_RS_TEA, HQ_CODE_DEPT | `SELECT t.NAME_, t.ZW_NAME, d.NAME_ FROM HQ_RS_TEA t JOIN HQ_CODE_DEPT d ON t.DEPT_ID = d.ID` |

## 多表联查常见场景

### 学生-班级-专业-学院

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
LEFT JOIN HQ_CODE_DEPT d ON m.DEPT_ID = d.ID
WHERE s.STU_STATE_CODE = '01'
ORDER BY s.STU_NO;
```

### 专业/部门负责人

```sql
-- 专业负责人
SELECT
    m.NAME_ AS 专业名称,
    m.FZR_NO AS 负责人工号,
    t.NAME_ AS 负责人姓名,
    t.ZW_NAME AS 职称
FROM HQ_CODE_MAJOR m
LEFT JOIN HQ_RS_TEA t ON m.FZR_NO = t.TEA_NO
ORDER BY m.NAME_;

-- 部门负责人
SELECT
    d.NAME_ AS 部门名称,
    d.FZR_NO AS 负责人工号,
    t.NAME_ AS 负责人姓名,
    t.ZW_NAME AS 职称
FROM HQ_CODE_DEPT d
LEFT JOIN HQ_RS_TEA t ON d.FZR_NO = t.TEA_NO
ORDER BY d.NAME_;
```

### 课程-教师-教室

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

## 错误处理

| 错误 | 处理方式 |
|------|----------|
| 找不到表间关系 | 使用 ragflow_search 搜索表关系，或基于字段名推断 |
| JOIN 字段不匹配 | 检查字段类型，使用 describe_table 确认字段 |
| 结果为空 | 尝试 LEFT JOIN，或告知用户"没有找到相关数据" |
| 笛卡尔积 | 检查 JOIN 条件，确保有关联字段 |

## RAG 集成最佳实践

1. **多源检索**：同时检索 DDL 知识库和示例知识库
2. **关系验证**：使用 RAG 检索到的表关系验证 JOIN 条件
3. **示例参考**：优先参考 RAG 检索到的相似 JOIN 示例
4. **逐步构建**：先确定主表，再逐步添加关联表
