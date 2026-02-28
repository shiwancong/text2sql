---
name: aggregate-query
description: 处理带聚合函数的复杂查询，包括 GROUP BY、子查询、CASE WHEN
---

# 聚合查询 Skill

## 能力范围

处理涉及统计和聚合的复杂查询：
- GROUP BY 分组统计
- 聚合函数：COUNT、SUM、AVG、MAX、MIN
- 子查询、CASE WHEN、多层级聚合
- 比例计算、排名统计

## 可用 MCP 工具

| 工具 | 说明 | 参数 |
|------|------|------|
| mcp__oracle__list_tables | 列出所有可访问的表 | 无 |
| mcp__oracle__describe_table | 获取表结构（字段名、类型、注释） | table_name: string |
| mcp__oracle__execute_query | 执行 SELECT 查询 | query: string (仅 SELECT) |
| mcp__ragflow__search | 在 RAGFlow 知识库中搜索相关表和字段 | query: string, dataset: string, top_k: int |
| mcp__ragflow__get_schema | 获取表结构详情 | table_name: string |
| mcp__ragflow__get_examples | 获取相似聚合查询示例 | query: string, category: string, top_k: int |

## 执行流程

### 单问题处理

```
1. 接收用户问题
    │
    ▼
2. 识别聚合类型（计数/求和/平均/比例）
    │
    ▼
3. 调用 ragflow_search 检索相关表
    │
    ▼
4. 调用 ragflow_get_examples 获取聚合查询示例
    │
    ▼
5. 确定分组字段 (GROUP BY)
    │
    ▼
6. 识别涉及的表和关联关系
    │
    ▼
7. 生成聚合查询 SQL
    │
    ▼
8. 【重要】先展示生成的 SQL（不执行）
    │
    ▼
9. 使用 execute_query() 执行 SQL
    │
    ▼
10. 展示查询结果
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
   - 执行单问题处理流程（步骤2-10）
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

**聚合类型**：{计数/求和/平均/比例/排名}

**检索到的表**：{表名} - {表说明}

**分组字段**：{GROUP BY 的字段}

---

## 执行sql：

SELECT ..., COUNT(*) as count
FROM ...
GROUP BY ...
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

## 聚合函数映射

| 用户意图 | 关键词 | SQL 函数 |
|----------|--------|----------|
| 计数 | 有多少、数量、几个、Count | COUNT(*) / COUNT(DISTINCT field) |
| 求和 | 总计、一共、合计、Sum | SUM(field) |
| 平均 | 平均、人均、Avg | AVG(field) |
| 最大 | 最高、最大、Max | MAX(field) |
| 最小 | 最小、最低、Min | MIN(field) |
| 比例 | 占比、百分比、Percent | CASE WHEN + COUNT / SUM |
| 排名 | 第几、排名、Rank | RANK() / DENSE_RANK() |

## RAG 检索策略

### 1. 识别聚合类型后检索

```
计数类查询:
  ragflow_search(query="计数 学生人数", dataset="examples")

比例类查询:
  ragflow_search(query="比例 占比 百分比", dataset="examples")

排名类查询:
  ragflow_search(query="排名 排序", dataset="examples")
```

### 2. 获取相似示例

```
ragflow_get_examples(
  query="每个专业有多少学生？",
  category="aggregate"
)
```

## SQL 模板

### 基础分组统计

```sql
SELECT
    group_field,
    COUNT(*) as count,
    SUM(num_field) as total,
    AVG(num_field) as average
FROM table_name
WHERE condition
GROUP BY group_field
ORDER BY count DESC;
```

### 比例计算

```sql
-- 方法一：使用窗口函数
SELECT
    group_field,
    COUNT(*) as count,
    ROUND(COUNT(*) * 100.0 / SUM(COUNT(*)) OVER(), 2) as percentage
FROM table_name
GROUP BY group_field;

-- 方法二：使用子查询
SELECT
    group_field,
    COUNT(*) as count,
    ROUND(COUNT(*) * 100.0 / (SELECT COUNT(*) FROM table_name), 2) as percentage
FROM table_name
GROUP BY group_field;
```

### CASE WHEN 条件统计

```sql
SELECT
    COUNT(*) as total,
    SUM(CASE WHEN condition THEN 1 ELSE 0 END) as match_count,
    ROUND(SUM(CASE WHEN condition THEN 1 ELSE 0 END) * 100.0 / COUNT(*), 2) as percentage
FROM table_name;
```

### 禁止使用硬编码ID原则

⚠️ **重要**：聚合查询时，WHERE条件必须使用用户输入的名称，不要先查ID再用ID查询

```
❌ 错误：使用硬编码ID
SELECT COUNT(*) AS 学生人数
FROM HQ_XS_STU
WHERE MAJOR_CODE = '6501155'  -- 硬编码的专业代码

✅ 正确：使用名称匹配
SELECT COUNT(*) AS 学生人数
FROM HQ_XS_STU s
JOIN HQ_CODE_MAJOR m ON s.MAJOR_CODE = m.CODE_
WHERE m.NAME_ LIKE '%陶瓷设计与工艺%'  -- 直接使用用户输入
```

**对比示例**：

| 用户问题 | ❌ 错误做法 | ✅ 正确做法 |
|---------|-----------|-----------|
| 各专业学生人数 | `GROUP BY MAJOR_CODE` | `JOIN HQ_CODE_MAJOR m ... GROUP BY m.NAME_` |
| 某学院教师人数 | `WHERE DEPT_ID = '10035'` | `WHERE d.NAME_ LIKE '%建工%'` |
| 某系开设专业 | `WHERE DEPT_ID = '10047'` | `WHERE d.NAME_ LIKE '%陶瓷琉璃%'` |

### ISTRUE有效性检查（必须）

⚠️ **极重要**：聚合查询时，所有表都要检查 ISTRUE 字段

```
❌ 错误：没有检查ISTRUE（结果错误：146个专业）
SELECT COUNT(*) AS 专业数量
FROM HQ_CODE_MAJOR m
WHERE NOT EXISTS (
    SELECT 1 FROM HQ_CODE_MAJOR_MAPPER mp WHERE mp.MAJOR_CODE = m.CODE_
)

✅ 正确：所有表都检查ISTRUE（结果正确：19个专业）
SELECT COUNT(*) AS 专业数量
FROM HQ_CODE_MAJOR m
WHERE m.ISTRUE = 1
AND NOT EXISTS (
    SELECT 1 FROM HQ_CODE_MAJOR_MAPPER mp
    WHERE mp.MAJOR_CODE = m.CODE_ AND mp.ISTRUE = 1
)
```

**ISTRUE = 1 的常见场景**：
- 专业统计：`WHERE m.ISTRUE = 1`
- 课程统计：`WHERE c.ISTRUE = 1`
- 学生统计：`WHERE s.STU_STATE_CODE = '01'`（在校学生）
- 教师统计：`WHERE t.ZW_NAME IS NOT NULL`（有职称）

### 多层级聚合

```sql
SELECT
    dept_name,
    major_name,
    COUNT(*) as student_count
FROM student s
JOIN major m ON s.major_id = m.id
JOIN department d ON m.dept_id = d.id
GROUP BY ROLLUP(dept_name, major_name)
ORDER BY dept_name, major_name;
```

### 排名

```sql
-- RANK() - 并列时跳过后续排名
SELECT
    field,
    COUNT(*),
    RANK() OVER (ORDER BY COUNT(*) DESC) as rank_value
FROM table_name
GROUP BY field;

-- DENSE_RANK() - 并列时不跳过后续排名
SELECT
    field,
    COUNT(*),
    DENSE_RANK() OVER (ORDER BY COUNT(*) DESC) as rank_value
FROM table_name
GROUP BY field;
```

## 常见聚合场景

### 学生统计

```sql
-- 各专业学生人数
SELECT
    m.NAME_ AS 专业名称,
    COUNT(s.STU_NO) AS 学生人数
FROM HQ_CODE_MAJOR m
LEFT JOIN HQ_XS_STU s ON m.CODE_ = s.MAJOR_CODE AND s.STU_STATE_CODE = '01'
GROUP BY m.NAME_
ORDER BY COUNT(s.STU_NO) DESC;

-- 各学院学生人数
SELECT
    d.NAME_ AS 学院名称,
    COUNT(s.STU_NO) AS 学生人数
FROM HQ_CODE_DEPT d
LEFT JOIN HQ_CODE_MAJOR m ON d.ID = m.DEPT_ID
LEFT JOIN HQ_XS_STU s ON m.CODE_ = s.MAJOR_CODE AND s.STU_STATE_CODE = '01'
GROUP BY d.NAME_
ORDER BY COUNT(s.STU_NO) DESC;

-- 民族分布（含比例）
SELECT
    CASE s.NATION_CODE
        WHEN '01' THEN '汉族'
        ELSE '少数民族'
    END AS 民族类别,
    COUNT(*) AS 人数,
    ROUND(COUNT(*) * 100.0 / SUM(COUNT(*)) OVER(), 2) AS 比例
FROM HQ_XS_STU s
WHERE s.STU_STATE_CODE = '01'
GROUP BY CASE s.NATION_CODE WHEN '01' THEN '汉族' ELSE '少数民族' END;
```

### 性别统计

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

### 教师统计

```sql
-- 各学院教师人数
SELECT
    d.NAME_ AS 学院,
    COUNT(t.TEA_NO) AS 教师人数
FROM HQ_CODE_DEPT d
LEFT JOIN HQ_RS_TEA t ON d.ID = t.DEPT_ID
GROUP BY d.NAME_
ORDER BY COUNT(t.TEA_NO) DESC;

-- 各职称教师人数
SELECT
    t.ZW_NAME AS 职称,
    COUNT(*) AS 教师人数
FROM HQ_RS_TEA t
WHERE t.ZW_NAME IS NOT NULL
GROUP BY t.ZW_NAME
ORDER BY COUNT(*) DESC;
```

### 培养层次统计

```sql
SELECT
    CASE s.PYCC_CODE
        WHEN '1' THEN '博士'
        WHEN '2' THEN '硕士'
        WHEN '3' THEN '本科'
        WHEN '4' THEN '专科'
        ELSE '其他'
    END AS 培养层次,
    COUNT(*) AS 学生人数,
    ROUND(COUNT(*) * 100.0 / SUM(COUNT(*)) OVER(), 2) AS 比例
FROM HQ_XS_STU s
WHERE s.STU_STATE_CODE = '01'
GROUP BY s.PYCC_CODE
ORDER BY COUNT(*) DESC;
```

### 专业学生排名

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

## 注意事项

1. **GROUP BY 字段**：SELECT 中的非聚合字段必须出现在 GROUP BY 中
2. **NULL 处理**：聚合函数默认忽略 NULL，使用 COUNT(*) 包含 NULL
3. **精度控制**：使用 ROUND() 控制小数位数
4. **性能优化**：先 WHERE 过滤再 GROUP BY，减少计算量
5. **Oracle 特性**：
   - 使用 `FETCH FIRST n ROWS ONLY` 而不是 `LIMIT`
   - 使用 `ROLLUP` 或 `CUBE` 进行多层级聚合
   - 窗口函数：`RANK()`, `DENSE_RANK()`, `ROW_NUMBER()`

## 错误处理

| 错误 | 处理方式 |
|------|----------|
| 除零错误 | 使用 `NULLIF(divisor, 0)` 或 `CASE WHEN` 检查分母 |
| GROUP BY 字段缺失 | 检查 SELECT 字段，确保非聚合字段都在 GROUP BY 中 |
| 聚合结果异常 | 检查数据类型，确保字段可以聚合 |
| 结果为空 | 告知用户"没有找到相关数据" |

## RAG 集成最佳实践

1. **关键词检索**：使用聚合关键词检索相似示例
2. **模式参考**：优先使用 RAG 检索到的查询模式
3. **分步验证**：
   - 先用 RAG 检索确定聚合类型
   - 再检索获取相似示例
   - 最后参考示例生成 SQL
4. **复杂降级**：如果 RAG 检索失败，逐步简化查询
