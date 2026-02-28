# 单表查询示例 (C级)

生成时间: 2026-02-28 14:46:53

问题数量: 4

---

## 示例 1

**问题**: 1.0

**难度**: C

```sql
SELECT DISTINCT NAME_ AS 专业名称, CODE_ AS 代码 FROM HQ_CODE_MAJOR WHERE ISTRUE = 1;
```

---

## 示例 2

**问题**: 17.0

**难度**: C

```sql
SELECT DISTINCT jys.NAME_ AS 教学部名称, bm.NAME_ AS 部门名称 FROM HQ_CODE_DEPT_JYS jys LEFT JOIN HQ_CODE_DEPT_BM bm ON jys.DEPT_ID = bm.ID WHERE jys.NAME_ IN ('制药技术教育教学部', '数学教学部', '数控教育教学部', '机电教育教学部') AND jys.ISTRUE = 1;
```

---

## 示例 3

**问题**: 21.0

**难度**: C

```sql
SELECT DISTINCT t2.NAME_ AS 教师姓名, t2.TEA_NO AS 工号, t4.NAME_ AS 部门 FROM HQ_RS_TEA t1 LEFT JOIN HQ_CODE_DEPT_JYS_CY t3 ON t1.TEA_NO = t3.TEA_NO LEFT JOIN HQ_CODE_DEPT_JYS t5 ON t3.JYS_ID = t5.ID LEFT JOIN HQ_CODE_DEPT_JYS_CY t6 ON t5.ID = t6.JYS_ID LEFT JOIN HQ_RS_TEA t2 ON t6.TEA_NO = t2.TEA_NO LEFT JOIN HQ_CODE_DEPT_BM t4 ON t2.DEPT_ID = t4.ID WHERE t1.NAME_ = '闫静静' AND t3.ISTRUE = 1 AND t6.ISTRUE = 1;
```

---

## 示例 4

**问题**: 25.0

**难度**: C

```sql
SELECT DISTINCT m.NAME_ AS 专业名称 FROM HQ_CODE_CLASSES c LEFT JOIN HQ_CODE_MAJOR m ON c.MAJOR_CODE = m.CODE_ WHERE c.NAME_ = '夏季高考2019学前教育P05班';
```

---

