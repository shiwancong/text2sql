# 业务术语知识库

## 使用说明

本文档记录数据库相关的业务术语和概念，帮助理解用户查询意图并映射到正确的表和字段。

---

## 实际表名映射

### 核心业务表

| 业务概念 | 实际表名 | 说明 |
|----------|----------|------|
| 学校信息 | HQ_JC_XX | 学校基本信息 |
| 校区 | HQ_JC_XQ | 校区信息 |
| 学年学期 | HQ_CODE_XNXQ | 学年学期配置 |
| 课程表(课表) | HQ_JX_KCB | 课程排课信息 |
| 课程 | HQ_CODE_COURSE | 课程基本信息 |
| 教学班 | HQ_JX_TEACHCLASS | 教学班信息 |
| 学生 | HQ_XS_STU | 学生基本信息 |
| 教师 | HQ_RS_TEA | 教师基本信息 |
| 教师校区 | HQ_RS_TEA_XQ | 教师校区信息 |
| 专业 | HQ_CODE_MAJOR | 专业信息 |
| 部门/学院 | HQ_CODE_DEPT | 组织机构(部门/学院/专业) |
| 班级 | HQ_CODE_CLASSES | 班级信息 |
| 学生成绩 | HQ_XS_SCORE | 学生成绩信息 |

### 新增业务表 (A/BC级)

| 业务概念 | 实际表名 | 说明 | 级别 |
|----------|----------|------|------|
| 勤工助学 | HQ_XS_JZD_QGZX | 学生勤工助学岗位信息 | A |
| 困难补助 | HQ_XS_JZD_KNBZ | 学生困难补助信息 | A |
| 顶岗实习 | HQ_XS_DGSX | 学生顶岗实习信息 | A |
| 实习单位 | HQ_XS_DGSX_COMPANY | 实习单位信息 | A |
| 选课课程 | HQ_JX_COURSE_CHOICE | 选课课程信息 | A |
| 学生选课 | HQ_JX_COURSE_CHOICE_STU | 学生选课信息 | A |
| 教学活动 | HQ_JX_HD | 活动基本信息 | A |
| 学生作业 | HQ_JX_HD_ZYRW_XSZY | 学生作业内容信息 | A |
| 学生保险 | HQ_XS_STU_BX | 学生保险信息 | BC |
| 学生请销假 | HQ_XS_STU_QXJ | 学生请销假信息 | BC |
| 学生社团 | HQ_XS_STU_ST | 社团基本信息 | BC |
| 教师工资 | HQ_CW_TEA_SALARY | 教职工工资表 | BC |
| 学生收费 | HQ_CW_STU_CHARGE | 学生收费总表 | BC |
| 图书借阅 | HQ_TS_BOOK_BORROW | 图书借阅记录 | A |
| 一卡通 | HQ_YKT_CARD | 一卡通发卡信息 | A |
| 校园门禁 | HQ_YKT_SCH_RKE | 校园门禁记录 | A |
| 宿舍管理 | HQ_ZZJG_SS_SS | 宿舍基本信息 | A |
| 宿舍床位 | HQ_ZZJG_SS_BED | 宿舍床位基本信息 | A |
| 科研项目 | HQ_KY_XM_ZX | 纵向科研项目 | A |
| 科研论文 | HQ_KY_LW | 论文信息表 | A |
| 教师获奖 | HQ_RS_AWARD | 行政参赛获奖信息 | A |
| 学生获奖 | HQ_XS_COMPETITION_AWARD | 学生比赛信息 | A |
| 奖学金 | HQ_XS_STU_JXJ | 奖学金信息 | A |
| 助学金 | HQ_XS_STU_ZXJ | 学生助学金信息 | A |
| 招生录取 | HQ_ZS_STU | 招生录取数据 | A |
| 就业信息 | HQ_JY_EMPLOYMENT | 学生就业明细数据 | A |

### 代码表（字典表）

| 代码类型 | 说明 |
|----------|------|
| SEX_CODE | 性别：1-男，2-女 |
| NATION_CODE | 民族代码 |
| POLITICS_CODE | 政治面貌代码 |
| PYCC_CODE | 培养层次：1-博士，2-硕士，3-本科，4-专科 |
| STU_STATE_CODE | 学生状态：01-在读，02-休学，03-退学，07-毕业 |
| COURSE_TYPE_CODE | 课程类型代码 |
| COURSE_ATTR_CODE | 课程属性代码 |
| COURSE_NATURE_CODE | 课程性质代码 |
| ZYJSZW_ID | 专业专业技术职务 |
| GWJB_ID | 岗位级别 |

---

## 教学管理术语

### 学期相关

| 术语 | 英文 | 说明 | 实际表/字段 |
|------|------|------|------------|
| 学期 | Semester | 教学周期 | HQ_CODE_XNXQ.TERM_CODE (01/02) |
| 本学期 | Current Semester | 当前学期 | 最新记录或通过日期判断 |
| 学年 | Academic Year | 如 2019-2020 | HQ_CODE_XNXQ.SCHOOL_YEAR |
| 开学时间 | Start Date | 学期开始日期 | HQ_CODE_XNXQ.BEGIN_DATE |
| 结课时间 | End Date | 学期结束日期 | HQ_CODE_XNXQ.END_DATE |
| 教学开始日期 | Teaching Start Date | 教学周开始 | HQ_CODE_XNXQ.TEACH_BEGIN_DATE |
| 教学结束日期 | Teaching End Date | 教学周结束 | HQ_CODE_XNXQ.TEACH_END_DATE |

### 课程相关

| 术语 | 英文 | 说明 | 实际表/字段 |
|------|------|------|------------|
| 课程 | Course | 教学课程 | HQ_CODE_COURSE.NAME_ |
| 课程代码 | Course Code | 课程编号 | HQ_CODE_COURSE.CODE_ |
| 课程类型 | Course Type | 课程分类 | HQ_CODE_COURSE.COURSE_TYPE_CODE |
| 理实一体课 | Integrated Course | 理论实践结合 | COURSE_TYPE_CODE 对应的理实一体类型 |
| 必修/选修 | Required/Elective | 课程性质 | HQ_CODE_COURSE.COURSE_NATURE_CODE |
| 学分 | Credit | 课程学分 | HQ_CODE_COURSE.CREDIT |
| 课时 | Period Count | 课程总课时 | HQ_CODE_COURSE.PERIOD_COUNT |
| 理论课时 | Theory Periods | 理论学时 | HQ_CODE_COURSE.PERIOD_THEORY |
| 实践课时 | Practice Periods | 实践学时 | HQ_CODE_COURSE.PERIOD_PRACTICE |
| 核心课 | Core Course | 是否核心课 | HQ_CODE_COURSE.IS_CORE = 1 |
| 教学班 | Teaching Class | 上课班级 | HQ_JX_TEACHCLASS.NAME_ |

### 教师相关

| 术语 | 英文 | 说明 | 实际表/字段 |
|------|------|------|------------|
| 教师 | Teacher | 授课教师 | HQ_RS_TEA.NAME_ |
| 教工号 | Teacher No | 教师编号 | HQ_RS_TEA.TEA_NO |
| 职称 | Title | 职务职称 | HQ_RS_TEA.ZW_NAME / ZYJSZW_ID |
| 专业负责人 | Major Head | 专业负责人 | HQ_CODE_MAJOR.FZR_NO (关联教师工号) |
| 部门负责人 | Dept Head | 部门负责人 | HQ_CODE_DEPT.FZR_NO (关联教师工号) |
| 入职日期 | In Date | 入职时间 | HQ_RS_TEA.IN_DATE |
| 参加工作日期 | Work Date | 工作起始 | HQ_RS_TEA.WORK_DATE |
| 学历 | Education | 最高学历 | HQ_RS_TEA.EDU_ID |
| 学位 | Degree | 学位 | HQ_RS_TEA.DEGREE_ID |

### 学生相关

| 术语 | 英文 | 说明 | 实际表/字段 |
|------|------|------|------------|
| 学生 | Student | 在校学生 | HQ_XS_STU.NAME_ |
| 学号 | Student No | 学生编号 | HQ_XS_STU.STU_NO |
| 班级 | Class | 所属班级 | HQ_XS_STU.CLASS_ID (关联 HQ_CODE_CLASSES.NO_) |
| 专业 | Major | 所属专业 | HQ_XS_STU.MAJOR_CODE (关联 HQ_CODE_MAJOR.CODE_) |
| 学院/部门 | Department | 所属院系 | HQ_XS_STU.DEPT_ID (关联 HQ_CODE_DEPT) |
| 年级 | Grade | 入学年级 | HQ_XS_STU.ENROLL_GRADE |
| 入学年份 | Enroll Year | 入学年 | HQ_XS_STU.ENROLL_YEAR |
| 民族 | Ethnicity | 学生民族 | HQ_XS_STU.NATION_CODE |
| 性别 | Sex/Gender | 性别 | HQ_XS_STU.SEX_CODE (1-男，2-女) |
| 少数民族 | Minority | 非汉族民族 | NATION_CODE IS NOT NULL AND NATION_CODE != '01' (01为汉族，NULL表示未填报) |
| 学生状态 | Student State | 在读/休学/毕业 | HQ_XS_STU.STU_STATE_CODE |
| 在校学生 | Normal Student | 正常在校 | HQ_XS_STU.IS_NORMAL = 1 |
| 培养层次 | PYCC | 专科/本科/研究生 | HQ_XS_STU.PYCC_CODE |
| 学制 | Length of Schooling | 学习年限 | HQ_XS_STU.LENGTH_SCHOOLING |

### 教室/校区相关

| 术语 | 英文 | 说明 | 实际表/字段 |
|------|------|------|------------|
| 校区 | Campus | 学校分区 | HQ_JC_XQ.NAME_ |
| 教室 | Classroom | 上课地点 | HQ_JX_KCB.CLASSROOM_ID |
| 办公电话 | Office Phone | 联系电话 | HQ_JC_XQ.OFFICE_PHONE |
| 校区地址 | Address | 校区地址 | HQ_JC_XQ.ADDRESS |

---

## 常见查询意图映射

### 统计类

| 用户问题 | 语义 | SQL 关键字 |
|----------|------|------------|
| 有多少 | 计数 | COUNT(*) |
| 数量 | 计数 | COUNT(*) |
| 总数 | 计数 | COUNT(*) |
| 平均 | 平均值 | AVG() |
| 比例 | 百分比 | CASE WHEN + COUNT/SUM |
| 排名 | 排序 | ORDER BY + RANK() |

### 查询类

| 用户问题 | 语义 | SQL 关键字 |
|----------|------|------------|
| 是什么 | 单值查询 | SELECT ... WHERE ... ROWNUM = 1 |
| 有哪些 | 列表查询 | SELECT ... |
| 哪些 | 筛选查询 | SELECT ... WHERE |
| 几号到几号 | 日期范围 | WHERE date BETWEEN ... AND ... |
| 范围 | 区间查询 | WHERE BEGIN_DATE AND END_DATE |

### 关联类

| 用户问题 | 语义 | SQL 关键字 |
|----------|------|------------|
| A 的 B | 关联查询 | JOIN |
| 在哪里上课 | 位置查询 | JOIN classroom |
| 什么时候上课 | 时间查询 | WHERE WEEKS/DAY_OF_WEEK/PERIOD |
| 本学期 | 当前学期 | 最新学期或日期匹配 |

---

## 时间相关表达

| 表达 | 含义 | SQL 实现 |
|------|------|----------|
| 本学期 | 当前学期 | ORDER BY BEGIN_DATE DESC FETCH FIRST 1 ROW |
| 本周 | 当前周 | WHERE WEEKS LIKE '%当前周%' |
| 本月 | 当前月份 | WHERE TO_CHAR(date, 'YYYY-MM') = TO_CHAR(SYSDATE, 'YYYY-MM') |
| 今年 | 当前年份 | WHERE SCHOOL_YEAR LIKE '%2024%' |
| 今天 | 当前日期 | WHERE date = TRUNC(SYSDATE) |
| 学期范围 | 开学到结课 | SELECT TEACH_BEGIN_DATE, TEACH_END_DATE |

---

## 常见字段值映射

### 性别 (SEX_CODE)
| 值 | 说明 |
|----|------|
| 1 | 男 |
| 2 | 女 |

### 培养层次 (PYCC_CODE)
| 值 | 说明 |
|----|------|
| 1 | 博士 |
| 2 | 硕士 |
| 3 | 本科 |
| 4 | 专科 |
| 9 | 其他 |

### 学生状态 (STU_STATE_CODE)
| 值 | 说明 |
|----|------|
| 01 | 在读 |
| 02 | 休学 |
| 03 | 退学 |
| 07 | 毕业 |
| 08 | 结业 |
| 09 | 肄业 |

### 学期代码 (TERM_CODE)
| 值 | 说明 |
|----|------|
| 01 | 第一学期（秋季/上学期） |
| 02 | 第二学期（春季/下学期） |

### 是否 (ISTRUE / IS_NORMAL)
| 值 | 说明 |
|----|------|
| 1 | 是/有效 |
| 0 | 否/无效 |

---

## 系统提示词中使用

当用户使用以下术语时，参考此文档：

- "理实一体课" → HQ_CODE_COURSE.COURSE_TYPE_CODE 查找对应类型
- "少数民族" → NATION_CODE IS NOT NULL AND NATION_CODE != '01' (01为汉族，NULL表示未填报，不应算作少数民族)
- "本学期" → HQ_CODE_XNXQ 按 BEGIN_DATE DESC 取最新记录
- "专业负责人" → HQ_CODE_MAJOR.FZR_NO 关联 HQ_RS_TEA.TEA_NO
- "部门负责人" → HQ_CODE_DEPT.FZR_NO 关联 HQ_RS_TEA.TEA_NO
- "学期范围" → HQ_CODE_XNXQ.TEACH_BEGIN_DATE 到 TEACH_END_DATE
- "学校名称" → HQ_JC_XX.NAME_

---

## 重要注意事项

### NULL值处理（🔥 极重要！）

当查询涉及可能为NULL的字段时（如NATION_CODE），必须显式处理NULL值：

| 场景 | 错误做法 | 正确做法 |
|------|---------|---------|
| 查询少数民族 | `WHERE NATION_CODE != '01'` | `WHERE NATION_CODE IS NOT NULL AND NATION_CODE != '01'` |
| 计算少数民族比例 | `COUNT(CASE WHEN NATION_CODE != '01' THEN 1 END)` | `COUNT(CASE WHEN NATION_CODE IS NOT NULL AND NATION_CODE != '01' THEN 1 END)` |

**原因**：
- NULL != '01' 的结果是 NULL（非TRUE）
- 在某些聚合场景下，NULL可能被错误统计
- NULL 表示未填报/未知，不应算作少数民族

---

## 注意事项

1. **表名前缀**：大部分表以 `HQ_` 开头
2. **命名约定**：
   - `JC_` = 基础/基础信息 (如学校、校区)
   - `CODE_` = 代码/字典表
   - `XS_` = 学生相关
   - `RS_` = 人事/教师相关
   - `JX_` = 教学相关
3. **字段后缀**：
   - `_CODE` 通常表示外键或代码
   - `_ID` 通常表示主键或外键
   - `NAME_` 表示名称（注意下划线后缀）
   - `NO_` 表示编号
4. **同义词识别**：用户可能用"学院"、"部门"、"院系"表示同一概念
5. **关联字段**：
   - 学生→专业：HQ_XS_STU.MAJOR_CODE → HQ_CODE_MAJOR.CODE_
   - 学生→班级：HQ_XS_STU.CLASS_ID → HQ_CODE_CLASSES.ID/NO_
   - 专业→学院：HQ_CODE_MAJOR.DEPT_ID → HQ_CODE_DEPT.ID
   - 教师→部门：HQ_RS_TEA.DEPT_ID → HQ_CODE_DEPT.ID

---

## 常见查询意图映射

### 统计类

| 用户问题 | 语义 | SQL 关键字 |
|----------|------|------------|
| 有多少 | 计数 | COUNT(*) |
| 数量 | 计数 | COUNT(*) |
| 总数 | 计数 | COUNT(*) |
| 平均 | 平均值 | AVG() |
| 比例 | 百分比 | CASE WHEN + COUNT/SUM |
| 排名 | 排序 | ORDER BY + RANK() |

### 查询类

| 用户问题 | 语义 | SQL 关键字 |
|----------|------|------------|
| 是什么 | 单值查询 | SELECT ... WHERE ... LIMIT 1 |
| 有哪些 | 列表查询 | SELECT ... |
| 哪些 | 筛选查询 | SELECT ... WHERE |
| 几号到几号 | 日期范围 | WHERE date BETWEEN ... AND ... |

### 关联类

| 用户问题 | 语义 | SQL 关键字 |
|----------|------|------------|
| A 的 B | 关联查询 | JOIN |
| 在哪里上课 | 位置查询 | JOIN classroom |
| 什么时候上课 | 时间查询 | JOIN schedule/time_slot |

---

## 时间相关表达

| 表达 | 含义 | SQL 实现 |
|------|------|----------|
| 本学期 | 当前学期 | WHERE is_current = 1 |
| 本周 | 当前周 | WHERE week_no = CURRENT_WEEK |
| 本月 | 当前月份 | WHERE TO_CHAR(date, 'YYYY-MM') = TO_CHAR(SYSDATE, 'YYYY-MM') |
| 今年 | 当前年份 | WHERE TO_CHAR(date, 'YYYY') = TO_CHAR(SYSDATE, 'YYYY') |
| 今天 | 当前日期 | WHERE date = TRUNC(SYSDATE) |
| 最近N天 | 日期范围 | WHERE date >= SYSDATE - N |

---

## 常见字段值映射

### 性别
| 值 | 说明 |
|----|------|
| 1 / M / 男 | 男 |
| 2 / F / 女 | 女 |

### 状态
| 值 | 说明 |
|----|------|
| 1 / active | 启用/有效 |
| 0 / inactive | 禁用/无效 |

### 是非
| 值 | 说明 |
|----|------|
| 1 / Y | 是 |
| 0 / N | 否 |

---

## 系统提示词中使用

当用户使用以下术语时，参考此文档：

- "理实一体课" → COURSE_TYPE 表查找对应类型
- "少数民族" → 使用 IS_MINORITY 字段或 NATION 字段判断
- "本学期" → 查找 IS_CURRENT = 1 的学期记录
- "专业负责人" → 在 TEACHER 表中查找 IS_HEAD = 1 或通过 MAJOR 表的 HEAD_ID 关联

---

## 注意事项

1. **同义词识别**：用户可能用不同的词表达相同概念（如"学院"和"部门"）
2. **缩写处理**：注意识别缩写（如"理实一体"是"理论与实践一体化"的简称）
3. **方言/口语**：理解用户的自然表达，不要求术语完全规范
4. **上下文推断**：根据前后文理解用户意图

---

## RAG 集成说明

### RAG 检索策略

当处理用户查询时，系统使用以下 RAG 检索策略：

1. **表检索**
   - 使用 `ragflow_search(query="关键词", dataset="ddl")` 检索相关表
   - 检索关键词应包含业务术语（如"学生"、"课程"、"教师"）

2. **字段检索**
   - 使用 `ragflow_get_schema(table_name)` 获取表结构详情
   - 确认字段名、数据类型和注释

3. **示例检索**
   - 使用 `ragflow_get_examples(query="用户问题", category="类型")` 获取相似示例
   - category: "simple" (单表), "join" (多表), "aggregate" (聚合)

### 检索验证

- **术语验证**：结合本知识库的业务术语映射验证 RAG 返回结果
- **表关系验证**：参考 table-relationships.md 确认表间关联关系
- **结果一致性**：确保 RAG 返回的表名与实际数据库一致

### 时间相关处理

对于"本学期/今年"等时间查询：

1. **判断当前学期**
   - 检索条件: `BEGIN_DATE <= SYSDATE AND END_DATE >= SYSDATE`
   - 使用 RAG 检索学期表相关字段

2. **数据存在性检查**
   - 如果查询结果为空，明确告知用户"暂无当前学期数据"
   - 不要编造或推测数据

3. **常用时间模式**
   ```sql
   -- 本学期
   WHERE BEGIN_DATE <= SYSDATE AND END_DATE >= SYSDATE

   -- 指定学年
   WHERE SCHOOL_YEAR = '2024-2025'

   -- 指定学期
   WHERE TERM_CODE = '01'  -- 01:上学期, 02:下学期
   ```

### RAG 服务降级

如果 RAGFlow 服务不可用：

- 回退到直接使用 `describe_table()` 和 `list_tables()`
- 使用本知识库的术语映射进行表名推断
- 基于字段命名规则推断关联关系
