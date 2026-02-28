# 多表联查示例 (B级)

生成时间: 2026-02-28 14:46:53

问题数量: 325

---

## 示例 1

**问题**: 1000.0

**难度**: BC

```sql
SELECT DISTINCT NAME_ AS 专业名称, CODE_ AS 专业代码 FROM HQ_CODE_MAJOR WHERE ISTRUE = 1;
```

**答案**: 356个（状态1，含0的有442）

---

## 示例 2

**问题**: 1000.0

**难度**: BC

```sql
SELECT DISTINCT D.NAME_ AS 院系名称, M.NAME_ AS 专业名称, M.CODE_ AS 代码 FROM HQ_CODE_MAJOR M LEFT JOIN HQ_CODE_DEPT_YX D ON M.DEPT_ID = D.ID WHERE D.NAME_ = '材料与化学工程学院' AND M.ISTRUE = 1;
```

**答案**: 356个（状态1，含0的有442）

---

## 示例 3

**问题**: 1000.0

**难度**: BC

```sql
SELECT DISTINCT NAME_ AS 专业名称, CODE_ AS 专业代码 FROM HQ_CODE_MAJOR WHERE ISTRUE = 1;
```

**答案**: 356个（状态1，含0的有442）

---

## 示例 4

**问题**: 1000.0

**难度**: BC

```sql
SELECT DISTINCT NAME_ AS 专业名称, CODE_ AS 专业代码 FROM HQ_CODE_MAJOR WHERE ISTRUE = 1;
```

**答案**: 356个（状态1，含0的有442）

---

## 示例 5

**问题**: 1000.0

**难度**: BC

```sql
SELECT DISTINCT NAME_ AS 专业名称, CODE_ AS 代码 FROM HQ_CODE_MAJOR WHERE ISTRUE = 1;
```

**答案**: 356个（状态1，含0的有442）

---

## 示例 6

**问题**: 1000.0

**难度**: BC

```sql
SELECT DISTINCT NAME_ AS 专业名称, CODE_ AS 代码 FROM HQ_CODE_MAJOR WHERE ISTRUE = 1;
```

**答案**: 356个（状态1，含0的有442）

---

## 示例 7

**问题**: 1000.0

**难度**: BC

```sql
SELECT DISTINCT NAME_ AS 专业名称, CODE_ AS 代码 FROM HQ_CODE_MAJOR WHERE ISTRUE = 1;
```

**答案**: 356个（状态1，含0的有442）

---

## 示例 8

**问题**: 1000.0

**难度**: BC

```sql
SELECT DISTINCT NAME_ AS 专业名称, CODE_ AS 专业代码 FROM HQ_CODE_MAJOR;
```

**答案**: 356个（状态1，含0的有442）

---

## 示例 9

**问题**: 1000.0

**难度**: BC

```sql
SELECT DISTINCT NAME_ AS 专业名称, CODE_ AS 代码 FROM HQ_CODE_MAJOR WHERE ISTRUE = 1;
```

**答案**: 356个（状态1，含0的有442）

---

## 示例 10

**问题**: 1001.0

**难度**: BC

```sql
SELECT DISTINCT NAME_ AS 学院名称, CODE_ AS 院系代码 FROM HQ_CODE_DEPT_YX WHERE NAME_ = '材料与化学工程学院' AND ISTRUE = 1;
```

**答案**: 23个（状态1，含0的有24个）

---

## 示例 11

**问题**: 1001.0

**难度**: BC

```sql
SELECT DISTINCT NAME_ AS 学院名称, CODE_ AS 院系代码 FROM HQ_CODE_DEPT_YX WHERE ISTRUE = 1;
```

**答案**: 23个（状态1，含0的有24个）

---

## 示例 12

**问题**: 1001.0

**难度**: BC

```sql
SELECT DISTINCT NAME_ AS 学院名称, CODE_ AS 院系代码 FROM HQ_CODE_DEPT_YX WHERE ISTRUE = 1;
```

**答案**: 23个（状态1，含0的有24个）

---

## 示例 13

**问题**: 1001.0

**难度**: BC

```sql
SELECT DISTINCT NAME_ AS 学院名称, CODE_ AS 院系代码 FROM HQ_CODE_DEPT_YX WHERE ISTRUE = 1;
```

**答案**: 23个（状态1，含0的有24个）

---

## 示例 14

**问题**: 1001.0

**难度**: BC

```sql
SELECT DISTINCT NAME_ AS 学院名称, CODE_ AS 院系代码 FROM HQ_CODE_DEPT_YX WHERE ISTRUE = 1;
```

**答案**: 23个（状态1，含0的有24个）

---

## 示例 15

**问题**: 1001.0

**难度**: BC

```sql
SELECT DISTINCT NAME_ AS 学院名称, CODE_ AS 院系代码 FROM HQ_CODE_DEPT_YX WHERE ISTRUE = 1;
```

**答案**: 23个（状态1，含0的有24个）

---

## 示例 16

**问题**: 1001.0

**难度**: BC

```sql
SELECT DISTINCT NAME_ AS 学院名称, CODE_ AS 院系代码 FROM HQ_CODE_DEPT_YX WHERE ISTRUE = 1;
```

**答案**: 23个（状态1，含0的有24个）

---

## 示例 17

**问题**: 1001.0

**难度**: BC

```sql
SELECT DISTINCT NAME_ AS 学院名称, CODE_ AS 院系代码 FROM HQ_CODE_DEPT_YX WHERE ISTRUE = 1;
```

**答案**: 23个（状态1，含0的有24个）或提示只有系院

---

## 示例 18

**问题**: 1001.0

**难度**: BC

```sql
SELECT DISTINCT NAME_ AS 学院名称, CODE_ AS 院系代码 FROM HQ_CODE_DEPT_YX WHERE ISTRUE = 1;
```

**答案**: 未查询到结果（学校名称不对）或提示您可能想要查询的是淄博职业学院的系院，并正确列出系院

---

## 示例 19

**问题**: 1001.0

**难度**: BC

```sql
SELECT DISTINCT HQ_CODE_DEPT_YX.NAME_ AS 院系名称, HQ_CODE_MAJOR.NAME_ AS 专业名称, HQ_CODE_MAJOR.CODE_ AS 代码 FROM HQ_CODE_DEPT_YX LEFT JOIN HQ_CODE_MAJOR ON HQ_CODE_DEPT_YX.ID = HQ_CODE_MAJOR.DEPT_ID WHERE HQ_CODE_DEPT_YX.NAME_ = '材料与化学工程学院' AND HQ_CODE_MAJOR.ISTRUE = 1;
```

**答案**: 19个（状态1，含0的有22个）14

---

## 示例 20

**问题**: 1002.0

**难度**: BC

```sql
SELECT DISTINCT D.NAME_ AS 院系名称, M.NAME_ AS 专业名称, M.CODE_ AS 代码 FROM HQ_CODE_MAJOR M LEFT JOIN HQ_CODE_DEPT_YX D ON M.DEPT_ID = D.ID WHERE D.NAME_ = '材料与化学工程学院' AND M.ISTRUE = 1;
```

**答案**: 19个（状态1，含0的有22个） 14

---

## 示例 21

**问题**: 1002.0

**难度**: BC

```sql
SELECT DISTINCT D.NAME_ AS 院系名称, M.NAME_ AS 专业名称, M.CODE_ AS 代码 FROM HQ_CODE_MAJOR M LEFT JOIN HQ_CODE_DEPT_YX D ON M.DEPT_ID = D.ID WHERE D.NAME_ = '材料与化学工程学院' AND M.ISTRUE = 1;
```

**答案**: 18个（状态1，含0的有22个）

---

## 示例 22

**问题**: 1002.0

**难度**: BC

```sql
SELECT DISTINCT D.NAME_ AS 院系名称, M.NAME_ AS 专业名称, M.CODE_ AS 代码 FROM HQ_CODE_MAJOR M LEFT JOIN HQ_CODE_DEPT_YX D ON M.DEPT_ID = D.ID WHERE D.NAME_ = '材料与化学工程学院' AND M.ISTRUE = 1;
```

**答案**: 18个（状态1，含0的有22个）

---

## 示例 23

**问题**: 1002.0

**难度**: BC

```sql
SELECT DISTINCT D.NAME_ AS 院系名称, M.NAME_ AS 专业名称, M.CODE_ AS 代码 FROM HQ_CODE_DEPT_YX D LEFT JOIN HQ_CODE_MAJOR M ON D.ID = M.DEPT_ID WHERE D.NAME_ = '材料与化学工程学院' AND M.ISTRUE = 1;
```

**答案**: 18个（状态1，含0的有22个）

---

## 示例 24

**问题**: 1002.0

**难度**: BC

```sql
SELECT DISTINCT D.NAME_ AS 院系名称, M.NAME_ AS 专业名称, M.CODE_ AS 代码 FROM HQ_CODE_MAJOR M LEFT JOIN HQ_CODE_DEPT_YX D ON M.DEPT_ID = D.ID WHERE D.NAME_ = '材料与化学工程学院' AND M.ISTRUE = 1;
```

**答案**: 18个（状态1，含0的有22个）

---

## 示例 25

**问题**: 1002.0

**难度**: BC

```sql
SELECT DISTINCT NAME_ AS 教研室名称 FROM HQ_CODE_DEPT_JYS WHERE ISTRUE = 1;
```

**答案**: 52个（状态1，含0的有100个）

---

## 示例 26

**问题**: 1002.0

**难度**: BC

```sql
SELECT DISTINCT bm.NAME_ AS 院系名称, jys.NAME_ AS 教研室名称 FROM HQ_CODE_DEPT_BM bm LEFT JOIN HQ_CODE_DEPT_JYS jys ON bm.ID = jys.DEPT_ID WHERE bm.NAME_ = '材料与化学工程学院' AND bm.ISTRUE = 1 AND jys.ISTRUE = 1;
```

**答案**: 52个（状态1，含0的有100个）2

---

## 示例 27

**问题**: 1002.0

**难度**: BC

```sql
SELECT DISTINCT yx.NAME_ AS 院系名称, jys.NAME_ AS 教研室名称 FROM HQ_CODE_DEPT_YX yx LEFT JOIN HQ_CODE_DEPT_JYS jys ON yx.ID = jys.DEPT_ID WHERE yx.NAME_ = '材料与化学工程学院' AND yx.ISTRUE = 1 AND jys.ISTRUE = 1;
```

**答案**: 52个（状态1，含0的有100个）2

---

## 示例 28

**问题**: 1002.0

**难度**: BC

```sql
SELECT DISTINCT NAME_ AS 教研室名称 FROM HQ_CODE_DEPT_JYS WHERE ISTRUE = 1;
```

**答案**: 52个（状态1，含0的有100个）

---

## 示例 29

**问题**: 1002.0

**难度**: BC

```sql
SELECT DISTINCT NAME_ AS 教研室名称 FROM HQ_CODE_DEPT_JYS WHERE ISTRUE = 1;
```

**答案**: 52个（状态1，含0的有100个）

---

## 示例 30

**问题**: 1003.0

**难度**: BC

```sql
SELECT DISTINCT NAME_ AS 教研室名称 FROM HQ_CODE_DEPT_JYS WHERE ISTRUE = 1;
```

**答案**: 52个（状态1，含0的有100个）

---

## 示例 31

**问题**: 1003.0

**难度**: BC

```sql
SELECT DISTINCT NAME_ AS 教研室名称 FROM HQ_CODE_DEPT_JYS WHERE ISTRUE = 1;
```

**答案**: 52个（状态1，含0的有100个）

---

## 示例 32

**问题**: 1003.0

**难度**: BC

```sql
SELECT DISTINCT NAME_ AS 教研室名称 FROM HQ_CODE_DEPT_JYS WHERE ISTRUE = 1;
```

**答案**: 52个（状态1，含0的有100个）

---

## 示例 33

**问题**: 1003.0

**难度**: BC

```sql
SELECT DISTINCT NAME_ AS 教研室名称 FROM HQ_CODE_DEPT_JYS WHERE ISTRUE = 1;
```

**答案**: 52个（状态1，含0的有100个）

---

## 示例 34

**问题**: 1003.0

**难度**: BC

```sql
SELECT DISTINCT bm.NAME_ AS 院系名称, jys.NAME_ AS 教研室名称 FROM HQ_CODE_DEPT_JYS jys LEFT JOIN HQ_CODE_DEPT_BM bm ON jys.DEPT_ID = bm.ID WHERE bm.LEVEL_TYPE = 'YX' AND bm.NAME_ = '人工智能与大数据学院' AND jys.ISTRUE = 1;
```

**答案**: 5个（状态1，含0的有9个）

---

## 示例 35

**问题**: 1003.0

**难度**: BC

```sql
org.springframework.web.client.ResourceAccessException: I/O error on POST request for "http://192.168.1.216:3001/v1/chat/completions": Request was interrupted: null
```

**答案**: 5个（状态1，含0的有9个）

---

## 示例 36

**问题**: 1003.0

**难度**: BC

```sql
SELECT DISTINCT bm.NAME_ AS 院系名称, jys.NAME_ AS 教研室名称 FROM HQ_CODE_DEPT_JYS jys LEFT JOIN HQ_CODE_DEPT_BM bm ON jys.DEPT_ID = bm.ID WHERE bm.NAME_ = '人工智能与大数据学院' AND jys.ISTRUE = 1;
```

**答案**: 5个（状态1，含0的有9个）

---

## 示例 37

**问题**: 1003.0

**难度**: BC

```sql
SELECT DISTINCT bm.NAME_ AS 院系名称, jys.NAME_ AS 教研室名称 FROM HQ_CODE_DEPT_BM bm LEFT JOIN HQ_CODE_DEPT_JYS jys ON bm.ID = jys.DEPT_ID WHERE bm.LEVEL_TYPE = 'YX' AND bm.NAME_ = '人工智能与大数据学院' AND jys.ISTRUE = 1;
```

**答案**: 5个（状态1，含0的有9个）

---

## 示例 38

**问题**: 1003.0

**难度**: BC

```sql
SELECT DISTINCT bm.NAME_ AS 院系名称, jys.NAME_ AS 教研室名称 FROM HQ_CODE_DEPT_BM bm LEFT JOIN HQ_CODE_DEPT_JYS jys ON bm.ID = jys.DEPT_ID WHERE bm.NAME_ = '人工智能与大数据学院' AND bm.LEVEL_TYPE = 'YX' AND jys.ISTRUE = 1;
```

**答案**: 5个（状态1，含0的有9个）

---

## 示例 39

**问题**: 1004.0

**难度**: BC

```sql
SELECT DISTINCT jys.NAME_ AS 教研室名称 FROM HQ_CODE_DEPT_JYS jys LEFT JOIN HQ_CODE_DEPT_BM bm ON jys.DEPT_ID = bm.ID WHERE bm.NAME_ = '人工智能与大数据学院' AND jys.ISTRUE = 1;
```

**答案**: 5个（状态1，含0的有9个）

---

## 示例 40

**问题**: 1004.0

**难度**: BC

```sql
SELECT DISTINCT D.NAME_ AS 院系名称, J.NAME_ AS 教研室名称 FROM HQ_CODE_DEPT_BM D LEFT JOIN HQ_CODE_DEPT_JYS J ON D.ID = J.DEPT_ID WHERE D.NAME_ = '人工智能与大数据学院' AND D.ISTRUE = 1 AND J.ISTRUE = 1;
```

**答案**: 5个（状态1，含0的有9个）

---

## 示例 41

**问题**: 1004.0

**难度**: BC

```sql
SELECT DISTINCT D.NAME_ AS 院系名称, J.NAME_ AS 教研室名称, J.CODE_ AS 教研室代码 FROM HQ_CODE_DEPT_JYS J LEFT JOIN HQ_CODE_DEPT_BM D ON J.DEPT_ID = D.ID WHERE D.LEVEL_TYPE = 'YX' AND D.NAME_ = '人工智能与大数据学院';
```

**答案**: 5个（状态1，含0的有9个）

---

## 示例 42

**问题**: 1004.0

**难度**: BC

```sql
SELECT DISTINCT HQ_CODE_MAJOR.NAME_ AS 专业名称, HQ_CODE_MAJOR.CODE_ AS 代码 FROM HQ_CODE_MAJOR LEFT JOIN HQ_CODE_DEPT_YX ON HQ_CODE_MAJOR.DEPT_ID = HQ_CODE_DEPT_YX.ID WHERE HQ_CODE_DEPT_YX.NAME_ = '制药与生物工程系' AND HQ_CODE_MAJOR.ISTRUE = 1;
```

**答案**: 5个（状态1，含0的有9个）

---

## 示例 43

**问题**: 1004.0

**难度**: BC

```sql
SELECT DISTINCT bm.NAME_ AS 院系名称, jys.NAME_ AS 教研室名称 FROM HQ_CODE_DEPT_BM bm LEFT JOIN HQ_CODE_DEPT_JYS jys ON bm.ID = jys.DEPT_ID WHERE bm.NAME_ = '人工智能与大数据学院' AND bm.ISTRUE = 1 AND jys.ISTRUE = 1;
```

**答案**: 5个（状态1，含0的有9个）

---

## 示例 44

**问题**: 1004.0

**难度**: BC

```sql
SELECT DISTINCT HQ_CODE_DEPT_BM.NAME_ AS 院系名称, HQ_CODE_DEPT_JYS.NAME_ AS 教研室名称 FROM HQ_CODE_DEPT_JYS LEFT JOIN HQ_CODE_DEPT_BM ON HQ_CODE_DEPT_JYS.DEPT_ID = HQ_CODE_DEPT_BM.ID WHERE HQ_CODE_DEPT_BM.NAME_ = '人工智能与大数据学院' AND HQ_CODE_DEPT_JYS.ISTRUE = 1;
```

**答案**: 5个（状态1，含0的有9个）

---

## 示例 45

**问题**: 1004.0

**难度**: BC

```sql
SELECT DISTINCT bm.NAME_ AS 院系名称, jys.NAME_ AS 教研室名称 FROM HQ_CODE_DEPT_BM bm LEFT JOIN HQ_CODE_DEPT_JYS jys ON bm.ID = jys.DEPT_ID WHERE bm.NAME_ = '人工智能与大数据学院' AND bm.ISTRUE = 1 AND jys.ISTRUE = 1;
```

**答案**: 5个（状态1，含0的有9个）

---

## 示例 46

**问题**: 1004.0

**难度**: BC

```sql
SELECT DISTINCT jys.NAME_ AS 教研室名称 FROM HQ_CODE_DEPT_JYS jys LEFT JOIN HQ_CODE_DEPT_BM bm ON jys.DEPT_ID = bm.ID WHERE bm.NAME_ = '高职研究院(已删)' AND jys.ISTRUE = 1;
```

**答案**: 高职研究院是个学院，状态是0，其下无教研室

---

## 示例 47

**问题**: 1004.0

**难度**: BC

```sql
SELECT DISTINCT jys.NAME_ AS 教研室名称, yx.NAME_ AS 院系名称, yx.CODE_ AS 院系代码 FROM HQ_CODE_DEPT_JYS jys LEFT JOIN HQ_CODE_DEPT_BM bm ON jys.DEPT_ID = bm.ID LEFT JOIN HQ_CODE_DEPT_YX yx ON bm.ID = yx.ID WHERE jys.NAME_ = '制药技术教育教学部' AND jys.ISTRUE = 1 AND bm.ISTRUE = 1 AND yx.ISTRUE = 1;
```

**答案**: 制药与生物工程系（10034）

---

## 示例 48

**问题**: 1004.0

**难度**: BC

```sql
SELECT DISTINCT JYS.NAME_ AS 教研室名称, YX.NAME_ AS 院系名称, YX.CODE_ AS 院系代码 FROM HQ_CODE_DEPT_JYS JYS LEFT JOIN HQ_CODE_DEPT_BM BM ON JYS.DEPT_ID = BM.ID LEFT JOIN HQ_CODE_DEPT_YX YX ON BM.ID = YX.ID WHERE JYS.NAME_ = '制药技术教育教学部' AND JYS.ISTRUE = 1 AND BM.ISTRUE = 1 AND YX.ISTRUE = 1;
```

**答案**: 制药与生物工程系（10034）

---

## 示例 49

**问题**: 1005.0

**难度**: BC

```sql
SELECT DISTINCT jys.NAME_ AS 教研室名称, yx.NAME_ AS 院系名称, yx.CODE_ AS 院系代码 FROM HQ_CODE_DEPT_JYS jys LEFT JOIN HQ_CODE_DEPT_BM bm ON jys.DEPT_ID = bm.ID LEFT JOIN HQ_CODE_DEPT_YX yx ON bm.ID = yx.ID WHERE jys.NAME_ = '制药技术教育教学部' AND jys.ISTRUE = 1 AND bm.ISTRUE = 1 AND yx.ISTRUE = 1;
```

**答案**: 制药与生物工程系（10034）

---

## 示例 50

**问题**: 1005.0

**难度**: BC

```sql
SELECT DISTINCT j.NAME_ AS 教研室名称, b.NAME_ AS 院系名称, b.CODE_ AS 院系代码 FROM HQ_CODE_DEPT_JYS j LEFT JOIN HQ_CODE_DEPT_BM b ON j.DEPT_ID = b.ID WHERE j.NAME_ = '制药技术教育教学部' AND b.LEVEL_TYPE = 'YX' AND j.ISTRUE = 1 AND b.ISTRUE = 1;
```

**答案**: 制药与生物工程系（10034）

---

## 示例 51

**问题**: 1005.0

**难度**: BC

```sql
SELECT DISTINCT JYS.NAME_ AS 教研室名称, BM.NAME_ AS 院系名称, BM.CODE_ AS 院系代码 FROM HQ_CODE_DEPT_JYS JYS LEFT JOIN HQ_CODE_DEPT_BM BM ON JYS.DEPT_ID = BM.ID WHERE JYS.NAME_ = '制药技术教育教学部' AND JYS.ISTRUE = 1;
```

**答案**: 制药与生物工程系（10034）

---

## 示例 52

**问题**: 1005.0

**难度**: BC

```sql
SELECT DISTINCT bm.NAME_ AS 部门名称, bm.CODE_ AS 代码 FROM HQ_CODE_DEPT_JYS jys LEFT JOIN HQ_CODE_DEPT_BM bm ON jys.DEPT_ID = bm.ID WHERE jys.NAME_ = '数学教学部' AND jys.ISTRUE = 1;
```

**答案**: 教务处（10071）

---

## 示例 53

**问题**: 1005.0

**难度**: BC

```sql
SELECT DISTINCT JYS.NAME_ AS 教研室名称, YX.NAME_ AS 院系名称, YX.CODE_ AS 院系代码 FROM HQ_CODE_DEPT_JYS JYS LEFT JOIN HQ_CODE_DEPT_BM BM ON JYS.DEPT_ID = BM.ID LEFT JOIN HQ_CODE_DEPT_YX YX ON BM.ID = YX.ID WHERE JYS.NAME_ = '数学教学部' AND BM.LEVEL_TYPE = 'YX' AND JYS.ISTRUE = 1 AND BM.ISTRUE = 1 AND YX.ISTRUE = 1;
```

**答案**: 不属于某个学院，属于教务处（10071）

---

## 示例 54

**问题**: 1005.0

**难度**: BC

```sql
SELECT DISTINCT JYS.NAME_ AS 教研室名称, BM.NAME_ AS 所属部门 FROM HQ_CODE_DEPT_JYS JYS LEFT JOIN HQ_CODE_DEPT_BM BM ON JYS.DEPT_ID = BM.ID WHERE JYS.ISTRUE = 1 AND JYS.NAME_ IN ('制药技术教育教学部', '数学教学部', '数控教育教学部', '机电教育教学部');
```

**答案**: 制药与生物工程系（10034）、教务处（10071）、智能制造学院（中德智能制造学院）10029、智能制造学院（中德智能制造学院）10029

---

## 示例 55

**问题**: 1005.0

**难度**: BC

```sql
SELECT DISTINCT jys.NAME_ AS 教研室名称, tea.NAME_ AS 教师名称 FROM HQ_CODE_DEPT_JYS jys LEFT JOIN HQ_CODE_DEPT_JYS_CY cy ON jys.ID = cy.JYS_ID LEFT JOIN HQ_RS_TEA tea ON cy.TEA_NO = tea.TEA_NO WHERE jys.NAME_ = '应用教育教学部' AND jys.ISTRUE = 1 AND cy.ISTRUE = 1;
```

**答案**: 18个成员

---

## 示例 56

**问题**: 1005.0

**难度**: BC

```sql
SELECT DISTINCT jys.NAME_ AS 教研室名称, tea.NAME_ AS 教师名称, tea.TEA_NO AS 工号 FROM HQ_CODE_DEPT_JYS jys LEFT JOIN HQ_CODE_DEPT_JYS_CY cy ON jys.ID = cy.JYS_ID LEFT JOIN HQ_RS_TEA tea ON cy.TEA_NO = tea.TEA_NO WHERE jys.NAME_ = '计算机基础教育教学部' AND jys.ISTRUE = 1;
```

**答案**: 0，该教研室状态是0，其下有11位成员，状态都是0

---

## 示例 57

**问题**: 1005.0

**难度**: BC

```sql
SELECT DISTINCT jys.NAME_ AS 教研室名称, tea.NAME_ AS 教师名称, tea.TEA_NO AS 工号 FROM HQ_CODE_DEPT_JYS jys LEFT JOIN HQ_CODE_DEPT_JYS_CY cy ON jys.ID = cy.JYS_ID LEFT JOIN HQ_RS_TEA tea ON cy.TEA_NO = tea.TEA_NO WHERE jys.NAME_ = '计算机基础教学部' AND jys.ISTRUE = '1' AND cy.ISTRUE = '1' AND tea.IS_NORMAL = '1';
```

**答案**: 13

---

## 示例 58

**问题**: 1005.0

**难度**: BC

```sql
SELECT DISTINCT jys.NAME_ AS 教研室名称, tea.NAME_ AS 教师名称, tea.TEA_NO AS 工号 FROM HQ_CODE_DEPT_JYS jys LEFT JOIN HQ_CODE_DEPT_JYS_CY cy ON jys.ID = cy.JYS_ID LEFT JOIN HQ_RS_TEA tea ON cy.TEA_NO = tea.TEA_NO WHERE jys.NAME_ = '计算机基础教学部' AND jys.ISTRUE = 1 AND cy.ISTRUE = 1;
```

**答案**: 13

---

## 示例 59

**问题**: 1006.0

**难度**: BC

```sql
SELECT DISTINCT jys.NAME_ AS 教研室名称, tea.NAME_ AS 教师名称, tea.TEA_NO AS 工号 FROM HQ_CODE_DEPT_JYS jys LEFT JOIN HQ_CODE_DEPT_JYS_CY cy ON jys.ID = cy.JYS_ID LEFT JOIN HQ_RS_TEA tea ON cy.TEA_NO = tea.TEA_NO WHERE jys.NAME_ = '计算机基础教学部' AND jys.ISTRUE = 1;
```

**答案**: 13

---

## 示例 60

**问题**: 1006.0

**难度**: BC

```sql
SELECT DISTINCT jys.NAME_ AS 教研室名称 FROM HQ_RS_TEA tea LEFT JOIN HQ_CODE_DEPT_JYS_CY cy ON tea.TEA_NO = cy.TEA_NO LEFT JOIN HQ_CODE_DEPT_JYS jys ON cy.JYS_ID = jys.ID WHERE tea.NAME_ = '闫静静';
```

**答案**: 计算机基础教学部（120921）

---

## 示例 61

**问题**: 1006.0

**难度**: BC

```sql
SELECT DISTINCT jys.NAME_ AS 教研室名称 FROM HQ_RS_TEA tea LEFT JOIN HQ_CODE_DEPT_JYS_CY cy ON tea.TEA_NO = cy.TEA_NO LEFT JOIN HQ_CODE_DEPT_JYS jys ON cy.JYS_ID = jys.ID WHERE tea.NAME_ = '闫静静' AND jys.ISTRUE = 1;
```

**答案**: 计算机基础教学部（120921）

---

## 示例 62

**问题**: 1006.0

**难度**: BC

```sql
SELECT DISTINCT jys.NAME_ AS 教研室名称 FROM HQ_RS_TEA tea LEFT JOIN HQ_CODE_DEPT_JYS_CY cy ON tea.TEA_NO = cy.TEA_NO LEFT JOIN HQ_CODE_DEPT_JYS jys ON cy.JYS_ID = jys.ID WHERE tea.NAME_ = '闫静静' AND tea.IS_NORMAL = 1;
```

**答案**: 计算机基础教学部（120921）

---

## 示例 63

**问题**: 1006.0

**难度**: BC

```sql
SELECT DISTINCT JYS.NAME_ AS 教研室名称 FROM HQ_RS_TEA TEA LEFT JOIN HQ_CODE_DEPT_BM BM ON TEA.DEPT_ID = BM.ID LEFT JOIN HQ_CODE_DEPT_JYS JYS ON BM.ID = JYS.DEPT_ID WHERE TEA.NAME_ = '闫静静' AND BM.ISTRUE = 1 AND JYS.ISTRUE = 1;
```

**答案**: 计算机基础教学部（120921）

---

## 示例 64

**问题**: 1006.0

**难度**: BC

```sql
SELECT DISTINCT jys.NAME_ AS 教研室名称 FROM HQ_RS_TEA tea LEFT JOIN HQ_CODE_DEPT_JYS_CY cy ON tea.TEA_NO = cy.TEA_NO LEFT JOIN HQ_CODE_DEPT_JYS jys ON cy.JYS_ID = jys.ID WHERE tea.NAME_ = '闫静静' AND jys.ISTRUE = 1;
```

**答案**: 计算机基础教学部（120921）

---

## 示例 65

**问题**: 1006.0

**难度**: BC

```sql
SELECT DISTINCT jys.NAME_ AS 教研室名称 FROM HQ_RS_TEA tea LEFT JOIN HQ_CODE_DEPT_JYS_CY cy ON tea.TEA_NO = cy.TEA_NO LEFT JOIN HQ_CODE_DEPT_JYS jys ON cy.JYS_ID = jys.ID WHERE tea.NAME_ = '闫静静' AND tea.IS_NORMAL = 1;
```

**答案**: 计算机基础教学部（120921）

---

## 示例 66

**问题**: 1006.0

**难度**: BC

```sql
SELECT DISTINCT jys.NAME_ AS 教研室名称, tea.NAME_ AS 教师名称, tea.TEA_NO AS 工号, bm.NAME_ AS 所属部门 FROM HQ_RS_TEA tea LEFT JOIN HQ_CODE_DEPT_JYS_CY cy ON tea.TEA_NO = cy.TEA_NO LEFT JOIN HQ_CODE_DEPT_JYS jys ON cy.JYS_ID = jys.ID LEFT JOIN HQ_CODE_DEPT_BM bm ON jys.DEPT_ID = bm.ID WHERE jys.ID = (SELECT jys.ID FROM HQ_RS_TEA tea LEFT JOIN HQ_CODE_DEPT_JYS_CY cy ON tea.TEA_NO = cy.TEA_NO LEFT JOIN HQ_CODE_DEPT_JYS jys ON cy.JYS_ID = jys.ID WHERE tea.NAME_ = '闫静静' AND jys.ISTRUE = 1) AND jys.ISTRUE = 1;
```

**答案**: 13位老师，状态含0的有23条数据

---

## 示例 67

**问题**: 1006.0

**难度**: BC

```sql
SELECT DISTINCT jys.NAME_ AS 教研室名称, tea.NAME_ AS 教师名称, tea.TEA_NO AS 工号, bm.NAME_ AS 所属部门 FROM HQ_RS_TEA tea LEFT JOIN HQ_CODE_DEPT_JYS_CY cy ON tea.TEA_NO = cy.TEA_NO LEFT JOIN HQ_CODE_DEPT_JYS jys ON cy.JYS_ID = jys.ID LEFT JOIN HQ_CODE_DEPT_BM bm ON jys.DEPT_ID = bm.ID WHERE jys.ID IN (SELECT jys.ID FROM HQ_RS_TEA tea LEFT JOIN HQ_CODE_DEPT_JYS_CY cy ON tea.TEA_NO = cy.TEA_NO LEFT JOIN HQ_CODE_DEPT_JYS jys ON cy.JYS_ID = jys.ID WHERE tea.NAME_ = '闫静静');
```

**答案**: 13位老师，状态含0的有23条数据

---

## 示例 68

**问题**: 1006.0

**难度**: BC

```sql
SELECT DISTINCT jys.NAME_ AS 教研室名称, tea.NAME_ AS 教师名称, tea.TEA_NO AS 工号, bm.NAME_ AS 所属部门 FROM HQ_RS_TEA tea LEFT JOIN HQ_CODE_DEPT_JYS_CY cy ON tea.TEA_NO = cy.TEA_NO LEFT JOIN HQ_CODE_DEPT_JYS jys ON cy.JYS_ID = jys.ID LEFT JOIN HQ_CODE_DEPT_BM bm ON jys.DEPT_ID = bm.ID WHERE jys.ID IN (SELECT jys.ID FROM HQ_RS_TEA tea LEFT JOIN HQ_CODE_DEPT_JYS_CY cy ON tea.TEA_NO = cy.TEA_NO LEFT JOIN HQ_CODE_DEPT_JYS jys ON cy.JYS_ID = jys.ID WHERE tea.NAME_ = '闫静静');
```

**答案**: 13位老师，状态含0的有23条数据

---

## 示例 69

**问题**: 1007.0

**难度**: BC

```sql
SELECT DISTINCT C.NAME_ AS 班级名称, C.NO_ AS 班级代码 FROM HQ_CODE_CLASSES C LEFT JOIN HQ_CODE_MAJOR M ON C.MAJOR_CODE = M.CODE_ WHERE M.NAME_ = '动漫制作技术' AND C.GRADE = 2023 AND C.ISTRUE = 1;
```

**答案**: 2023动漫制作1班、2班（含状态0 的有4个班）

---

## 示例 70

**问题**: 1007.0

**难度**: BC

```sql
SELECT DISTINCT C.NAME_ AS 班级名称, C.NO_ AS 班级代码 FROM HQ_CODE_CLASSES C LEFT JOIN HQ_CODE_MAJOR M ON C.MAJOR_CODE = M.CODE_ WHERE M.NAME_ = '动漫制作技术' AND C.GRADE = 2023 AND C.ISTRUE = 1;
```

**答案**: 2023动漫制作1班、2班（含状态0 的有4个班）

---

## 示例 71

**问题**: 1007.0

**难度**: BC

```sql
SELECT DISTINCT C.NAME_ AS 班级名称, C.NO_ AS 班级代码 FROM HQ_CODE_CLASSES C LEFT JOIN HQ_CODE_MAJOR M ON C.MAJOR_CODE = M.CODE_ WHERE M.NAME_ = '动漫制作技术' AND C.GRADE = 2023 AND C.ISTRUE = 1;
```

**答案**: 2023动漫制作1班、2班（含状态0 的有4个班）

---

## 示例 72

**问题**: 1007.0

**难度**: BC

```sql
SELECT DISTINCT C.NAME_ AS 班级名称, C.NO_ AS 班级代码 FROM HQ_CODE_CLASSES C LEFT JOIN HQ_CODE_MAJOR M ON C.MAJOR_CODE = M.CODE_ WHERE M.NAME_ = '动漫制作技术' AND C.GRADE = 2023 AND C.ISTRUE = 1;
```

**答案**: 2023动漫制作1班、2班（含状态0 的有4个班）

---

## 示例 73

**问题**: 1007.0

**难度**: BC

```sql
SELECT DISTINCT C.NAME_ AS 班级名称, C.NO_ AS 班级代码 FROM HQ_CODE_CLASSES C LEFT JOIN HQ_CODE_MAJOR M ON C.MAJOR_CODE = M.CODE_ WHERE M.NAME_ = '动漫制作技术' AND C.GRADE = 2023 AND C.ISTRUE = 1;
```

**答案**: 2023动漫制作1班、2班（含状态0 的有4个班）

---

## 示例 74

**问题**: 1007.0

**难度**: BC

```sql
SELECT DISTINCT C.NAME_ AS 班级名称, C.NO_ AS 班级代码 FROM HQ_CODE_CLASSES C LEFT JOIN HQ_CODE_MAJOR M ON C.MAJOR_CODE = M.CODE_ WHERE M.NAME_ = '动漫制作技术' AND C.GRADE = 2023 AND C.ISTRUE = 1;
```

**答案**: 2023动漫制作1班、2班（含状态0 的有4个班）

---

## 示例 75

**问题**: 1007.0

**难度**: BC

```sql
SELECT DISTINCT C.NAME_ AS 班级名称, C.NO_ AS 班级代码 FROM HQ_CODE_CLASSES C LEFT JOIN HQ_CODE_MAJOR M ON C.MAJOR_CODE = M.CODE_ WHERE M.NAME_ = '动漫制作技术' AND C.GRADE = 2023 AND C.ISTRUE = 1;
```

**答案**: 2023动漫制作1班、2班（含状态0 的有4个班）

---

## 示例 76

**问题**: 1007.0

**难度**: BC

```sql
SELECT DISTINCT C.NAME_ AS 班级名称, C.NO_ AS 班级代码 FROM HQ_CODE_CLASSES C LEFT JOIN HQ_CODE_MAJOR M ON C.MAJOR_CODE = M.CODE_ WHERE M.NAME_ = '动漫制作技术' AND C.GRADE = 2023 AND C.ISTRUE = 1;
```

**答案**: 2023动漫制作1班、2班（含状态0 的有4个班）

---

## 示例 77

**问题**: 1007.0

**难度**: BC

```sql
SELECT DISTINCT C.NAME_ AS 班级名称, C.NO_ AS 代码 FROM HQ_CODE_CLASSES C LEFT JOIN HQ_CODE_MAJOR M ON C.MAJOR_CODE = M.CODE_ WHERE M.NAME_ = '动漫制作技术' AND C.GRADE = 2023 AND C.ISTRUE = 1;
```

**答案**: 2023动漫制作1班、2班（含状态0 的有4个班）

---

## 示例 78

**问题**: 1007.0

**难度**: BC

```sql
SELECT DISTINCT C.NAME_ AS 班级名称, C.NO_ AS 代码 FROM HQ_CODE_CLASSES C LEFT JOIN HQ_CODE_MAJOR M ON C.MAJOR_CODE = M.CODE_ WHERE M.NAME_ = '动漫制作技术' AND C.GRADE = 2023 AND C.ISTRUE = 1;
```

**答案**: 2023动漫制作1班、2班（含状态0 的有4个班）

---

## 示例 79

**问题**: 1008.0

**难度**: BC

```sql
SELECT DISTINCT C.NAME_ AS 班级名称, C.NO_ AS 代码 FROM HQ_CODE_CLASSES C LEFT JOIN HQ_CODE_MAJOR M ON C.MAJOR_CODE = M.CODE_ WHERE M.NAME_ = '动漫制作技术' AND C.GRADE = 2023 AND C.ISTRUE = 1;
```

**答案**: 2023动漫制作1班、2班（含状态0 的有4个班）

---

## 示例 80

**问题**: 1008.0

**难度**: BC

```sql
SELECT DISTINCT C.NAME_ AS 班级名称, C.NO_ AS 班级代码, M.NAME_ AS 专业名称, M.CODE_ AS 专业代码 FROM HQ_CODE_CLASSES C LEFT JOIN HQ_CODE_MAJOR M ON C.MAJOR_CODE = M.CODE_ WHERE C.NAME_ = '夏季高考2019学前教育P05班' AND C.ISTRUE = 1;
```

**答案**: 学前教育6701023

---

## 示例 81

**问题**: 1008.0

**难度**: BC

```sql
SELECT DISTINCT C.NAME_ AS 班级名称, C.NO_ AS 班级代码, M.NAME_ AS 专业名称, M.CODE_ AS 代码 FROM HQ_CODE_CLASSES C LEFT JOIN HQ_CODE_MAJOR M ON C.MAJOR_CODE = M.CODE_ WHERE C.NAME_ = '夏季高考2019学前教育P05班';
```

**答案**: 学前教育6701023

---

## 示例 82

**问题**: 1008.0

**难度**: BC

```sql
SELECT DISTINCT C.NAME_ AS 班级名称, C.NO_ AS 班级代码, M.NAME_ AS 专业名称, M.CODE_ AS 代码 FROM HQ_CODE_CLASSES C LEFT JOIN HQ_CODE_MAJOR M ON C.MAJOR_CODE = M.CODE_ WHERE C.NAME_ = '夏季高考2019学前教育P05班' AND C.ISTRUE = 1;
```

**答案**: 学前教育6701023

---

## 示例 83

**问题**: 1008.0

**难度**: BC

```sql
SELECT DISTINCT C.NAME_ AS 班级名称, C.NO_ AS 班级代码, M.NAME_ AS 专业名称, M.CODE_ AS 代码 FROM HQ_CODE_CLASSES C LEFT JOIN HQ_CODE_MAJOR M ON C.MAJOR_CODE = M.CODE_ WHERE C.NAME_ = '夏季高考2019学前教育P05班' AND C.ISTRUE = 1;
```

**答案**: 学前教育6701023

---

## 示例 84

**问题**: 1008.0

**难度**: BC

```sql
SELECT DISTINCT C.NAME_ AS 班级名称, C.NO_ AS 班级代码, M.NAME_ AS 专业名称, M.CODE_ AS 代码 FROM HQ_CODE_CLASSES C LEFT JOIN HQ_CODE_MAJOR M ON C.MAJOR_CODE = M.CODE_ WHERE C.NAME_ = '夏季高考2019学前教育P05班' AND C.ISTRUE = 1;
```

**答案**: 学前教育6701023

---

## 示例 85

**问题**: 1008.0

**难度**: BC

```sql
SELECT DISTINCT C.NAME_ AS 班级名称, C.NO_ AS 班级代码, M.NAME_ AS 专业名称, M.CODE_ AS 代码 FROM HQ_CODE_CLASSES C LEFT JOIN HQ_CODE_MAJOR M ON C.MAJOR_CODE = M.CODE_ WHERE C.NAME_ = '夏季高考2019学前教育P05班' AND C.ISTRUE = 1 AND M.ISTRUE = 1;
```

**答案**: 学前教育6701023

---

## 示例 86

**问题**: 1008.0

**难度**: BC

```sql
SELECT DISTINCT M.NAME_ AS 专业名称, M.CODE_ AS 专业代码 FROM HQ_JX_TEACHCLASS T LEFT JOIN HQ_JX_TEACHCLASS_MAJOR TM ON T.ID = TM.TEACHCLASS_ID LEFT JOIN HQ_CODE_MAJOR M ON TM.MAJOR_CODE = M.CODE_ WHERE T.NAME_ = '夏季高考2019学前教育P05班' AND T.ISTRUE = 1 AND TM.ISTRUE = 1 AND M.ISTRUE = 1;
```

**答案**: 学前教育

---

## 示例 87

**问题**: 1008.0

**难度**: BC

```sql
SELECT DISTINCT C.NAME_ AS 班级名称, C.NO_ AS 班级代码, M.NAME_ AS 专业名称, M.CODE_ AS 代码 FROM HQ_CODE_CLASSES C LEFT JOIN HQ_CODE_MAJOR M ON C.MAJOR_CODE = M.CODE_ WHERE C.NAME_ = '夏季高考2019学前教育P05班' AND C.ISTRUE = 1;
```

**答案**: 学前教育

---

## 示例 88

**问题**: 1008.0

**难度**: BC

```sql
SELECT DISTINCT C.NAME_ AS 班级名称, C.NO_ AS 班级代码, M.NAME_ AS 专业名称, M.CODE_ AS 专业代码 FROM HQ_CODE_CLASSES C LEFT JOIN HQ_CODE_MAJOR M ON C.MAJOR_CODE = M.CODE_ WHERE C.NAME_ = '夏季高考2019学前教育P05班' AND C.ISTRUE = 1;
```

**答案**: 学前教育

---

## 示例 89

**问题**: 1009.0

**难度**: BC

```sql
SELECT DISTINCT C.NAME_ AS 班级名称, C.NO_ AS 班级代码, M.NAME_ AS 专业名称, M.CODE_ AS 专业代码 FROM HQ_CODE_CLASSES C LEFT JOIN HQ_CODE_MAJOR M ON C.MAJOR_CODE = M.CODE_ WHERE C.NAME_ = '夏季高考2019学前教育P05班' AND C.ISTRUE = 1;
```

**答案**: 学前教育

---

## 示例 90

**问题**: 1009.0

**难度**: BC

```sql
SELECT DISTINCT C.NAME_ AS 班级名称, C.NO_ AS 班级代码, M.NAME_ AS 专业名称, M.CODE_ AS 专业代码 FROM HQ_CODE_CLASSES C LEFT JOIN HQ_CODE_MAJOR M ON C.MAJOR_CODE = M.CODE_ WHERE C.NAME_ = '夏季高考2019学前教育P05班' AND C.ISTRUE = 1;
```

**答案**: 学前教育

---

## 示例 91

**问题**: 1009.0

**难度**: BC

```sql
SELECT DISTINCT NAME_ AS 班级名称, NO_ AS 代码, LENGTH_SCHOOLING AS 学制, GRADUATE_YEAR AS 毕业年份 FROM HQ_CODE_CLASSES WHERE NAME_ = '夏季高考2019学前教育P05班';
```

**答案**: 3  2022

---

## 示例 92

**问题**: 1009.0

**难度**: BC

```sql
SELECT DISTINCT NAME_ AS 班级名称, NO_ AS 代码, LENGTH_SCHOOLING AS 学制, GRADUATE_YEAR AS 毕业年份 FROM HQ_CODE_CLASSES WHERE NAME_ = '夏季高考2019学前教育P05班' AND ISTRUE = 1;
```

**答案**: 3  2022

---

## 示例 93

**问题**: 1009.0

**难度**: BC

```sql
SELECT DISTINCT NAME_ AS 班级名称, NO_ AS 代码, LENGTH_SCHOOLING AS 学制, GRADUATE_YEAR AS 毕业年份 FROM HQ_CODE_CLASSES WHERE NAME_ = '夏季高考2019学前教育P05班' AND ISTRUE = 1;
```

**答案**: 3  2022

---

## 示例 94

**问题**: 1009.0

**难度**: BC

```sql
SELECT DISTINCT NAME_ AS 班级名称, NO_ AS 代码, NOW_GRADE_NO AS 当前年级 FROM HQ_CODE_CLASSES WHERE NAME_ = '夏季高考2019学前教育P05班' AND ISTRUE = 1;
```

**答案**: 已毕业（3）

---

## 示例 95

**问题**: 1009.0

**难度**: BC

```sql
SELECT DISTINCT NAME_ AS 班级名称, NO_ AS 班级代码, GRADUATE_YEAR AS 毕业年份 FROM HQ_CODE_CLASSES WHERE NAME_ = '夏季高考2019学前教育P05班' AND ISTRUE = 1;
```

**答案**: 2022

---

## 示例 96

**问题**: 1009.0

**难度**: BC

```sql
SELECT DISTINCT NAME_ AS 班级名称, NO_ AS 班级代码, GRADUATE_YEAR AS 毕业年份 FROM HQ_CODE_CLASSES WHERE NAME_ = '夏季高考2019学前教育P05班';
```

**答案**: 2022

---

## 示例 97

**问题**: 1009.0

**难度**: BC

```sql
SELECT DISTINCT c.NAME_ AS 班级名称, c.NO_ AS 班级代码, t.NAME_ AS 班主任姓名, t.TEA_NO AS 班主任工号 FROM HQ_CODE_CLASSES c LEFT JOIN HQ_RS_FDYBZR_CLASS fc ON c.ID = fc.CLASS_ID LEFT JOIN HQ_RS_FDYBZR f ON fc.FDYBZR_ID = f.ID LEFT JOIN HQ_RS_TEA t ON f.TEA_NO = t.TEA_NO WHERE c.NAME_ = '夏季高考2019学前教育P05班' AND f.FDYBZR_CODE = (SELECT CODE_ FROM HQ_CODE WHERE GROUP_TYPE = 'FDYBZR_CODE' AND NAME_ = '班主任');
```

**答案**: 未查询到数据（原因是当前学年学期无带班信息，2021-2022-02班主任是李莎12304）

---

## 示例 98

**问题**: 1009.0

**难度**: BC

```sql
SELECT DISTINCT C.NAME_ AS 班级名称, C.NO_ AS 班级代码, Y.NAME_ AS 学院名称, Y.CODE_ AS 学院代码 FROM HQ_CODE_CLASSES C LEFT JOIN HQ_CODE_MAJOR M ON C.MAJOR_CODE = M.CODE_ LEFT JOIN HQ_CODE_DEPT_YX Y ON M.DEPT_ID = Y.ID WHERE C.NAME_ = '夏季高考2019学前教育P05班';
```

**答案**: 学前教育学院

---

## 示例 99

**问题**: 1010.0

**难度**: BC

```sql
SELECT DISTINCT c.NAME_ AS 班级名称, c.NO_ AS 班级代码, d.NAME_ AS 学院名称, d.CODE_ AS 学院代码 FROM HQ_CODE_CLASSES c LEFT JOIN HQ_CODE_MAJOR m ON c.MAJOR_CODE = m.CODE_ LEFT JOIN HQ_CODE_DEPT_YX d ON m.DEPT_ID = d.ID WHERE c.NAME_ = '夏季高考2019学前教育P05班' AND c.ISTRUE = 1;
```

**答案**: 学前教育学院

---

## 示例 100

**问题**: 1010.0

**难度**: BC

```sql
SELECT DISTINCT C.NAME_ AS 班级名称, C.NO_ AS 班级代码, D.NAME_ AS 学院名称, D.CODE_ AS 学院代码 FROM HQ_CODE_CLASSES C LEFT JOIN HQ_CODE_MAJOR M ON C.MAJOR_CODE = M.CODE_ LEFT JOIN HQ_CODE_DEPT_YX D ON M.DEPT_ID = D.ID WHERE C.NAME_ = '夏季高考2019学前教育P05班' AND C.ISTRUE = 1;
```

**答案**: 学前教育学院

---

