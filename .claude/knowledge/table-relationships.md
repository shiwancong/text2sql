# 表关系知识库

## 使用说明

本文档记录数据库中表之间的关联关系，供生成 JOIN 查询时参考。

## 表关系图例

- `1:1` - 一对一关系
- `1:N` - 一对多关系（最常见）
- `N:M` - 多对多关系（通过中间表）
- `PK` - 主键 (Primary Key)
- `FK` - 外键 (Foreign Key)

---

## 教学核心表关系

```
                    ┌─────────────┐
                    │  SEMESTER   │
                    │   (学期)     │
                    └──────┬──────┘
                           │
        ┌──────────────────┼──────────────────┐
        │                  │                  │
        ▼                  ▼                  ▼
┌───────────────┐  ┌───────────────┐  ┌───────────────┐
│    COURSE     │  │   SCHEDULE    │  │  CLASSROOM    │
│   (课程表)     │  │  (课程安排)    │  │   (教室)      │
└───────┬───────┘  └───────┬───────┘  └───────┬───────┘
        │                  │                  │
        │         ┌────────┴────────┐         │
        │         │                 │         │
        ▼         ▼                 ▼         ▼
┌───────────────┐  ┌───────────────┐  ┌───────────────┐
│ COURSE_TYPE   │  │   TEACHER     │  │  BUILDING     │
│  (课程类型)    │  │   (教师)      │  │   (楼栋)      │
└───────────────┘  └───────┬───────┘  └───────────────┘
                           │
                           │ 1:N
                           ▼
                  ┌───────────────┐
                  │  DEPARTMENT   │
                  │   (部门/学院)  │
                  └───────────────┘
```

## 学生相关表关系

```
                    ┌─────────────┐
                    │  STUDENT    │
                    │   (学生)     │
                    └──────┬──────┘
                           │
        ┌──────────────────┼──────────────────┐
        │                  │                  │
        ▼ 1:N              ▼ N:M              ▼ 1:N
┌───────────────┐  ┌───────────────┐  ┌───────────────┐
│    CLASS      │  │  SELECTION    │  │    MAJOR      │
│   (班级)      │  │  (选课记录)    │  │   (专业)      │
└───────┬───────┘  └───────┬───────┘  └───────┬───────┘
        │                  │                  │
        │                  │                  │ 1:N
        ▼                  ▼                  ▼
┌───────────────┐  ┌───────────────┐  ┌───────────────┐
│   MAJOR       │  │   COURSE      │  │  DEPARTMENT   │
│  (专业)       │  │   (课程)      │  │   (部门)      │
└───────────────┘  └───────────────┘  └───────────────┘
```

---

## 详细关系定义

### 学生 (STUDENT)

| 关联表 | 关系类型 | 关联字段 | 说明 |
|--------|----------|----------|------|
| CLASS | N:1 | STUDENT.CLASS_ID → CLASS.ID | 学生属于一个班级 |
| MAJOR | N:1 | STUDENT.MAJOR_CODE → MAJOR.CODE_ | 学生属于一个专业 |
| DEPARTMENT | N:1 | STUDENT.DEPT_ID → DEPARTMENT.ID | 学生所属学院 |
| SELECTION | 1:N | STUDENT.ID → SELECTION.STUDENT_ID | 学生的选课记录 |
| ATTENDANCE | 1:N | STUDENT.ID → ATTENDANCE.STUDENT_ID | 学生的出勤记录 |
| EXAM_RESULT | 1:N | STUDENT.ID → EXAM_RESULT.STUDENT_ID | 学生的考试成绩 |
| HQ_XS_SCORE | 1:N | STUDENT.STU_NO → HQ_XS_SCORE.STU_NO | 学生的成绩记录 |

### 课程 (COURSE)

| 关联表 | 关系类型 | 关联字段 | 说明 |
|--------|----------|----------|------|
| COURSE_TYPE | N:1 | COURSE.TYPE_ID → COURSE_TYPE.ID | 课程类型 |
| TEACHER | N:1 | COURSE.TEACHER_ID → TEACHER.ID | 授课教师 |
| DEPARTMENT | N:1 | COURSE.DEPT_ID → DEPARTMENT.ID | 开课学院 |
| SELECTION | 1:N | COURSE.ID → SELECTION.COURSE_ID | 课程被选情况 |
| SCHEDULE | 1:N | COURSE.ID → SCHEDULE.COURSE_ID | 课程安排 |

### 教师 (TEACHER)

| 关联表 | 关系类型 | 关联字段 | 说明 |
|--------|----------|----------|------|
| DEPARTMENT | N:1 | TEACHER.DEPT_ID → DEPARTMENT.ID | 所属部门 |
| COURSE | 1:N | TEACHER.ID → COURSE.TEACHER_ID | 教授的课程 |
| SCHEDULE | 1:N | TEACHER.ID → SCHEDULE.TEACHER_ID | 排课记录 |
| HQ_RS_TEA_XQ | 1:N | TEACHER.TEA_NO → HQ_RS_TEA_XQ.TEA_NO | 教师校区信息 |

### 班级 (CLASS)

| 关联表 | 关系类型 | 关联字段 | 说明 |
|--------|----------|----------|------|
| MAJOR | N:1 | CLASS.MAJOR_ID → MAJOR.ID | 班级所属专业 |
| STUDENT | 1:N | CLASS.ID → STUDENT.CLASS_ID | 班级内的学生 |

### 专业 (MAJOR)

| 关联表 | 关系类型 | 关联字段 | 说明 |
|--------|----------|----------|------|
| DEPARTMENT | N:1 | MAJOR.DEPT_ID → DEPARTMENT.ID | 专业所属学院 |
| CLASS | 1:N | MAJOR.ID → CLASS.MAJOR_ID | 专业下的班级 |
| STUDENT | 1:N | MAJOR.ID → STUDENT.MAJOR_ID | 专业下的学生 |

### 课程安排 (SCHEDULE)

| 关联表 | 关系类型 | 关联字段 | 说明 |
|--------|----------|----------|------|
| COURSE | N:1 | SCHEDULE.COURSE_ID → COURSE.ID | 安排的课程 |
| TEACHER | N:1 | SCHEDULE.TEACHER_ID → TEACHER.ID | 授课教师 |
| CLASSROOM | N:1 | SCHEDULE.ROOM_ID → CLASSROOM.ID | 上课教室 |
| SEMESTER | N:1 | SCHEDULE.SEMESTER_ID → SEMESTER.ID | 所属学期 |
| TIME_SLOT | N:1 | SCHEDULE.TIME_ID → TIME_SLOT.ID | 时间段 |

### 教室 (CLASSROOM)

| 关联表 | 关系类型 | 关联字段 | 说明 |
|--------|----------|----------|------|
| BUILDING | N:1 | CLASSROOM.BUILDING_ID → BUILDING.ID | 所在楼栋 |
| SCHEDULE | 1:N | CLASSROOM.ID → SCHEDULE.ROOM_ID | 教室使用安排 |

---

## 常见查询场景的表组合

### 查询学生的课程
```
STUDENT → SELECTION → COURSE → COURSE_TYPE
         → TEACHER
         → SCHEDULE → CLASSROOM
```

### 查询教师的授课安排
```
TEACHER → SCHEDULE → COURSE
         → CLASSROOM → BUILDING
         → TIME_SLOT
         → SEMESTER
```

### 查询专业的学生统计
```
DEPARTMENT → MAJOR → CLASS → STUDENT
                       → SELECTION → COURSE
```

### 查询课程的学生名单
```
COURSE → SELECTION → STUDENT → CLASS → MAJOR
         → SCHEDULE → CLASSROOM
```

---

## 中间表（多对多关系）

### 选课记录 (SELECTION)
连接 STUDENT 和 COURSE
- 主键：(STUDENT_ID, COURSE_ID) 或独立 ID
- 附加字段：STATUS（状态）, SCORE（成绩）, SELECT_TIME（选课时间）

### 班级成员（如果存在）
连接 CLASS 和 STUDENT
- 用于管理班级-学生关系
- 可能包含：角色（班长/学员）、入班时间等

---

## 补充说明

1. **表名约定**：实际表名可能与上述不同，使用 describe_table() 确认
2. **字段命名**：外键通常格式为 `关联表名_ID`（如 MAJOR_ID）
3. **NULL 处理**：可选关联使用 LEFT JOIN，必须匹配使用 INNER JOIN
4. **循环引用**：注意避免 A→B→C→A 的循环关联

---

## 新增表关系 (A/BC级)

### 勤工助学 (HQ_XS_JZD_QGZX)

| 关联表 | 关系类型 | 关联字段 | 说明 |
|--------|----------|----------|------|
| HQ_XS_STU | N:1 | STU_NO → HQ_XS_STU.STU_NO | 学生 |
| HQ_CODE_CLASSES | N:1 | CLASS_ID → HQ_CODE_CLASSES.ID | 班级 |
| HQ_CODE_DEPT | N:1 | DEPT_ID → HQ_CODE_DEPT.ID | 用人部门 |

### 顶岗实习 (HQ_XS_DGSX)

| 关联表 | 关系类型 | 关联字段 | 说明 |
|--------|----------|----------|------|
| HQ_XS_DGSX_COMPANY | 1:N | COMPANY_ID → HQ_XS_DGSX_COMPANY.ID | 实习单位 |
| HQ_XS_DGSX_SXXX | 1:N | HQ_XS_DGSX.ID → HQ_XS_DGSX_SXXX.DGSX_ID | 实习信息 |

### 学生选课 (HQ_JX_COURSE_CHOICE_STU)

| 关联表 | 关系类型 | 关联字段 | 说明 |
|--------|----------|----------|------|
| HQ_JX_COURSE_CHOICE | N:1 | COURSE_CHOICE_ID → HQ_JX_COURSE_CHOICE.ID | 选课课程 |
| HQ_XS_STU | N:1 | STU_NO → HQ_XS_STU.STU_NO | 学生 |

### 教学活动 (HQ_JX_HD)

| 关联表 | 关系类型 | 关联字段 | 说明 |
|--------|----------|----------|------|
| HQ_JX_HD_STCY | 1:N | HQ_JX_HD.ID → HQ_JX_HD_STCY.HD_ID | 活动参与 |
| HQ_JX_HD_ZYRW | 1:N | HQ_JX_HD.ID → HQ_JX_HD_ZYRW.HD_ID | 作业任务 |
| HQ_JX_HD_TPWJ_TG | 1:N | HQ_JX_HD.ID → HQ_JX_HD_TPWJ_TG.HD_ID | 投票问卷 |

### 学生作业 (HQ_JX_HD_ZYRW_XSZY)

| 关联表 | 关系类型 | 关联字段 | 说明 |
|--------|----------|----------|------|
| HQ_JX_HD_ZYRW | N:1 | ZYRW_ID → HQ_JX_HD_ZYRW.ID | 作业任务 |
| HQ_XS_STU | N:1 | STU_NO → HQ_XS_STU.STU_NO | 学生 |

### 教师工资 (HQ_CW_TEA_SALARY)

| 关联表 | 关系类型 | 关联字段 | 说明 |
|--------|----------|----------|------|
| HQ_RS_TEA | N:1 | TEA_NO → HQ_RS_TEA.TEA_NO | 教师 |
| HQ_CW_TEA_SALARY_DETAIL | 1:N | HQ_CW_TEA_SALARY.ID → HQ_CW_TEA_SALARY_DETAIL.SALARY_ID | 工资明细 |

### 学生收费 (HQ_CW_STU_CHARGE)

| 关联表 | 关系类型 | 关联字段 | 说明 |
|--------|----------|----------|------|
| HQ_XS_STU | N:1 | STU_NO → HQ_XS_STU.STU_NO | 学生 |
| HQ_CW_STU_CHARGE_DETAIL | 1:N | HQ_CW_STU_CHARGE.ID → HQ_CW_STU_CHARGE_DETAIL.CHARGE_ID | 收费明细 |
| HQ_CW_STU_CHARGE_BILL | 1:N | HQ_CW_STU_CHARGE.ID → HQ_CW_STU_CHARGE_BILL.CHARGE_ID | 收费单 |

### 图书借阅 (HQ_TS_BOOK_BORROW)

| 关联表 | 关系类型 | 关联字段 | 说明 |
|--------|----------|----------|------|
| HQ_TS_BOOK | N:1 | BOOK_ID → HQ_TS_BOOK.ID | 图书 |
| HQ_XS_STU | N:1 | READER_ID → HQ_XS_STU.STU_NO | 读者(学生) |

### 一卡通 (HQ_YKT_CARD)

| 关联表 | 关系类型 | 关联字段 | 说明 |
|--------|----------|----------|------|
| HQ_YKT_CARD_IDENTITY | N:1 | IDENTITY_ID → HQ_YKT_CARD_IDENTITY.ID | 持卡人身份 |
| HQ_YKT_CARD_DEPT | N:1 | DEPT_ID → HQ_YKT_CARD_DEPT.ID | 商户 |
| HQ_YKT_CARD_PAY | 1:N | HQ_YKT_CARD.ID → HQ_YKT_CARD_PAY.CARD_ID | 消费记录 |
| HQ_YKT_CARD_RECHARGE | 1:N | HQ_YKT_CARD.ID → HQ_YKT_CARD_RECHARGE.CARD_ID | 充值记录 |

### 宿舍管理 (HQ_ZZJG_SS_SS)

| 关联表 | 关系类型 | 关联字段 | 说明 |
|--------|----------|----------|------|
| HQ_ZZJG_SS_SSL | N:1 | SSL_ID → HQ_ZZJG_SS_SSL.ID | 宿舍楼 |
| HQ_ZZJG_SS_LC | N:1 | LC_ID → HQ_ZZJG_SS_LC.ID | 楼层 |
| HQ_ZZJG_SS_BED | 1:N | HQ_ZZJG_SS_SS.ID → HQ_ZZJG_SS_BED.SS_ID | 床位 |

### 科研项目 (HQ_KY_XM_ZX)

| 关联表 | 关系类型 | 关联字段 | 说明 |
|--------|----------|----------|------|
| HQ_KY_XM_CY | 1:N | HQ_KY_XM_ZX.ID → HQ_KY_XM_CY.XM_ID | 项目成员 |

### 科研论文 (HQ_KY_LW)

| 关联表 | 关系类型 | 关联字段 | 说明 |
|--------|----------|----------|------|
| HQ_KY_LW_CY | 1:N | HQ_KY_LW.ID → HQ_KY_LW_CY.LW_ID | 论文作者 |

### 学生社团 (HQ_XS_STU_ST)

| 关联表 | 关系类型 | 关联字段 | 说明 |
|--------|----------|----------|------|
| HQ_XS_STU_ST_CY | 1:N | HQ_XS_STU_ST.ID → HQ_XS_STU_ST_CY.ST_ID | 社团成员 |
| HQ_XS_STU_STHD | 1:N | HQ_XS_STU_ST.ID → HQ_XS_STU_STHD.ST_ID | 社团活动 |

### 奖学金 (HQ_XS_STU_JXJ)

| 关联表 | 关系类型 | 关联字段 | 说明 |
|--------|----------|----------|------|
| HQ_XS_STU | N:1 | STU_NO → HQ_XS_STU.STU_NO | 学生 |

### 助学金 (HQ_XS_STU_ZXJ)

| 关联表 | 关系类型 | 关联字段 | 说明 |
|--------|----------|----------|------|
| HQ_XS_STU | N:1 | STU_NO → HQ_XS_STU.STU_NO | 学生 |

### 学生获奖 (HQ_XS_COMPETITION_AWARD)

| 关联表 | 关系类型 | 关联字段 | 说明 |
|--------|----------|----------|------|
| HQ_XS_COMPETITION_AWARD_STU | 1:N | HQ_XS_COMPETITION_AWARD.ID → HQ_XS_COMPETITION_AWARD_STU.AWARD_ID | 参赛学生 |
| HQ_XS_COMPETITION_AWARD_TEA | 1:N | HQ_XS_COMPETITION_AWARD.ID → HQ_XS_COMPETITION_AWARD_TEA.AWARD_ID | 指导教师 |

---

## 常见查询场景的表组合

### 查询勤工助学岗位
```
HQ_XS_JZD_QGZX → HQ_XS_STU (学生信息)
                 → HQ_CODE_CLASSES (班级信息)
                 → HQ_CODE_DEPT (部门信息)
```

### 查询学生选课
```
HQ_JX_COURSE_CHOICE_STU → HQ_JX_COURSE_CHOICE (选课课程)
                         → HQ_XS_STU (学生信息)
```

### 查询教师工资
```
HQ_CW_TEA_SALARY → HQ_RS_TEA (教师信息)
                 → HQ_CW_TEA_SALARY_DETAIL (工资明细)
```

### 查询学生收费
```
HQ_CW_STU_CHARGE → HQ_XS_STU (学生信息)
                  → HQ_CW_STU_CHARGE_DETAIL (收费明细)
                  → HQ_CW_STU_CHARGE_BILL (收费单)
```

### 查询学生社团活动
```
HQ_XS_STU_STHD → HQ_XS_STU_ST (社团信息)
                → HQ_XS_STU_ST_CY (社团成员)
```

### 查询科研论文
```
HQ_KY_LW → HQ_KY_LW_CY (论文作者)
         → HQ_KY_LW_ZZ (转载信息)
         → HQ_KY_LW_SL (收录信息)
```
