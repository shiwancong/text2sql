# 关键字段必查表

生成SQL前，必须检查以下关键字段，确保查询条件完整。

## Oracle 语法规范（极重要！）

### ROWNUM vs FETCH FIRST（高频错误）

⚠️ **极重要**：Oracle 旧版本不支持 `FETCH FIRST ... ROWS ONLY` 语法，必须使用 `ROWNUM`

| 场景 | ❌ 错误写法 | ✅ 正确写法 |
|------|------------|------------|
| 限制1条记录 | `FETCH FIRST 1 ROW ONLY` | `WHERE ROWNUM = 1` |
| 限制N条记录 | `FETCH FIRST N ROWS ONLY` | `WHERE ROWNUM <= N` |
| 获取第一条 | `FETCH FIRST 1 ROW WITH TIES` | `WHERE ROWNUM = 1` |

**完整示例对比**：
```sql
-- ❌ 错误：旧版本Oracle不支持
SELECT * FROM HQ_RS_TEA
WHERE IS_NORMAL = 1
FETCH FIRST 5 ROWS ONLY;

-- ✅ 正确：使用ROWNUM
SELECT * FROM HQ_RS_TEA
WHERE IS_NORMAL = 1 AND ROWNUM <= 5;

-- ❌ 错误
SELECT * FROM HQ_CODE_DEPT
ORDER BY NAME_
FETCH FIRST 1 ROW ONLY;

-- ✅ 正确
SELECT * FROM (
    SELECT * FROM HQ_CODE_DEPT
    ORDER BY NAME_
) WHERE ROWNUM = 1;
```

**注意事项**：
1. `ROWNUM` 必须在 `WHERE` 子句中使用
2. `ROWNUM` 在 `ORDER BY` **之前**赋值，所以需要子查询排序后再外层过滤
3. 如果需要排序后取第一条，必须使用子查询

### 表别名一致性（常见错误）

⚠️ **重要**：表别名一旦定义，在整个SQL中必须保持一致

| 错误类型 | 示例 | 说明 |
|----------|------|------|
| 别名不一致 | `JOIN HQ_RS_TEA tEA` 但使用 `t.TEA_NO` | 定义了`tEA`却使用`t` |
| 别名拼写错误 | 定义 `t` 但写成 `te` | 拼写必须完全一致 |
| 未定义别名 | 直接使用 `t.NAME_` | 必须先在FROM/JOIN中定义 |

**错误示例（来自B级题目5）**：
```sql
-- ❌ 错误：表别名不一致
SELECT m.NAME_
FROM HQ_CODE_MAJOR m
JOIN HQ_RS_TEA tEA ON m.FZR_NO = t.TEA_NO  -- 定义了 tEA
WHERE t.IS_NORMAL = 1;  -- 这里使用了 t（应该是 tEA）
```

**正确写法**：
```sql
-- ✅ 正确：统一使用 t
SELECT m.NAME_
FROM HQ_CODE_MAJOR m
JOIN HQ_RS_TEA t ON m.FZR_NO = t.TEA_NO  -- 定义 t
WHERE t.IS_NORMAL = 1;  -- 使用 t

-- ✅ 或统一使用 tEA
SELECT m.NAME_
FROM HQ_CODE_MAJOR m
JOIN HQ_RS_TEA tEA ON m.FZR_NO = tEA.TEA_NO  -- 定义 tEA
WHERE tEA.IS_NORMAL = 1;  -- 使用 tEA
```

**表别名命名建议**：
- 教师表：`t` 或 `tea`
- 学生表：`s` 或 `stu`
- 班级表：`cls` 或 `c`
- 专业表：`m` 或 `major`
- 院系表：`d` 或 `dept`
- 课程表：`crs` 或 `course`
- 课程表：`k` 或 `kcb`
- 教学班：`tc` 或 `teachclass`

---

## 使用说明

当用户提出查询问题时，按以下步骤操作：

1. **确定涉及的表**
2. **查阅本表，检查关键字段**
3. **根据问题含义，确定需要哪些条件**
4. **生成SQL时包含必要条件**

---

## 通用关键字段

### ISTRUE（有效性标识）

| 表名 | 是否有ISTRUE | 用户问题含义 | 是否需要条件 |
|------|-------------|-------------|-------------|
| HQ_CODE_MAJOR | ✅ | "专业有几个" | **必须** `WHERE ISTRUE = 1` |
| HQ_CODE_COURSE | ✅ | "课程有哪些" | **必须** `WHERE ISTRUE = 1` |
| HQ_CODE_DEPT | ✅ | "部门有哪些" | **必须** `WHERE ISTRUE = 1` |
| HQ_CODE_DEPT_JYS | ✅ | "教研室有哪些" | **必须** `WHERE ISTRUE = 1` |
| HQ_CODE_CLASSES | ✅ | "班级有哪些" | **必须** `WHERE ISTRUE = 1` |
| HQ_CODE_MAJOR_MAPPER | ✅ | 国标映射查询 | **必须** `WHERE ISTRUE = 1` |

**ISTRUE字段含义**：
- `1` = 有效/启用/当前使用
- `0` = 无效/停用/已废弃

**原则**：除非用户明确要求查询所有历史数据（包括已停用），否则都必须加 `ISTRUE = 1`

---

## 学生相关关键字段

### STU_STATE_CODE（学籍状态）

| 字段值 | 含义 | 用户问题含义 |
|--------|------|-------------|
| 01 | 在校 | "学生有几个" → **必须** `WHERE STU_STATE_CODE = '01'` |
| 02 | 休学 | "休学学生有几个" → `WHERE STU_STATE_CODE = '02'` |
| 03 | 退学 | "退学学生有几个" → `WHERE STU_STATE_CODE = '03'` |
| 其他 | 毕业、离校等 | 根据具体问题确定 |

**示例**：
```sql
-- 查询在校学生
WHERE STU_STATE_CODE = '01'

-- 查询休学学生
WHERE STU_STATE_CODE = '02'

-- 查询退学学生
WHERE STU_STATE_CODE = '03'
```

### ENROLL_GRADE vs ENROLL_YEAR（🔥 极重要！）

⚠️ **核心概念**：HQ_XS_STU 表有两个相似字段，用途不同

| 字段名 | 含义 | 格式 | 使用场景 |
|--------|------|------|---------|
| ENROLL_GRADE | 入学年级 | "2024" | ✅ 正确：用于查询"2024级学生" |
| ENROLL_YEAR | 入学年份 | "2024" | ❌ 错误：不是用来查询年级的 |

**错误案例**：
```sql
-- ❌ 错误：使用 ENROLL_YEAR 查询年级
WHERE ENROLL_YEAR = '2024'

-- ✅ 正确：使用 ENROLL_GRADE 查询年级
WHERE ENROLL_GRADE = '2024'
```

**典型场景**：
```sql
-- 场景1：查询2024级退学学生
SELECT COUNT(*)
FROM HQ_XS_STU
WHERE ENROLL_GRADE = '2024'  -- 使用 ENROLL_GRADE
  AND STU_STATE_CODE = '03'  -- 退学状态

-- 场景2：查询2024级有没有退学的学生（返回详细信息）
SELECT s.STU_NO, s.NAME_, s.DEPT_ID, s.MAJOR_CODE, s.CLASS_ID, c.DATE_
FROM HQ_XS_STU s
LEFT JOIN HQ_XS_CHANGE c ON s.STU_NO = c.STU_NO AND c.STU_CHANGE_CODE = '31'
WHERE s.ENROLL_GRADE = '2024'
  AND s.STU_STATE_CODE = '03'
```

---

## 课表相关关键字段

### WEEKS（周次范围字段）

⚠️ **极重要**：查询具体日期的课程时，应优先使用 HQ_JX_KCB_PERIOD 表

**表选择决策（题目20错误案例）**：
| 表名 | 字段特点 | 使用场景 |
|------|---------|---------|
| **HQ_JX_KCB_PERIOD** | 有 DATE_ 字段（具体日期） | ✅ 题目有具体日期 |
| HQ_JX_KCB | 有 WEEKS 字段（周次范围字符串） | 题目只有周次，无具体日期 |

**错误案例（题目20）**：
```sql
-- ❌ 错误：使用 HQ_JX_KCB 表 + WEEKS 字段等号比较
SELECT k.TEACHCLASS_NAME, k.COURSE_CODE, k.PERIOD, t.NAME_
FROM HQ_JX_KCB k
WHERE k.WEEKS = (SELECT WEEK FROM HQ_JX_JXZ_DAY WHERE DATE_ = '2024-05-17')
-- 问题1：WEEKS 是字符串（如"1-18"），不能直接用等号比较
-- 问题2：会导致 ORA-01722 无效数字错误
```

**正确做法**：
```sql
-- ✅ 推荐：使用 HQ_JX_KCB_PERIOD 表（有具体日期字段）
SELECT
    kp.TEACHCLASS_NAME AS 班级名称,
    c.NAME_ AS 课程名称,
    kp.PERIOD AS 节次,
    t.NAME_ AS 教师姓名
FROM HQ_JX_KCB_PERIOD kp
LEFT JOIN HQ_CODE_COURSE c ON kp.COURSE_CODE = c.CODE_
LEFT JOIN HQ_JX_KCB_PERIOD_TEA kpt ON kp.ID = kpt.KCB_PERIOD_ID
LEFT JOIN HQ_RS_TEA t ON kpt.TEA_NO = t.TEA_NO
LEFT JOIN HQ_JC_JS_ZZJG js ON kp.CLASSROOM_ID = js.ID
WHERE kp.DATE_ = '2024-05-17'
  AND js.NAME_ = '1号教学楼211室'
  AND kp.ISTRUE = 1

-- ✅ 备选方案：如果必须用 HQ_JX_KCB 表，使用 LIKE 模糊匹配
WHERE k.WEEKS LIKE '%' || (SELECT WEEK FROM HQ_JX_JXZ_DAY WHERE DATE_ = '2024-05-17') || '%'
```

**查询规则**：

| 用户问题 | 优先表名 | 备选方案 |
|---------|---------|---------|
| "某日期某教室的课" | HQ_JX_KCB_PERIOD | HQ_JX_KCB + LIKE |
| "某周有哪些课" | HQ_JX_KCB | LIKE '%周次%' |
| "某日课表" | HQ_JX_KCB_PERIOD | - |

**WEEKS 字段格式说明**：
- `"1-5"` → 第1到5周
- `"1-5,10-15"` → 第1到5周和第10到15周
- `"1,3,5,7,9"` → 第1、3、5、7、9周

**规则**：
1. 有具体日期时，优先使用 HQ_JX_KCB_PERIOD 表
2. 使用 HQ_JX_KCB 表的 WEEKS 字段时，必须用 LIKE 模糊匹配
3. 禁止对 WEEKS 字段使用等号精确匹配

---

## 教师相关关键字段

### 教师状态字段

HQ_RS_TEA表没有ISTRUE字段，但可以通过其他字段判断：

| 字段 | 含义 | 使用场景 |
|------|------|---------|
| ZW_NAME | 职称 | 查询有职称的教师：`WHERE ZW_NAME IS NOT NULL` |
| 其他状态字段 | 根据实际情况 | 查看 describe_table 确认 |

### NATION_CODE NULL值处理（🔥 极重要！）

⚠️ **核心概念**：NATION_CODE 字段可能为 NULL，表示未填报民族信息

**错误示例（题目6）**：
```sql
-- ❌ 错误：NULL值被统计为少数民族
SELECT
    COUNT(CASE WHEN t.NATION_CODE != '01' THEN 1 END) AS 少数民族人数,
    COUNT(*) AS 总人数
FROM HQ_RS_TEA t
WHERE t.IS_NORMAL = 1

-- 问题：NATION_CODE = NULL 的记录被 != '01' 条件匹配，错误计入少数民族
```

**正确做法**：
```sql
-- ✅ 正确：显式处理NULL值
SELECT
    COUNT(CASE WHEN t.NATION_CODE IS NOT NULL AND t.NATION_CODE != '01' THEN 1 END) AS 少数民族人数,
    COUNT(*) AS 总人数
FROM HQ_RS_TEA t
WHERE t.IS_NORMAL = 1
```

**规则**：
1. 涉及 NATION_CODE 的条件判断时，必须先检查 `IS NOT NULL`
2. `NATION_CODE = '01'` 表示汉族
3. `NATION_CODE IS NULL` 表示未填报，不应算作少数民族
4. 正确的少数民族判断：`NATION_CODE IS NOT NULL AND NATION_CODE != '01'`

---

## 班级相关关键字段

### 班级名称规范化处理（🔥 极重要！）

⚠️ **核心概念**：用户输入的班级名称可能是简写，需要先查询数据库获取准确名称

**错误案例（题目5）**：
```sql
-- ❌ 错误：直接使用用户简写进行模糊匹配
WHERE k.TEACHCLASS_NAME LIKE '%2022大数据P02班%'

-- 问题：数据库中实际班级名是"2022大数据技术P02班"，用户说"2022大数据P02班"
-- 导致查询不到结果
```

**正确做法**：
```sql
-- ✅ 方式1：先查询准确班级名称，再使用子查询
SELECT DISTINCT c.NAME_ AS 课程名称
FROM HQ_JX_TEACHCLASS tc
JOIN HQ_CODE_COURSE c ON tc.COURSE_CODE = c.CODE_
JOIN HQ_JX_TEACHCLASS_XZB xzb ON tc.ID = xzb.TEACHCLASS_ID AND xzb.ISTRUE = 1
JOIN HQ_CODE_CLASSES cls ON xzb.CLASS_ID = cls.ID AND cls.ISTRUE = 1
WHERE cls.ID IN (
    SELECT ID FROM HQ_CODE_CLASSES
    WHERE NAME_ LIKE '%2022%大数据%P02%'  -- 使用更宽松的匹配
    AND ISTRUE = 1
)
AND tc.SCHOOL_YEAR = '2023-2024'
AND tc.TERM_CODE = '02'
AND tc.ISTRUE = 1

-- ✅ 方式2：使用多个关键词组合匹配
WHERE cls.NAME_ LIKE '%2022%'
AND (cls.NAME_ LIKE '%大数据%' OR cls.NAME_ LIKE '%大数据技术%')
AND cls.NAME_ LIKE '%P02%'
```

**规则**：
1. 用户输入的班级名可能是简写（如"大数据"→"大数据技术"）
2. 优先使用子查询先获取准确的班级ID
3. 使用关键词拆分组合匹配：`LIKE '%2022%' AND LIKE '%大数据%' AND LIKE '%P02%'`
4. 避免使用单一简写词进行精确匹配

**常见班级名称简写对照**：
| 用户输入 | 可能的完整名称 |
|---------|---------------|
| 大数据 | 大数据技术、大数据与财务管理 |
| 财务 | 财务管理、大数据与财务管理 |
| 会计 | 会计、会计信息管理 |
| P02班 | P02班、P02（可能无"班"字） |

---

## 课程相关关键字段

### IS_CORE（核心课程标识）

| 字段值 | 含义 | 用户问题 |
|--------|------|---------|
| 1 | 是核心课程 | "核心课有哪些" → `WHERE IS_CORE = 1` |
| 0 或 NULL | 非核心课程 | - |

---

## 时间相关关键字段

### 学年格式（SCHOOL_YEAR vs YEAR_）

⚠️ **极重要**：数据库中学年格式为"YYYY-YYYY"，不是单独的年份

| 字段名 | 表名 | 格式 | 说明 |
|--------|------|------|------|
| SCHOOL_YEAR | HQ_JX_KCB, HQ_JX_JXZ, HQ_CODE_XNXQ | "2023-2024" | 学年格式（跨年） |
| YEAR_ | HQ_JX_MAJOR_COURSE | 2023 | 自然年格式（单年） |

**用户问题 "2023年开设课程多少门" 的处理**：

```sql
-- ❌ 错误：学年格式错误
WHERE SCHOOL_YEAR = '2023'  -- 不存在这样的学年

-- ✅ 正确方式1：通过 HQ_CODE_XNXQ 表匹配自然年范围
WHERE SCHOOL_YEAR IN (
  SELECT DISTINCT SCHOOL_YEAR
  FROM HQ_CODE_XNXQ
  WHERE TO_NUMBER(SUBSTR(BEGIN_DATE, 1, 4)) <= 2023
    AND TO_NUMBER(SUBSTR(END_DATE, 1, 4)) >= 2023
)

-- ✅ 正确方式2：明确指定两个学期
WHERE (SCHOOL_YEAR = '2022-2023' AND TERM_CODE = '02')
   OR (SCHOOL_YEAR = '2023-2024' AND TERM_CODE = '01')

-- ✅ 正确方式3：从 HQ_JX_MAJOR_COURSE 表查询（使用 YEAR_ 字段）
WHERE YEAR_ = 2023
```

---

## 常见查询场景的条件模板

### 场景1：统计数量

```sql
-- 专业数量（仅有效）
SELECT COUNT(*) FROM HQ_CODE_MAJOR WHERE ISTRUE = 1

-- 在校学生数量
SELECT COUNT(*) FROM HQ_XS_STU WHERE STU_STATE_CODE = '01'

-- 有效课程数量
SELECT COUNT(*) FROM HQ_CODE_COURSE WHERE ISTRUE = 1
```

### 场景2：列表查询

```sql
-- 专业列表（仅有效）
SELECT NAME_ FROM HQ_CODE_MAJOR WHERE ISTRUE = 1 ORDER BY NAME_

-- 部门列表（仅有效）
SELECT NAME_ FROM HQ_CODE_DEPT WHERE ISTRUE = 1 ORDER BY NAME_
```

### 场景3：关联查询

```sql
-- 专业与国标映射（两个表都要检查ISTRUE）
SELECT m.NAME_, mp.GB_MAJOR_NAME
FROM HQ_CODE_MAJOR m
LEFT JOIN HQ_CODE_MAJOR_MAPPER mp ON m.CODE_ = mp.MAJOR_CODE AND mp.ISTRUE = 1
WHERE m.ISTRUE = 1
```

---

## 检查清单

生成SQL前，必须确认：

- [ ] 主表是否需要 `ISTRUE = 1`？
- [ ] 子查询/关联表是否需要 `ISTRUE = 1`？
- [ ] 学生表是否需要 `STU_STATE_CODE = '01'`？
- [ ] 是否有其他状态字段需要过滤？
- [ ] 用户问题是否隐含了特定状态？
- [ ] 查询结果是否符合业务常识？

---

## 错误案例对比

### 案例1：专业数量查询

| SQL | 结果 | 评价 |
|-----|------|------|
| `SELECT COUNT(*) FROM HQ_CODE_MAJOR` | 499 | ❌ 错误，包含已停用专业 |
| `SELECT COUNT(*) FROM HQ_CODE_MAJOR WHERE ISTRUE = 1` | 正确值 | ✅ 正确 |

### 案例2：仅有校标代码的专业

| SQL | 结果 | 评价 |
|-----|------|------|
| 没有ISTRUE条件 | 146 | ❌ 错误 |
| 有ISTRUE条件 | 19 | ✅ 正确 |

---

## 更新日志

- 2026-02-28：创建文档，基于ISTRUE问题的反思
