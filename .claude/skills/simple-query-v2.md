---
name: simple-query-v2
description: 处理Text2SQL查询（优化版）- 基于homework数据源分类
---

# Text2SQL Query Skill (优化版)

## 数据源分类概览

数据库共69张表，按7个分类组织：

| 分类 | 表数量 | 业务范围 | 典型关键词 | 核心表 |
|------|--------|----------|------------|--------|
| **基础代码表** | 16 | 院系、专业、班级、课程、学期、代码字典 | 院系、专业、班级、课程、学期 | HQ_CODE_DEPT, HQ_CODE_MAJOR, HQ_CODE_CLASSES, HQ_CODE_COURSE, HQ_CODE_XNXQ, HQ_CODE |
| **基础数据** | 5 | 学校信息、校区、教室、节假日 | 学校、校区、教室、教学楼 | HQ_JC_XX, HQ_JC_JS_ZZJG, HQ_JC_HOLIDAY |
| **教务数据** | 18 | 教学班、课程表、上课安排、评教 | 教学班、课程表、上课、排课、评教 | HQ_JX_TEACHCLASS, HQ_JX_KCB, HQ_JX_PJ_PJ, **HQ_JX_TEACHCLASS_XZB**, HQ_JX_JXZ_DAY |
| **学生数据** | 10 | 学生信息、学籍、综合测评 | 学生、学籍、转专业、退学 | **HQ_XS_STU**, HQ_XS_CHANGE, HQ_XS_STU_YEAR |
| **教职工数据** | 22 | 教职工信息、荣誉、教学成果 | 教师、教职工、双师型、荣誉 | **HQ_RS_TEA**, HQ_RS_TEACH_RES, **HQ_JC_XX_RY** |
| **外部数据** | 1 | 专业备案 | 专业备案 | HQ_OUT_MAJOR_RECORDS |
| **国标数据** | 1 | 国标专业目录 | 国标、专业目录 | HQ_GB_MAJOR_CATALOGUE |

## 能力范围

处理涉及单表或多表的查询，包括：
- 查询单个表的全部或部分数据
- 简单的 WHERE 条件筛选
- 基础的 ORDER BY 排序
- ROWNUM 结果数量限制
- 多表关联查询

## 核心规则（必须遵守）

### 0. 表选择原则（极重要！）

**原则：根据实际需求选择表，不盲目添加关联**

| 错误做法 | 正确做法 |
|----------|----------|
| 看到相关表就全部关联 | 只关联题目要求的字段 |
| 假设需要更多信息 | 按题目要求返回字段 |
| 过度设计关联 | 主表已包含大部分信息 |

**课程表选择：HQ_JX_KCB vs HQ_JX_KCB_PERIOD**

| 表名 | 用途 | 关键字段 | 使用场景 |
|------|------|----------|----------|
| **HQ_JX_KCB_PERIOD** | 每天每节具体课 | DATE_(具体日期)、TEACHCLASS_NAME | ✅ 题目有具体日期（如"2024-05-17"） |
| HQ_JX_KCB | 排课模板（周次） | WEEKS(如"1-5,10-15") | 题目只有周次或星期，无具体日期 |

**示例对比**：

```sql
-- ✅ 正确：题目"1号教学楼211室2024-05-17的上课..."
-- 使用 HQ_JX_KCB_PERIOD（有 DATE_ 字段）
SELECT kp.TEACHCLASS_NAME, c.NAME_, kp.PERIOD, t.NAME_
FROM HQ_JX_KCB_PERIOD kp
LEFT JOIN HQ_CODE_COURSE c ON kp.COURSE_CODE = c.CODE_
LEFT JOIN HQ_JX_KCB_PERIOD_TEA kpt ON kp.ID = kpt.KCB_PERIOD_ID
LEFT JOIN HQ_RS_TEA t ON kpt.TEA_NO = t.TEA_NO
WHERE kp.DATE_ = '2024-05-17'
  AND kp.CLASSROOM_ID = 'XXX'

-- ❌ 错误：盲目关联 HQ_JX_TEACHCLASS_XZB（题目没要求行政班）
JOIN HQ_JX_TEACHCLASS_XZB xzb ON ...  -- 不需要！
JOIN HQ_CODE_CLASSES cls ON ...       -- 不需要！

-- ❌ 错误：使用 HQ_JX_KCB + HQ_JX_JXZ_DAY（表选择错误）
FROM HQ_JX_KCB k
JOIN HQ_JX_JXZ_DAY d ON k.WEEKS LIKE '%' || d.WEEK || '%'  -- 复杂且不需要
```

**关联原则**：
1. 先用 `describe_table` 查看主表包含哪些字段
2. 主表已有的字段不要重复关联获取
3. 只关联题目明确要求返回的字段对应的表
4. 不假设用户需要更多信息

### 1. Oracle 语法规范（极重要）

**禁用 FETCH FIRST**：Oracle 旧版本不支持 `FETCH FIRST ... ROWS ONLY`，必须使用 `ROWNUM`

| 场景 | ❌ 错误写法 | ✅ 正确写法 |
|------|------------|------------|
| 限制1条 | `FETCH FIRST 1 ROW ONLY` | `WHERE ROWNUM = 1` |
| 限制N条 | `FETCH FIRST N ROWS ONLY` | `WHERE ROWNUM <= N` |
| 排序后取1条 | `ORDER BY ... FETCH FIRST 1 ROW` | 子查询排序 + 外层 `ROWNUM = 1` |

### 2. 表别名一致性

表别名一旦定义，整个SQL必须保持一致：

```sql
-- ❌ 错误
JOIN HQ_RS_TEA tEA ON ... WHERE t.NAME_ = ...

-- ✅ 正确
JOIN HQ_RS_TEA t ON ... WHERE t.NAME_ = ...
```

### 3. ISTRUE 字段（必须条件）

大多数表都有 `ISTRUE` 字段，**查询时必须添加**：

```sql
WHERE 表别名.ISTRUE = 1
```

**JOIN 时每个表都需要添加 ISTRUE 条件**：
```sql
FROM HQ_JX_KCB k
INNER JOIN HQ_JX_KCB_TEA kt ON kt.KCB_ID = k.ID AND kt.ISTRUE = 1  -- ✅ 别忘了
INNER JOIN HQ_JX_TEACHCLASS_XZB xzb ON xzb.TEACHCLASS_ID = tc.ID AND xzb.ISTRUE = 1  -- ✅ 别忘了
WHERE k.ISTRUE = 1
```

### 4. WEEKS 字段模糊匹配

`HQ_JX_KCB.WEEKS` 存储范围字符串（如 "1-5,10-15"），**不能用等号精确匹配**：

```sql
-- ❌ 错误
WHERE k.WEEKS = (SELECT WEEK FROM HQ_JX_JXZ_DAY WHERE DATE_ = '2024-05-17')

-- ✅ 正确：使用 LIKE
WHERE k.WEEKS LIKE '%' || (SELECT WEEK FROM HQ_JX_JXZ_DAY WHERE DATE_ = '2024-05-17') || '%'

-- ✅ 或使用 JOIN 方式
JOIN HQ_JX_JXZ_DAY d ON k.WEEKS LIKE '%' || d.WEEK || '%'
```

### 5. 教学班与行政班关联（谨慎使用）

**关键表**：`HQ_JX_TEACHCLASS_XZB`（教学班与行政班关联表）

⚠️ **仅在题目明确要求行政班信息时才关联此表**

| 题目要求 | 是否需要关联 |
|----------|-------------|
| "上课班级" | ❌ 不需要（HQ_JX_KCB_PERIOD 已有 TEACHCLASS_NAME） |
| "行政班" | ✅ 需要关联 |
| "教了哪些班" | ⚠️ 看上下文，通常指行政班 |

**示例对比**：

```sql
-- ✅ 题目："某天某教室的上课班级、课程、教师"
-- HQ_JX_KCB_PERIOD.TEACHCLASS_NAME 已包含班级信息，不需要额外关联
SELECT kp.TEACHCLASS_NAME, c.NAME_, t.NAME_
FROM HQ_JX_KCB_PERIOD kp
LEFT JOIN HQ_CODE_COURSE c ON kp.COURSE_CODE = c.CODE_
LEFT JOIN HQ_JX_KCB_PERIOD_TEA kpt ON kp.ID = kpt.KCB_PERIOD_ID
LEFT JOIN HQ_RS_TEA t ON kpt.TEA_NO = t.TEA_NO
WHERE kp.DATE_ = '2024-05-17'

-- ✅ 题目："某教师教了哪些行政班"
-- 需要返回行政班名称，必须关联
SELECT cls.NAME_
FROM HQ_JX_KCB k
JOIN HQ_JX_KCB_TEA kt ON k.ID = kt.KCB_ID AND kt.ISTRUE = 1
JOIN HQ_RS_TEA t ON kt.TEA_NO = t.TEA_NO
JOIN HQ_JX_TEACHCLASS tc ON k.TEACHCLASS_ID = tc.ID AND tc.ISTRUE = 1
JOIN HQ_JX_TEACHCLASS_XZB xzb ON tc.ID = xzb.TEACHCLASS_ID AND xzb.ISTRUE = 1
JOIN HQ_CODE_CLASSES cls ON xzb.CLASS_ID = cls.ID AND cls.ISTRUE = 1
WHERE t.NAME_ LIKE '%教师名%'
```

### 6. 学年格式

学年格式为 "YYYY-YYYY"（如 "2023-2024"），不是单独年份：

```sql
-- ❌ 错误
WHERE SCHOOL_YEAR = '2023'

-- ✅ 正确
WHERE SCHOOL_YEAR = '2023-2024'
```

### 7. 学生字段选择

- **ENROLL_GRADE**（入学年级）：用于查询"2024级学生"
- **ENROLL_YEAR**（入学年份）：不是用来查询年级的
- **STU_STATE_CODE**（学籍状态）：'01'=在读，'03'=退学

**重要：查询退学学生不需要关联 HQ_XS_CHANGE 表**

```sql
-- ✅ 查询2024级退学学生（正确，不需要关联）
SELECT s.STU_NO, s.NAME_
FROM HQ_XS_STU s
WHERE s.ENROLL_GRADE = '2024' AND s.STU_STATE_CODE = '03'

-- ❌ 错误1：使用 ENROLL_YEAR
WHERE ENROLL_YEAR = '2024'

-- ❌ 错误2：多余地关联 HQ_XS_CHANGE 表
FROM HQ_XS_STU s
LEFT JOIN HQ_XS_CHANGE c ON s.STU_NO = c.STU_NO AND c.STU_CHANGE_CODE = '31'  -- 多余！
WHERE s.STU_STATE_CODE = '03'  -- 已经是退学状态，不需要关联异动表
```

**原则**：`HQ_XS_STU.STU_STATE_CODE` 已经记录学生的当前状态，不需要关联 `HQ_XS_CHANGE` 表

### 8. 荣誉表选择

| 查询场景 | 正确表 | 错误表 |
|----------|--------|--------|
| 学校获得的荣誉 | **HQ_JC_XX_RY** | HQ_RS_HONOR_RES |
| 个人/集体荣誉 | HQ_RS_HONOR_RES | - |

### 9. 名称查询两步法

涉及名称查询（专业、班级、课程、院系等）必须分两步：

**第一步**：查询代码表获取精确ID（可用LIKE）
```sql
SELECT ID FROM HQ_CODE_CLASSES WHERE NAME_ LIKE '%2022%大数据%P02%' AND ISTRUE = 1
```

**第二步**：使用精确ID进行主查询（禁用LIKE）
```sql
WHERE cls.ID = 'CLASS123'  -- 精确匹配
```

---

## 准确率提升策略

```
用户问题 → RAG检索 → 表名验证 → 字段验证 → SQL生成 → 结果验证
```

### 2. 查询理解增强

| 用户表达 | 识别意图 | 映射规则 |
|----------|----------|----------|
| "我校" | 学校信息 | HQ_JC_XX |
| "性质类别" | 学校属性 | XX_XZLB_CODE, XX_BXLX_CODE |
| "网址" | 域名 | DOMAIN |
| "籍贯" | 教师籍贯 | PLACE |
| "双师型" | 教师类型 | IS_SSJS |
| "培养层次" | 学生层次 | PYCC_CODE |
| "归属/隶属于" | 上级部门 | PID 关联查询 |

### 3. 表名映射优化

| 业务概念 | 优先表名 | 备选表名 |
|----------|----------|----------|
| 学校信息 | HQ_JC_XX | - |
| 教师信息 | HQ_RS_TEA | - |
| 部门/组织 | HQ_CODE_DEPT | HQ_CODE_DEPT_JYS |
| 教研室 | HQ_CODE_DEPT_JYS | - |
| 专业 | HQ_CODE_MAJOR | - |
| 班级 | HQ_CODE_CLASSES | - |
| 课程 | HQ_CODE_COURSE | HQ_JX_KCB |
| 授课教师 | HQ_JX_KCB_TEA | HQ_JX_TEACHCLASS_TEA |

## SQL 生成与自检流程（极重要！）

### 第一步：需求分析

```
1. 识别要返回的字段（只选题目要求的）
2. 识别筛选条件（时间、地点、状态等）
3. 识别查询类型（单值/列表/统计/排序）
```

### 第二步：表选择

```
1. 根据需求选择主表（用 describe_table 查看字段）
2. 检查主表是否已包含需要的字段
3. 只关联题目要求返回的字段对应的表
```

### 第三步：SQL 编写

使用 WITH 子句处理复杂统计：
```sql
WITH 统计子查询 AS (
    -- 先统计，不关联名称表
    SELECT 分组字段, COUNT(*), SUM(...)
    FROM 主表
    WHERE 条件
    GROUP BY 分组字段
)
SELECT d.NAME_, s.*
FROM 统计子查询 s
JOIN 名称表 d ON s.关联字段 = d.ID
WHERE d.ISTRUE = 1
ORDER BY 排序字段
```

### 第四步：SQL 自检（必须执行！）

在执行前，检查以下问题：

| 检查项 | 问题 | 示例 |
|--------|------|------|
| 多余的 HAVING | 从主表 GROUP BY 时不需要 HAVING COUNT(*) > 0 | ❌ GROUP BY ... HAVING COUNT(*) > 0 |
| 多余的关联 | 主表已有字段不需要重复关联 | ❌ 关联 HQ_CODE_CLASSES 获取班级（主表已有） |
| 错误的表 | 有具体日期用 HQ_JX_KCB_PERIOD，不用 HQ_JX_KCB | ❌ FROM HQ_JX_KCB WHERE ... DATE_ = ... |
| FETCH FIRST | 旧版 Oracle 不支持，改用 ROWNUM | ❌ FETCH FIRST 3 ROWS ONLY |
| 表别名不一致 | 定义后必须一致使用 | ❌ JOIN ... tEA WHERE ... t.NAME_ |
| ISTRUE 条件 | 多数表需要添加，JOIN 的表也要加 | ❌ JOIN ... ON kt.ID = k.ID（缺少 kt.ISTRUE=1） |
| IS_NORMAL vs STU_STATE_CODE | 教师用 IS_NORMAL，学生用 STU_STATE_CODE | ❌ 学生 WHERE IS_NORMAL = 1 |

### 第五步：执行验证

```
1. 先执行 SQL 检查是否有错误
2. 检查结果数量是否合理
3. 检查结果内容是否符合预期
```

### 常见错误模式

| 错误类型 | 错误示例 | 正确示例 |
|----------|----------|----------|
| 多余的 HAVING | `GROUP BY d.ID HAVING COUNT(*) > 0` | `GROUP BY d.ID`（删除 HAVING） |
| 过早关联 | 直接 JOIN 名称表后统计 | 用 WITH 先统计，再关联名称表 |
| 盲目关联 | 题目要求班级、课程、教师，却关联了行政班表 | 只关联题目要求的表 |
| 表选择错误 | 有日期用 HQ_JX_KCB | 用 HQ_JX_KCB_PERIOD |

---

## SQL 优化实例对比

### 实例 1：统计查询优化

**题目：双师型教师比例 top3 的院系**

| 方面 | ❌ 错误/次优写法 | ✅ 优化写法 |
|------|----------------|------------|
| 结构 | 直接 JOIN 后统计 | WITH 子句先统计，再关联 |
| HAVING | `HAVING COUNT(*) > 0`（多余） | 删除 |
| 可读性 | 统计和关联混在一起 | 逻辑分层清晰 |

**对比**：
```sql
-- ❌ 次优写法
SELECT * FROM (
    SELECT d.NAME_, COUNT(*), SUM(...) / COUNT(*)
    FROM HQ_RS_TEA t
    JOIN HQ_CODE_DEPT d ON t.DEPT_ID = d.ID AND d.ISTRUE = 1
    WHERE t.IS_NORMAL = 1
    GROUP BY d.ID, d.NAME_
    HAVING COUNT(*) > 0  -- 多余！
    ORDER BY ... DESC
) WHERE ROWNUM <= 3

-- ✅ 优化写法
SELECT * FROM (
    WITH dept_tea_stats AS (
      SELECT t.DEPT_ID, COUNT(*) AS total, SUM(...) AS ssjs,
             ROUND(SUM(...) * 100.0 / COUNT(*), 2) AS ratio
      FROM HQ_RS_TEA t
      WHERE t.IS_NORMAL = 1
      GROUP BY t.DEPT_ID
    )
    SELECT d.NAME_, s.total, s.ssjs, s.ratio
    FROM dept_tea_stats s
    JOIN HQ_CODE_DEPT d ON s.DEPT_ID = d.ID
    WHERE d.ISTRUE = 1
    ORDER BY s.ratio DESC
) WHERE ROWNUM <= 3
```

### 实例 2：具体日期查询优化

**题目：1号教学楼211室2024-05-17的上课班级、课程、节次、教师**

| 方面 | ❌ 错误写法 | ✅ 优化写法 |
|------|------------|------------|
| 表选择 | HQ_JX_KCB（周次模板） | HQ_JX_KCB_PERIOD（具体日期） |
| 关联 | 盲目关联 HQ_JX_TEACHCLASS_XZB | 只关联题目要求的表 |
| 复杂度 | 需要 JOIN HQ_JX_JXZ_DAY | 直接用 DATE_ = '2024-05-17' |

```sql
-- ❌ 错误写法
SELECT cls.NAME_, c.NAME_, k.PERIOD, t.NAME_
FROM HQ_JX_KCB k
JOIN HQ_JX_JXZ_DAY d ON k.WEEKS LIKE '%' || d.WEEK || '%'
JOIN HQ_JX_TEACHCLASS tc ON k.TEACHCLASS_ID = tc.ID
JOIN HQ_JX_TEACHCLASS_XZB xzb ON tc.ID = xzb.TEACHCLASS_ID  -- 不需要！
JOIN HQ_CODE_CLASSES cls ON xzb.CLASS_ID = cls.ID           -- 不需要！
WHERE d.DATE_ = '2024-05-17'

-- ✅ 优化写法
SELECT kp.TEACHCLASS_NAME, c.NAME_, kp.PERIOD, t.NAME_
FROM HQ_JX_KCB_PERIOD kp
JOIN HQ_JC_JS_ZZJG js ON kp.CLASSROOM_ID = js.ID
JOIN HQ_CODE_COURSE c ON kp.COURSE_CODE = c.CODE_
JOIN HQ_JX_KCB_PERIOD_TEA kpt ON kp.ID = kpt.KCB_PERIOD_ID
JOIN HQ_RS_TEA t ON kpt.TEA_NO = t.TEA_NO
WHERE kp.DATE_ = '2024-05-17' AND js.NAME_ = '1号教学楼211室'
```

---

## 常见查询模式

### 模式1：单值查询
```
问题：我校的网址是什么？
SQL: SELECT DOMAIN FROM HQ_JC_XX WHERE ROWNUM = 1
```

### 模式2：属性查询
```
问题：学校的性质类别？
SQL: SELECT XX_XZLB_CODE FROM HQ_JC_XX WHERE ROWNUM = 1
```

### 模式3：列表查询
```
问题：学校设置了哪些行政单位？
SQL: SELECT NAME_ FROM HQ_CODE_DEPT WHERE ISTRUE = 1 ORDER BY NAME_
```

### 模式4：人员属性查询
```
问题：某教师的籍贯/职称/双师型？
SQL: SELECT PLACE, ZW_NAME, IS_SSJS FROM HQ_RS_TEA WHERE NAME_ LIKE '%xxx%'
```

### 模式5：关联查询（通过代码表）
```
问题：培养层次名称？
SQL: SELECT CODE.NAME_ FROM HQ_CODE_CLASSES c
     JOIN HQ_CODE CODE ON c.PYCC_CODE = CODE.CODE_
     WHERE c.ID = 'xxx'
```

## 字段名推断规则

### 当不确定字段名时：

1. **尝试关键词匹配**
   - 含"名称" → NAME_
   - 含"代码" → CODE_
   - 含"类型" → TYPE_CODE 或 XXX_CODE
   - 含"标识" → ID 或 NO_

2. **查看表结构**
   - 使用 describe_table 查看所有字段
   - 优先选择有注释的字段

3. **参考命名规范**
   - XXX_CODE: 外键或代码
   - XXX_ID: 主键或外键ID
   - NAME_: 名称
   - ISTRUE: 是否有效（1是/0否）

## 错误处理

| 错误类型 | 处理方式 |
|----------|----------|
| 表不存在 | 检查表名拼写，使用模糊搜索 |
| 字段不存在 | 使用 describe_table 确认字段名 |
| 结果为空 | 检查筛选条件，使用 LIKE 扩大范围 |
| 多表关联 | 降级为单表查询，分步获取数据 |
| SQL 语法错误 | 检查字段名、引号、关键字 |

## 优化要点

### 1. 精确匹配优先
```
有精确匹配的表名 → 使用精确匹配
无精确匹配 → 使用 RAG 检索 → 使用模糊查询
```

### 2. 代码表处理
```
查询代码字段 → 同时关联 HQ_CODE 表获取名称
GROUP_TYPE 用于区分不同类型的代码
```

### 3. 层级结构处理
```
部门/专业/班级的层级关系：
- PID: 上级ID
- 通过自关联获取完整层级路径
```

### 4. 布尔值处理
```
ISTRUE, IS_NORMAL, IS_SSJS 等：
- 1: 是/有效/双师型
- 0: 否/无效/非双师型
- 转换为中文显示
```

## 示例参考库

### 学校信息类
| 问题 | 表 | 字段 |
|------|-----|------|
| 学校网址 | HQ_JC_XX | DOMAIN |
| 学校名称 | HQ_JC_XX | NAME_ |
| 学校性质 | HQ_JC_XX | XX_XZLB_CODE |
| 学校地址 | HQ_JC_XX | ADDRESS |

### 教师信息类
| 问题 | 表 | 字段 |
|------|-----|------|
| 教师籍贯 | HQ_RS_TEA | PLACE |
| 教师职称 | HQ_RS_TEA | ZW_NAME |
| 是否双师型 | HQ_RS_TEA | IS_SSJS |
| 教师电话 | HQ_RS_TEA | PHONE |

### 组织机构类
| 问题 | 表 | 字段 |
|------|-----|------|
| 部门列表 | HQ_CODE_DEPT | NAME_ |
| 部门归属 | HQ_CODE_DEPT | PID |
| 教研室 | HQ_CODE_DEPT_JYS | NAME_ |

### 专业班级类
| 问题 | 表 | 字段 |
|------|-----|------|
| 培养层次 | HQ_CODE_CLASSES | PYCC_CODE |
| 专业名称 | HQ_CODE_MAJOR | NAME_ |
| 班级名称 | HQ_CODE_CLASSES | NAME_ |
