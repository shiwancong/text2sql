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

### 按需关联表原则（极重要！）

⚠️ **核心原则**：只关联用户问题明确需要的表，避免关联无用表导致数据重复

```
┌─────────────────────────────────────────────────────────────┐
│              数据重复问题的常见原因                           │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│   问题1：关联了课程表，但课程有多名教师导致重复         │
│   ├─ SELECT ... JOIN HQ_CODE_COURSE ... JOIN HQ_JX_KCB_TEA     │
│   ├─ 一门课程可能关联多个教师，每个教师产生一条记录    │
│   └─ 结果：3条记录变成了15条（5个教师×3门课）           │
│                                                             │
│   问题2：关联了教室表，但教室可能被多次使用             │
│   ├─ SELECT ... JOIN HQ_JC_JS_ZZJG ...                     │
│   ├─ 同一教室在不同时间被不同课程使用，导致重复           │
│   └─ 结果：实际3条记录，显示20+条（每个时间段一条）       │
│                                                             │
│   解决方案：按需关联，只关联用户明确要求的字段           │
└─────────────────────────────────────────────────────────────┘
```

**按需关联判断表：**

| 用户问题需求 | 需要关联的表 | 不需要关联的表 | 理由 |
|-------------|-----------|--------------|------|
| "教师的排课信息" | HQ_JX_KCB + HQ_JX_KCB_TEA + HQ_RS_TEA | 课程表、教室表 | 用户没要求课程名称和教室 |
| "上了哪些课程" | HQ_JX_KCB + HQ_CODE_COURSE | 教室表、教师表 | 用户没要求教室和教师 |
| "在哪些教室上课" | HQ_JX_KCB + HQ_JC_JS_ZZJG | 课程表、教师表 | 用户没要求课程和教师 |
| "课程在哪个教室" | HQ_JX_KCB + HQ_JC_JS_ZZJG | 教师表 | 用户没要求教师信息 |

**数据重复检查清单：**

```
生成SQL前问自己：
├─ 这个表是否是用户问题要求的？
├─ 关联这个表会产生数据重复吗？
├─ 用户明确要求显示这个字段吗？
├─ 这个字段对回答问题有必要吗？
└─ 能不能通过去掉JOIN来简化查询？
```

**典型错误示例：**

```sql
-- ❌ 错误：关联了课程表和教室表，导致82条结果（实际应该3条）
SELECT
  k.TEACHCLASS_NAME AS 班级,
  cr.NAME_ AS 课程,    ← 不需要！
  r.NAME_ AS 教室,    ← 不需要！
  t.NAME_ AS 教师
FROM HQ_JX_KCB k
JOIN HQ_JX_KCB_TEA kt ON k.ID = kt.KCB_ID
JOIN HQ_RS_TEA t ON kt.TEA_NO = t.TEA_NO
JOIN HQ_CODE_COURSE cr ON k.COURSE_CODE = cr.CODE_  ← 导致重复！
LEFT JOIN HQ_JC_JS_ZZJG r ON k.CLASSROOM_ID = r.ID  ← 导致重复！
WHERE ...

-- ✅ 正确：只关联必要的表，结果3条
SELECT
  k.TEACHCLASS_NAME AS 班级,
  k.COURSE_CODE AS 课程代码,
  k.PERIOD AS 节次,
  k.DAY_OF_WEEK AS 星期,
  t.NAME_ AS 教师
FROM HQ_JX_KCB k
JOIN HQ_JX_KCB_TEA kt ON k.ID = kt.KCB_ID
JOIN HQ_RS_TEA t ON kt.TEA_NO = t.TEA_NO
WHERE t.NAME_ = '战会玲'
  AND k.SCHOOL_YEAR = '2020-2021'
  AND k.TERM_CODE = '01'
```

**关联表的优先级：**

```
优先级1（必需）：
├─ 主表（如HQ_JX_KCB课表）
└─ 直接关联的表（如HQ_JX_KCB_TEA授课教师表）

优先级2（按需）：
├─ 如果用户要求"课程名称" → 关联HQ_CODE_COURSE
├─ 如果用户要求"教室" → 关联HQ_JC_JS_ZZJG
└─ 如果用户要求"教师信息" → 关联HQ_RS_TEA

优先级3（避免）：
└─ 如果用户没明确要求 → 不关联，直接显示代码字段
```

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

### IS_NORMAL 在职状态检查（必须）

⚠️ **极重要**：多表联查教师/教职工时，必须检查 IS_NORMAL 字段

```
❌ 错误：没有检查IS_NORMAL
SELECT t.NAME_ AS 教师姓名, d.NAME_ AS 部门名称
FROM HQ_RS_TEA t
JOIN HQ_CODE_DEPT d ON t.DEPT_ID = d.ID
WHERE d.NAME_ LIKE '%护理%'

✅ 正确：添加IS_NORMAL条件
SELECT t.NAME_ AS 教师姓名, d.NAME_ AS 部门名称
FROM HQ_RS_TEA t
JOIN HQ_CODE_DEPT d ON t.DEPT_ID = d.ID
WHERE d.NAME_ LIKE '%护理%'
  AND t.IS_NORMAL = 1  -- 只查询在职教师
  AND d.ISTRUE = 1     -- 只查询有效部门
```

### 班级表关联字段判断（重要）

⚠️ **重要**：班级表 HQ_CODE_CLASSES 有 ID 和 NO_ 两个字段

```
场景1：学生表关联班级（使用 NO_）
JOIN HQ_CODE_CLASSES c ON s.CLASS_ID = c.NO_

场景2：教学班行政班关联（需确认）
-- 先使用 describe_table HQ_JX_TEACHCLASS_XZB 确认
-- 如果 CLASS_ID 存储的是班级编码，使用 NO_
-- 如果 CLASS_ID 存储的是班级内部ID，使用 ID

判断原则：
- CLASS_ID 通常存储班级编码，关联 c.NO_
- 使用 describe_table 确认字段类型和注释
- 当不确定时，可以尝试两种关联方式
```

### 表名选择准确性

⚠️ **极重要**：根据查询对象选择正确的表

| 查询对象 | 正确表名 | 错误表名 |
|---------|---------|---------|
| 荣誉成果 | HQ_RS_HONOR_RES | HQ_RS_TEACH_RES ❌ |
| 教学成果奖 | HQ_RS_TEACH_RES | HQ_RS_HONOR_RES ❌ |
| 学生信息 | HQ_XS_STU | HQ_RS_TEA ❌ |
| 教师信息 | HQ_RS_TEA | HQ_XS_STU ❌ |

```
❌ 错误：查询学生用了教师表
问题："闫亚君"的信息
SELECT * FROM HQ_RS_TEA WHERE NAME_ = '闫亚君'  -- 闫亚君是学生

✅ 正确：使用学生表
SELECT * FROM HQ_XS_STU WHERE NAME_ = '闫亚君'  -- 闫亚君是学生
```

## 班级类型区分规则（极重要！）

⚠️ **核心概念**：教学班 ≠ 行政班，查询排课时必须区分！

```
┌─────────────────────────────────────────────────────────────┐
│              多表关联时的班级类型选择                        │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│   场景A：查询排课/课表/上课信息                             │
│   ├── 班级类型：教学班                                      │
│   ├── 使用字段：HQ_JX_KCB.TEACHCLASS_NAME                  │
│   ├── 关联表：不需要关联 HQ_CODE_CLASSES                   │
│   └── 示例："某教室某日的上课班级"                         │
│                                                             │
│   场景B：查询班级学生信息/班级属性                          │
│   ├── 班级类型：行政班                                      │
│   ├── 使用字段：HQ_CODE_CLASSES.NAME_                      │
│   ├── 关联表：需要关联学生表                                │
│   └── 示例："某班有多少学生"                               │
│                                                             │
│   关键判断：用户问题中的"班级"指什么？                       │
│   ├── "上课班级"、"教的班"、"排课" → 教学班                │
│   └── "班级学生"、"班级人数" → 行政班                      │
└─────────────────────────────────────────────────────────────┘
```

**班级关联决策表：**

| 查询场景 | 班级类型 | 使用字段 | 是否关联CODE_CLASSES |
|---------|---------|---------|---------------------|
| 教室的课、某日的课 | 教学班 | `k.TEACHCLASS_NAME` | ❌ 不关联 |
| 教师教的班 | 教学班 | `k.TEACHCLASS_NAME` | ❌ 不关联 |
| 某班上了什么课 | 教学班 | `k.TEACHCLASS_NAME` | ❌ 不关联 |
| 某班有多少学生 | 行政班 | `c.NAME_` | ✅ 需要关联 |
| 某班属于哪个专业 | 行政班 | `c.NAME_` | ✅ 需要关联 |

**错误模式警示：**

```
❌ 危险模式：查询排课时关联了行政班表
FROM HQ_JX_KCB k
JOIN HQ_JX_TEACHCLASS_XZB tx ON k.TEACHCLASS_ID = tx.TEACHCLASS_ID
JOIN HQ_CODE_CLASSES c ON tx.CLASS_ID = c.NO_  ← 可能导致数据爆炸

问题：
- 如果1个教学班对应10个行政班
- 1条课表记录会变成10条结果
- 用户期望2条，实际返回20条

✅ 安全模式：直接使用课表中的教学班字段
FROM HQ_JX_KCB k
...直接使用 k.TEACHCLASS_NAME
不关联 HQ_CODE_CLASSES
```

---

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
