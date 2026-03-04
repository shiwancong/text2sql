# 常见问题修复指南

本文档记录 Text2SQL 测试中的常见错误及修复方法。

---

## 表选择问题（极重要！）

### 问题 0: 盲目添加不必要的表关联

**错误现象**：题目只需要返回少量字段，却关联了大量不必要的表

**错误代码**：
```sql
-- 题目：1号教学楼211室2024-05-17的上课班级、课程、节次、教师
-- ❌ 错误：使用了错误的表 + 盲目关联
FROM HQ_JX_KCB k  -- 错误的表选择
JOIN HQ_JX_JXZ_DAY d ON k.WEEKS LIKE '%' || d.WEEK || '%'  -- 不需要的复杂关联
JOIN HQ_JX_TEACHCLASS tc ON k.TEACHCLASS_ID = tc.ID
JOIN HQ_JX_TEACHCLASS_XZB xzb ON tc.ID = xzb.TEACHCLASS_ID  -- 不需要！题目没要求行政班
JOIN HQ_CODE_CLASSES cls ON xzb.CLASS_ID = cls.ID  -- 不需要！
```

**修复方法**：
1. 先用 `describe_table` 查看主表包含哪些字段
2. 主表已有的字段不要重复关联获取
3. 只关联题目明确要求返回的字段对应的表

```sql
-- ✅ 正确：使用 HQ_JX_KCB_PERIOD（有具体日期）
-- ✅ 只关联获取课程名称和教师姓名
SELECT
    kp.TEACHCLASS_NAME AS 班级名称,  -- 主表已有
    c.NAME_ AS 课程名称,              -- 需要关联 HQ_CODE_COURSE
    kp.PERIOD AS 节次,                -- 主表已有
    t.NAME_ AS 教师姓名               -- 需要关联教师表
FROM HQ_JX_KCB_PERIOD kp
LEFT JOIN HQ_CODE_COURSE c ON kp.COURSE_CODE = c.CODE_
LEFT JOIN HQ_JX_KCB_PERIOD_TEA kpt ON kp.ID = kpt.KCB_PERIOD_ID
LEFT JOIN HQ_RS_TEA t ON kpt.TEA_NO = t.TEA_NO
WHERE kp.DATE_ = '2024-05-17'
  AND js.NAME_ = '1号教学楼211室'
  AND kp.ISTRUE = 1
```

**课程表选择规则**：
| 表名 | 用途 | 关键字段 | 使用场景 |
|------|------|----------|----------|
| **HQ_JX_KCB_PERIOD** | 每天每节具体课 | DATE_(具体日期) | ✅ 题目有具体日期 |
| HQ_JX_KCB | 排课模板（周次） | WEEKS(如"1-5,10-15") | 题目只有周次，无具体日期 |

**关联原则**：
- 主表已有的字段 → 不需要关联
- 题目要求的字段 → 按需关联
- 题目没要求的 → 不关联

---

## Oracle 语法兼容性问题

### 问题 1: FETCH FIRST 语法不支持

**错误现象**：SQL 使用 `FETCH FIRST ... ROWS ONLY` 语法，在旧版本 Oracle 中报错

**错误代码**：
```sql
SELECT * FROM HQ_RS_TEA
WHERE IS_NORMAL = 1
FETCH FIRST 5 ROWS ONLY;
```

**修复方法**：使用 ROWNUM 代替
```sql
SELECT * FROM HQ_RS_TEA
WHERE IS_NORMAL = 1 AND ROWNUM <= 5;
```

**涉及题目**：
- A级题目3: `FETCH FIRST 1 ROW WITH TIES` → `WHERE ROWNUM = 1`
- A级题目7: `FETCH FIRST 5 ROWS ONLY` → `WHERE ROWNUM <= 5`
- A级题目8: `FETCH FIRST 1 ROW ONLY` → `WHERE ROWNUM = 1`
- A级题目12: `FETCH FIRST 5 ROWS ONLY` → `WHERE ROWNUM <= 5`

---

## 表别名不一致问题

### 问题 2: 表别名定义与使用不一致

**错误现象**：定义了表别名 `tEA` 但使用时写成了 `t`

**错误代码（B级题目5）**：
```sql
SELECT m.NAME_
FROM HQ_CODE_MAJOR m
JOIN HQ_RS_TEA tEA ON m.FZR_NO = t.TEA_NO  -- 定义了 tEA，但引用 t
WHERE t.IS_NORMAL = 1;
```

**修复方法**：统一使用相同的别名
```sql
SELECT m.NAME_
FROM HQ_CODE_MAJOR m
JOIN HQ_RS_TEA t ON m.FZR_NO = t.TEA_NO  -- 统一使用 t
WHERE t.IS_NORMAL = 1;
```

---

## 周次匹配问题

### 问题 3: WEEKS 字段使用等号精确匹配

**错误现象**：WEEKS 字段存储的是范围字符串（如 "1-5,10-15"），不能使用等号精确匹配

**错误代码（A级题目4）**：
```sql
SELECT k.TEACHCLASS_NAME, k.COURSE_CODE
FROM HQ_JX_KCB k
WHERE k.WEEKS = (SELECT WEEK FROM HQ_JX_JXZ_DAY WHERE DATE_ = '2024-05-17')
```

**修复方法 1**：使用 LIKE 模糊匹配
```sql
SELECT k.TEACHCLASS_NAME, k.COURSE_CODE
FROM HQ_JX_KCB k
WHERE k.WEEKS LIKE '%' || (SELECT WEEK FROM HQ_JX_JXZ_DAY WHERE DATE_ = '2024-05-17') || '%'
```

**修复方法 2（推荐）**：使用 JOIN HQ_JX_JXZ_DAY 表
```sql
SELECT k.TEACHCLASS_NAME, k.COURSE_CODE, t.NAME_
FROM HQ_JX_KCB k
JOIN HQ_JC_JS_ZZJG r ON k.CLASSROOM_ID = r.ID
JOIN HQ_JX_JXZ_DAY d ON k.WEEKS LIKE '%' || d.WEEK || '%'
LEFT JOIN HQ_JX_KCB_TEA kt ON k.ID = kt.KCB_ID AND kt.ISTRUE = 1
LEFT JOIN HQ_RS_TEA t ON kt.TEA_NO = t.TEA_NO
WHERE r.NAME_ = '1号教学楼211室'
  AND d.DATE_ = '2024-05-17'
  AND k.DAY_OF_WEEK = d.DAY_OF_WEEK
  AND k.ISTRUE = 1
```

---

## 教学班关联问题

### 问题 4: 遗漏 HQ_JX_TEACHCLASS_XZB 表关联

**错误现象**：查询行政班课程时，未关联 HQ_JX_TEACHCLASS_XZB 表，导致遗漏课程

**错误代码（A级题目5）**：
```sql
SELECT c.NAME_
FROM HQ_JX_TEACHCLASS tc
JOIN HQ_CODE_COURSE c ON tc.COURSE_CODE = c.CODE_
JOIN HQ_CODE_CLASSES cls ON tc.NAME_ LIKE '%' || cls.NAME_ || '%'
WHERE cls.NAME_ LIKE '%2022大数据P02%'
  AND tc.SCHOOL_YEAR = '2023-2024'
  AND tc.TERM_CODE = '02'
```

**问题**：未使用 HQ_JX_TEACHCLASS_XZB 表关联教学班和行政班

**修复方法**：
```sql
SELECT DISTINCT c.NAME_
FROM HQ_JX_TEACHCLASS tc
JOIN HQ_CODE_COURSE c ON tc.COURSE_CODE = c.CODE_
JOIN HQ_JX_TEACHCLASS_XZB xzb ON tc.ID = xzb.TEACHCLASS_ID AND xzb.ISTRUE = 1
JOIN HQ_CODE_CLASSES cls ON xzb.CLASS_ID = cls.ID AND cls.ISTRUE = 1
WHERE cls.NAME_ LIKE '%2022%大数据%P02%'
  AND tc.SCHOOL_YEAR = '2023-2024'
  AND tc.TERM_CODE = '02'
  AND tc.ISTRUE = 1
```

**关键点**：
1. 必须使用 HQ_JX_TEACHCLASS_XZB 表关联教学班和行政班
2. 所有表都要添加 ISTRUE = 1 条件

---

## 字段名错误问题

### 问题 5: HQ_RS_TEACH_RES 表字段名错误

**错误现象（B级题目7）**：
- 使用 `r.NAME_` → 应为 `r.JX_NAME`
- 使用 `cy.RES_ID` → 应为 `cy.TEACH_RES_ID`
- 使用 `cy.CY_TYPE` → 应为 `cy.PERSON_TYPE_CODE`

**错误代码**：
```sql
SELECT r.NAME_, t.DATE_
FROM HQ_RS_TEACH_RES t
LEFT JOIN HQ_RS_TEACH_RES_CY cy ON cy.RES_ID = t.ID
WHERE cy.CY_TYPE > '3'
```

**修复方法**：
```sql
SELECT t.ID, t.JX_NAME, t.DATE_
FROM HQ_RS_TEACH_RES t
WHERE SUBSTR(t.DATE_, 1, 4) = '2024'
  AND NOT EXISTS (
    SELECT 1 FROM HQ_RS_TEACH_RES_CY cy
    WHERE cy.TEACH_RES_ID = t.ID
      AND (cy.PERSON_TYPE_CODE > '3' OR PERSON_TYPE_CODE IS NULL)
  )
```

---

## 表选择错误问题

### 问题 6: 学校荣誉查询使用了错误的表

**错误现象（B级题目8）**：查询"学校获得的荣誉"使用了 `HQ_RS_HONOR_RES`（个人荣誉表）

**错误代码**：
```sql
SELECT TITLE, DETAILS, YEAR_MONTH
FROM HQ_RS_HONOR_RES
WHERE HONOR_RES_ID = '1' AND RANKING = 1
```

**修复方法**：使用正确的学校荣誉表 `HQ_JC_XX_RY`
```sql
SELECT TITLE, DETAILS, YEAR_MONTH
FROM HQ_JC_XX_RY
WHERE XXRY_GRADE_CODE = '1'  -- 国家级
  AND IS_TASK_THE_HEAD = 1  -- 牵头单位
ORDER BY YEAR_MONTH DESC
```

---

## 学年格式问题

### 问题 7: 学年格式理解错误

**错误现象（A级题目16）**：学年格式为 "2023-2024"，不是 "2023"

**错误代码**：
```sql
SELECT COUNT(*) FROM HQ_JX_KCB
WHERE SCHOOL_YEAR = '2023'
```

**修复方法 1**：通过 HQ_CODE_XNXQ 表匹配自然年范围
```sql
SELECT COUNT(DISTINCT k.COURSE_CODE)
FROM HQ_JX_KCB k
WHERE k.SCHOOL_YEAR IN (
  SELECT DISTINCT SCHOOL_YEAR
  FROM HQ_CODE_XNXQ
  WHERE TO_NUMBER(SUBSTR(BEGIN_DATE, 1, 4)) <= 2023
    AND TO_NUMBER(SUBSTR(END_DATE, 1, 4)) >= 2023
)
AND k.ISTRUE = 1
```

**修复方法 2**：明确指定两个学期
```sql
SELECT COUNT(DISTINCT k.COURSE_CODE)
FROM HQ_JX_KCB k
WHERE (k.SCHOOL_YEAR = '2022-2023' AND k.TERM_CODE = '02')
   OR (k.SCHOOL_YEAR = '2023-2024' AND k.TERM_CODE = '01')
AND k.ISTRUE = 1
```

**修复方法 3**：从 HQ_JX_MAJOR_COURSE 表查询（使用 YEAR_ 字段）
```sql
SELECT COUNT(DISTINCT COURSE_CODE)
FROM HQ_JX_MAJOR_COURSE
WHERE YEAR_ = 2023
```

---

## 学籍状态查询问题

### 问题 8: 退学学生查询多余关联 HQ_XS_CHANGE

**错误现象**：查询退学学生时，关联了 `HQ_XS_CHANGE` 表（多余）

**错误代码**：
```sql
-- ❌ 多余地关联了 HQ_XS_CHANGE 表
SELECT s.STU_NO, s.NAME_, c.DATE_
FROM HQ_XS_STU s
LEFT JOIN HQ_XS_CHANGE c ON s.STU_NO = c.STU_NO AND c.STU_CHANGE_CODE = '31'
WHERE s.ENROLL_GRADE = '2024'
  AND s.STU_STATE_CODE = '03'
```

**问题**：`s.STU_STATE_CODE = '03'` 已经表示学生是退学状态，不需要再关联异动表

**修复方法**：直接使用 `HQ_XS_STU` 表
```sql
-- ✅ 简化写法
SELECT s.STU_NO, s.NAME_
FROM HQ_XS_STU s
WHERE s.ENROLL_GRADE = '2024'
  AND s.STU_STATE_CODE = '03'
```

**关键点**：
1. `HQ_XS_STU.STU_STATE_CODE` 直接记录学生的当前状态
2. 不需要关联 `HQ_XS_CHANGE` 表来验证异动类型
3. 只在需要异动详细信息（如退学日期）时才关联

---

## 排序字段错误问题

### 问题 9: 男女比例分布排序错误

**错误现象（A级题目12）**：题目要求"男女学生比例分布 top5"，应按比例排序而非按总人数

**错误代码**：
```sql
SELECT cls.NAME_,
       SUM(CASE WHEN s.SEX_CODE = '1' THEN 1 ELSE 0 END) AS 男生数,
       SUM(CASE WHEN s.SEX_CODE = '2' THEN 1 ELSE 0 END) AS 女生数,
       COUNT(*) AS 总人数
FROM HQ_CODE_CLASSES cls
JOIN HQ_XS_STU s ON cls.ID = s.CLASS_ID
GROUP BY cls.NAME_
ORDER BY COUNT(*) DESC  -- ❌ 按总人数排序
FETCH FIRST 5 ROWS ONLY;
```

**修复方法**：按男生或女生比例排序
```sql
SELECT cls.NAME_,
       SUM(CASE WHEN s.SEX_CODE = '1' THEN 1 ELSE 0 END) AS 男生数,
       SUM(CASE WHEN s.SEX_CODE = '2' THEN 1 ELSE 0 END) AS 女生数,
       COUNT(*) AS 总人数,
       ROUND(SUM(CASE WHEN s.SEX_CODE = '1' THEN 1 ELSE 0 END) * 100.0 / COUNT(*), 2) AS 男生比例
FROM HQ_CODE_CLASSES cls
JOIN HQ_XS_STU s ON cls.ID = s.CLASS_ID
WHERE s.STU_STATE_CODE = '01' AND cls.ISTRUE = 1
GROUP BY cls.NAME_
ORDER BY 男生比例 DESC  -- ✅ 按男生比例排序
```

---

## 教师班级查询问题

### 问题 10: 教师教了哪些班需要使用 HQ_JX_TEACHCLASS_XZB

**场景**：查询"某教师教了哪些班"时，需要返回行政班名称

**错误代码**：
```sql
SELECT tc.NAME_ AS 班级名称
FROM HQ_JX_KCB k
JOIN HQ_JX_KCB_TEA kt ON k.ID = kt.KCB_ID
JOIN HQ_RS_TEA t ON kt.TEA_NO = t.TEA_NO
JOIN HQ_JX_TEACHCLASS tc ON k.TEACHCLASS_ID = tc.ID
WHERE t.NAME_ LIKE '%高雯萱%'
  AND k.SCHOOL_YEAR = '2023-2024'
  AND k.TERM_CODE = '02'
```

**问题**：返回的是教学班名称，而非行政班名称

**修复方法**：通过 HQ_JX_TEACHCLASS_XZB 获取行政班
```sql
SELECT cls.NAME_ AS 行政班名称
FROM HQ_JX_KCB k
JOIN HQ_JX_KCB_TEA kt ON k.ID = kt.KCB_ID AND kt.ISTRUE = 1
JOIN HQ_RS_TEA t ON kt.TEA_NO = t.TEA_NO
JOIN HQ_JX_TEACHCLASS tc ON k.TEACHCLASS_ID = tc.ID AND tc.ISTRUE = 1
JOIN HQ_JX_TEACHCLASS_XZB xzb ON tc.ID = xzb.TEACHCLASS_ID AND xzb.ISTRUE = 1
JOIN HQ_CODE_CLASSES cls ON xzb.CLASS_ID = cls.ID AND cls.ISTRUE = 1
WHERE t.NAME_ LIKE '%高雯萱%'
  AND k.SCHOOL_YEAR = '2023-2024'
  AND k.TERM_CODE = '02'
  AND k.ISTRUE = 1
```

**关联路径**：
```
HQ_JX_KCB → HQ_JX_KCB_TEA → HQ_RS_TEA (教师)
                ↓
         HQ_JX_TEACHCLASS → HQ_JX_TEACHCLASS_XZB → HQ_CODE_CLASSES (行政班)
```

---

## 快速检查清单

生成 SQL 前，必须检查：

- [ ] 是否使用了 `FETCH FIRST`？→ 改用 `ROWNUM`
- [ ] 表别名是否一致？
- [ ] WEEKS 字段是否使用了 `=`？→ 改用 `LIKE` 或 JOIN
- [ ] 查询行政班是否使用了 `HQ_JX_TEACHCLASS_XZB`？
- [ ] 学年格式是否正确（`YYYY-YYYY`）？
- [ ] 是否使用了正确的表名（如 `HQ_JC_XX_RY` 而非 `HQ_RS_HONOR_RES`）？
- [ ] 所有 JOIN 的表是否都添加了 `ISTRUE = 1`？
- [ ] 学生查询是否使用了 `ENROLL_GRADE` 而非 `ENROLL_YEAR`？
- [ ] 退学学生查询是否返回详细信息而非仅数量？

---

## 数据源分类参考

根据 homework 项目的数据源分类，表按以下 7 个分类组织：

| 分类 | 表数量 | 典型关键词 | 核心表 |
|------|--------|------------|--------|
| 基础代码表 | 16 | 院系、专业、班级、课程、学期 | HQ_CODE_DEPT, HQ_CODE_MAJOR, HQ_CODE_CLASSES, HQ_CODE_COURSE, HQ_CODE_XNXQ |
| 基础数据 | 5 | 学校、校区、教室、节假日 | HQ_JC_XX, HQ_JC_JS_ZZJG, HQ_JC_HOLIDAY |
| 教务数据 | 18 | 教学班、课程表、排课、评教 | HQ_JX_TEACHCLASS, HQ_JX_KCB, HQ_JX_PJ_PJ, HQ_JX_TEACHCLASS_XZB |
| 学生数据 | 10 | 学生、学籍、综合测评 | HQ_XS_STU, HQ_XS_CHANGE, HQ_XS_STU_YEAR |
| 教职工数据 | 22 | 教师、双师型、荣誉、成果 | HQ_RS_TEA, HQ_RS_HONOR, HQ_RS_TEACH_RES, HQ_JC_XX_RY |
| 外部数据 | 1 | 专业备案 | HQ_OUT_MAJOR_RECORDS |
| 国标数据 | 1 | 国标专业目录 | HQ_GB_MAJOR_CATALOGUE |

**选择表时参考**：
1. 先确定问题涉及的分类
2. 查找该分类下的核心表
3. 检查表之间的关联关系
4. 确认所有表都添加了必要的条件（ISTRUE、IS_NORMAL等）
