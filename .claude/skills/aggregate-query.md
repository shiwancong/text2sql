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

### 代码字段关联（禁止硬编码CASE WHEN）

⚠️ **极重要**：聚合查询中显示代码对应的名称时，必须关联代码表，禁止使用硬编码的CASE WHEN

```
❌ 错误：使用硬编码的CASE WHEN（民族分布统计）
SELECT
  s.NATION_CODE,
  CASE s.NATION_CODE
    WHEN '01' THEN '汉族'
    WHEN '03' THEN '回族'
    WHEN '05' THEN '苗族'
    ELSE s.NATION_CODE
  END AS 民族,
  COUNT(*) AS 人数
FROM HQ_XS_STU s
GROUP BY s.NATION_CODE
问题：硬编码了民族映射，新增民族需要修改SQL

✅ 正确：关联HQ_CODE表获取民族名称
SELECT
  s.NATION_CODE AS 民族代码,
  c.NAME_ AS 民族,
  COUNT(*) AS 人数
FROM HQ_XS_STU s
JOIN HQ_CODE c ON c.CODE_ = s.NATION_CODE
WHERE c.CODE_TYPE = 'NATION'  -- 根据实际表结构调整
GROUP BY s.NATION_CODE, c.NAME_
ORDER BY COUNT(*) DESC
优势：自动从代码表获取最新数据
```

**常见聚合查询中的代码关联：**

| 聚合场景 | 代码字段 | 关联方式 |
|---------|---------|---------|
| 各民族学生分布 | NATION_CODE | `JOIN HQ_CODE c ON c.CODE_ = s.NATION_CODE WHERE c.CODE_TYPE = 'NATION'` |
| 各性别学生分布 | SEX_CODE | `JOIN HQ_CODE c ON c.CODE_ = s.SEX_CODE WHERE c.CODE_TYPE = 'SEX'` |
| 各学籍状态分布 | STU_STATE_CODE | `JOIN HQ_CODE c ON c.CODE_ = s.STU_STATE_CODE WHERE c.CODE_TYPE = 'STU_STATE'` |
| 各培养层次分布 | PYCC_CODE | `JOIN HQ_CODE c ON c.CODE_ = s.PYCC_CODE WHERE c.CODE_TYPE = 'PYCC'` |

**聚合查询 + 代码关联模板：**

```sql
SELECT
  c.NAME_ AS 分类名称,
  COUNT(*) AS 数量,
  ROUND(COUNT(*) * 100.0 / SUM(COUNT(*)) OVER(), 2) AS 比例
FROM 数据表 main_table
JOIN HQ_CODE c ON c.CODE_ = main_table.XXX_CODE
WHERE c.CODE_TYPE = 'XXX_CODE_TYPE'  -- 根据实际代码类型调整
  AND main_table.IS_NORMAL = 1       -- 根据业务需求添加
GROUP BY c.NAME_
ORDER BY COUNT(*) DESC
```

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
   - ⚠️ **禁止使用 FETCH FIRST**：使用 `ROWNUM <= n` 或子查询方式
   - 使用 `ROLLUP` 或 `CUBE` 进行多层级聚合
   - 窗口函数：`RANK()`, `DENSE_RANK()`, `ROW_NUMBER()`, `LAG()`

### COUNT 语法（极重要）

⚠️ **聚合查询中必须使用 COUNT(*)，不能使用 COUNT()**

```sql
-- ❌ 错误写法
SELECT COUNT() FROM table_name  -- 空括号是错误的

-- ✅ 正确写法
SELECT COUNT(*) FROM table_name
SELECT COUNT(DISTINCT field) FROM table_name

-- ✅ 计算比例时的正确写法
SELECT
    COUNT(CASE WHEN condition THEN 1 END) AS match_count,
    COUNT(*) AS total_count,
    ROUND(COUNT(CASE WHEN condition THEN 1 END) * 100.0 / COUNT(*), 2) AS percentage
FROM table_name
```

### 连续性判断（LAG窗口函数）

⚠️ **极重要**：当题目要求"连续N年/连续N学期"时，必须使用LAG窗口函数判断连续性

**场景1：连续三年获得教学成果奖项的二级学院**

```sql
-- ❌ 错误：只统计不同年份数量，未判断连续性
SELECT d.NAME_ AS 学院名称
FROM HQ_RS_TEACH_RES r
JOIN HQ_CODE_DEPT d ON r.DEPT_ID = d.ID
GROUP BY d.NAME_
HAVING COUNT(DISTINCT SUBSTR(r.DATE_, 1, 4)) >= 3

-- ✅ 正确：使用LAG判断年份连续性
WITH ranked_data AS (
  SELECT
    d.NAME_ AS 学院名称,
    SUBSTR(r.DATE_, 1, 4) AS 年份,
    LAG(SUBSTR(r.DATE_, 1, 4), 1) OVER (PARTITION BY d.ID ORDER BY SUBSTR(r.DATE_, 1, 4)) AS 前一年,
    LAG(SUBSTR(r.DATE_, 1, 4), 2) OVER (PARTITION BY d.ID ORDER BY SUBSTR(r.DATE_, 1, 4)) AS 前两年
  FROM HQ_RS_TEACH_RES r
  JOIN HQ_CODE_DEPT d ON r.DEPT_ID = d.ID
  WHERE d.LEVEL_TYPE = 'YX'  -- 二级学院筛选
    AND r.DATE_ IS NOT NULL
)
SELECT DISTINCT 学院名称
FROM ranked_data
WHERE TO_NUMBER(年份) - TO_NUMBER(前一年) = 1
  AND TO_NUMBER(前一年) - TO_NUMBER(前两年) = 1
```

**场景2：连续三年各民族学生人数超过100的民族**

```sql
-- ❌ 错误：只统计各年人数>100，未判断连续性
SELECT s.NATION_CODE, COUNT(*) AS 学生人数
FROM HQ_XS_STU_YEAR s
GROUP BY s.NATION_CODE, s."YEAR_"
HAVING COUNT(*) > 100

-- ✅ 正确：使用LAG判断连续性
WITH nation_yearly AS (
  SELECT
    s.NATION_CODE AS 民族代码,
    s."YEAR_" AS 年份,
    COUNT(*) AS 学生人数,
    LAG(s."YEAR_", 1) OVER (PARTITION BY s.NATION_CODE ORDER BY s."YEAR_") AS 前一年,
    LAG(s."YEAR_", 2) OVER (PARTITION BY s.NATION_CODE ORDER BY s."YEAR_") AS 前两年
  FROM HQ_XS_STU_YEAR s
  GROUP BY s.NATION_CODE, s."YEAR_"
  HAVING COUNT(*) > 100
),
continuous_nations AS (
  SELECT 民族代码
  FROM nation_yearly
  WHERE TO_NUMBER(年份) - TO_NUMBER(前一年) = 1
    AND TO_NUMBER(前一年) - TO_NUMBER(前两年) = 1
)
SELECT DISTINCT 民族代码
FROM continuous_nations
```

**连续性判断的关键点**：
1. 使用 `LAG(field, n)` 获取前n个时间点的值
2. 使用 `PARTITION BY` 按分组字段分组
3. 使用 `ORDER BY` 按时间字段排序
4. 判断相邻时间点差值 = 1（年份连续）
5. 对于学期：需要判断学年+学期的组合

### ROWNUM 分页语法

⚠️ **聚合查询禁止使用 FETCH FIRST**

```sql
-- ❌ 错误：使用 FETCH FIRST（不支持）
SELECT m.NAME_, COUNT(*)
FROM HQ_CODE_MAJOR m
GROUP BY m.NAME_
ORDER BY COUNT(*) DESC
FETCH FIRST 5 ROWS ONLY

-- ✅ 正确：使用子查询 + ROWNUM
SELECT * FROM (
  SELECT m.NAME_, COUNT(*) AS cnt
  FROM HQ_CODE_MAJOR m
  GROUP BY m.NAME_
  ORDER BY COUNT(*) DESC
) WHERE ROWNUM <= 5
```

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
