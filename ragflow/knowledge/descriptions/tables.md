# 表业务描述

生成时间: 2026-02-28 14:46:53

总表数: 69

---

## S级表 (69个)

### HQ_CODE

**业务概念**: 代码表

**说明**: 代码表

**注意事项**: 这些信息学校都会有

**责任部门**: 党办（通常来源党办部门、人才培养状态数据库、高基报表）

**字段列表**:

| 字段名 | 中文名 | 类型 | 说明 |
|--------|--------|------|------|
| ID | ID | VARCHAR2(60) | 主键，无特殊含义，唯一标识，不可重复； |
| CODE_ | 代码 | VARCHAR2(20) |  |
| NAME_ | 名称 | VARCHAR2(512) |  |
| GROUP_TYPE | 分组类型 | VARCHAR2(60) |  |
| GROUP_NAME | 分组名 | VARCHAR2(60) |  |
| CODE_CATEGORY_TYPE | 国标/部标/行标/校标 | VARCHAR2(20) |  |
| ORDER_ | 序号 | NUMBER(6) |  |
| ISTRUE | 是否可用 | NUMBER(1) |  |
| ID_USER_CREATE | 创建人ID | VARCHAR2(60) |  |
| CREATE_TIME | 创建时间 | VARCHAR2(30) |  |
| ID_USER_UPDATE | 修改人ID | VARCHAR2(60) |  |
| UPDATE_TIME | 修改时间 | VARCHAR2(30) |  |
| DES | 描述 | VARCHAR2(200) |  |

### HQ_CODE_CLASSES

**业务概念**: 行政班级信息

**说明**: 行政班级信息。用途：学校最基础的行政班级，影响：系统无法运行

**责任部门**: 教务处/学生处（根据学校管理情况而定）

**字段列表**:

| 字段名 | 中文名 | 类型 | 说明 |
|--------|--------|------|------|
| ID | ID | VARCHAR2(125) | 主键，无特殊含义，唯一标识，不可重复； |
| NO_ | 班级编号 | VARCHAR2(125) | 不能重复 |
| NAME_ | 班级名称 | VARCHAR2(64) |  |
| MAJOR_CODE | 所属专业CODE | VARCHAR2(60) | 对应：组织机构ID，行政组织结构表ID（HQ_CODE_DEPT） |
| LENGTH_SCHOOLING | 学制 | NUMBER(1) | 例：1/2/3/4/5…… |
| PYCC_CODE | 培养层次CODE | VARCHAR2(60) | 1：博士；2：硕士；3：本科；4：专科；9：其他（不可变更） |
| GRADE | 入学年级 | NUMBER(4) | 例：2018/2019 |
| GRADUATE_YEAR | 预计毕业年 | NUMBER(4) | 例：2021/2022 |
| GRADUATE_SCHOOLYEAR | 预计毕业学年 | VARCHAR2(32) | 例：2020-2021 |
| GRADUATE_DATE | 预计毕业日期 | VARCHAR2(32) | 例：2021-07-01 |
| ISTRUE | 是否可用 | NUMBER(1) | 1/0 |
| PINYIN | 拼音 | VARCHAR2(100) |  |
| NAME_SHORT | 简称 | VARCHAR2(100) |  |
| PINYIN_SHORT | 简称拼音 | VARCHAR2(100) |  |
| NOW_PYCC_CODE | 当前培养层次 | VARCHAR2(20) | 本科、专科…… |
| NOW_GRADE_NO | 当前年级 | NUMBER(1) |  |
| ORDER_ | 排序字段 | NUMBER(6) |  |

### HQ_CODE_COURSE

**业务概念**: 课程基本信息

**说明**: 课程库代码数据，仅存储课程最基本的数据

**责任部门**: 教务处（教务系统）

**字段列表**:

| 字段名 | 中文名 | 类型 | 说明 |
|--------|--------|------|------|
| ID | ID | VARCHAR2(60) | 主键，唯一 |
| CODE_ | 代码 | VARCHAR2(60) | 课程代码，通常为教务系统页面上提供给老师查看的编号，
注意不是教务系统内部使用的无意义唯一标识 |
| NAME_ | 名称 | VARCHAR2(100) |  |
| ZDKC_GRADE_CODE | 重点课程级别CODE | VARCHAR2(60) | 1：国家级，2：省部级，3：地市级；4：院校级，5：一般课程 |
| JPKC_GRADE_CODE | 精品课程级别CODE | VARCHAR2(60) | 1：国家级，2：省部级，3：地市级；4：院校级，5：一般课程 |
| YEAR_MONTH | 首次开课年月 | VARCHAR2(60) | yyyy-mm，如：2018-06 |
| COURSE_TYPE_CODE | 课程类型CODE | VARCHAR2(60) | A类（纯理论课）/B类（（理论＋实践）课）/ C类（纯实践课） |
| COURSE_ATTR_CODE | 课程属性CODE | VARCHAR2(60) | 公共课、专业基础课、专业课。 |
| COURSE_NATURE_CODE | 课程性质CODE | VARCHAR2(60) | 课程性质（单一选项）：必修课/专业选修课/公共选修课。 |
| FZR_NO | 课程负责人NO | VARCHAR2(60) |  |
| PERIOD_COUNT | 课时数 | NUMBER(10) |  |
| PERIOD_THEORY | 理论课时数 | NUMBER(10) |  |
| PERIOD_PRACTICE | 实践课时数 | NUMBER(10) |  |
| IS_CORE | 是否核心课程 | NUMBER(1) |  |
| IS_XQHZ | 是否校企合作 | NUMBER(1) |  |
| IS_KZRT | 是否课证融通 | NUMBER(1) |  |
| CREDIT | 学分 | NUMBER(4,1) |  |
| DEPT_ID | 课程承担单位ID | VARCHAR2(60) |  |
| ORDER_ | 排序号 | NUMBER(4) |  |
| BZ | 备注 | VARCHAR2(200) |  |
| ... | 还有 3 个字段 | | |

### HQ_CODE_DEPT

**业务概念**: 机构信息

**说明**: 组织机构信息。用途：学校最基础的行政/教学组织机构，影响：系统无法运行

**注意事项**: 包含“学校/部门/院系/教学单位（基础教学部、体育教学部等）/科室/专业”

**责任部门**: 党办（通常来源人事处、教务处）

**字段列表**:

| 字段名 | 中文名 | 类型 | 说明 |
|--------|--------|------|------|
| ID | ID | VARCHAR2(60) | 主键，无特殊含义，唯一标识，不可重复； |
| CODE_ | 代码 | VARCHAR2(60) | 代码不能重复 |
| NAME_ | 名称 | VARCHAR2(100) |  |
| NAME_SHORT | 简称 | VARCHAR2(60) |  |
| CODE_CATEGORY_TYPE | 分类 | VARCHAR2(60) |  |
| PID | 父节点 | VARCHAR2(60) |  |
| DES | 描述 | VARCHAR2(200) |  |
| PATH_ | 全息码 | VARCHAR2(200) | 例：0001/00010001 |
| LEVEL_ | 层次 | NUMBER(2) | 0/1/2/3（不可变更） |
| LEVEL_TYPE | 层次类型 | VARCHAR2(20) | XX/BM/KS/YX/ZY/JXDW（不可变更） |
| ISTRUE | 可用 | NUMBER(1) | 1/0 |
| ORDER_ | 排序号 | NUMBER(4) | 例：1/2/3…… |
| PINYIN | 拼音 | VARCHAR2(60) |  |
| PINYIN_SHORT | 简称拼音 | VARCHAR2(60) |  |
| ADMIN_MANAGE_TEA_NO | 行政负责人 | VARCHAR2(60) | 【2021-06-10：增加】废弃 |
| PARTY_MANAGE_TEA_NO | 党务负责人 | VARCHAR2(60) | 【2021-06-10：增加】废弃 |
| PARTY_FZR_NO | 党务负责人 | VARCHAR2(60) | 【2021-08-20：增加】 |
| FZR_NO | 行政负责人 | VARCHAR2(60) | 【2021-08-20：增加】 |
| LOSE_DATE | 废弃时间 | VARCHAR2(20) |  |
| ID_USER_CREATE | 创建人 | VARCHAR2(60) |  |
| ... | 还有 3 个字段 | | |

### HQ_CODE_DEPT_JYS

**业务概念**: 教研室或教学部信息

**说明**: 组织机构-教研室表

**责任部门**: 教务处

**字段列表**:

| 字段名 | 中文名 | 类型 | 说明 |
|--------|--------|------|------|
| ID | ID | VARCHAR2(60) | 主键，无特殊含义，唯一标识，不可重复； |
| DEPT_ID | 院系 | VARCHAR2(60) |  |
| CODE_ | 代码 | VARCHAR2(60) |  |
| NAME_ | 名称 | VARCHAR2(60) |  |
| ORDER_ | 排序 | NUMBER(4) | 教研室排序 |
| ISTRUE | 是否可用 | NUMBER(1) |  |
| ID_USER_CREATE | 创建人 | VARCHAR2(60) |  |
| CREATE_TIME | 创建时间 | VARCHAR2(30) |  |
| ID_USER_UPDATE | 修改人 | VARCHAR2(60) |  |
| UPDATE_TIME | 修改时间 | VARCHAR2(30) |  |

### HQ_CODE_DEPT_JYS_CY

**业务概念**: 教研室或教学部的成员

**说明**: 组织机构-教研室-成员表

**责任部门**: 教务处

**字段列表**:

| 字段名 | 中文名 | 类型 | 说明 |
|--------|--------|------|------|
| ID | ID | VARCHAR2(60) | 主键，无特殊含义，唯一标识，不可重复； |
| JYS_ID | 教研室ID | VARCHAR2(60) |  |
| TEA_NO | 职工号 | VARCHAR2(60) |  |
| TEA_NAME | 职工名称 | VARCHAR2(60) |  |
| MEMBER_TYPE | 成员类型 | VARCHAR2(60) | 1:主任；2：副主任；3：成员 |
| ORDER_ | 排序 | NUMBER(4) | 人员排序 |
| ISTRUE | 是否可用 | NUMBER(1) |  |
| ID_USER_CREATE | 创建人 | VARCHAR2(60) |  |
| CREATE_TIME | 创建时间 | VARCHAR2(30) |  |
| ID_USER_UPDATE | 修改人 | VARCHAR2(60) |  |
| UPDATE_TIME | 修改时间 | VARCHAR2(30) |  |

### HQ_CODE_MAJOR

**业务概念**: 专业基本信息

**说明**: 学校专业信息表，系统运行使用基础信息，不可缺少

**注意事项**: 学校一般把专业方向当成一个专业使用，导致与国标专业数量不一致的问题（采用校标专业与国标专业映射）

**责任部门**: 教务处（通常来源教务系统）

**字段列表**:

| 字段名 | 中文名 | 类型 | 说明 |
|--------|--------|------|------|
| ID | ID | VARCHAR2(60) | 主键，无特殊含义，唯一标识，不可重复；和组织机构保持一致 |
| CODE_ | 专业代码 | VARCHAR2(60) | 校标专业代码，和组织机构保持一致 |
| NAME_ | 名称 | VARCHAR2(100) | 专业名称 |
| DEPT_ID | 院系 | VARCHAR2(60) | 所属院系代码 |
| ORDER_ | 排序号 | NUMBER(4) | 排序号，学校对页面专业的显示顺序如有要求，可在此维护序号 |
| ISTRUE | 是否可用 | NUMBER(1) | 用于标识当前可用的专业，1：是，0：否 |
| YEAR_PZ | 批准年 | NUMBER(4) | 批准开设专业的年份，如：2017 |
| YEAR_ZS | 首次招生年 | NUMBER(4) | 首次招生年份，如：2018 |
| YEAR_TZ | 停止招生年 | NUMBER(4) | 停止招生年份，如：2019 |
| XYNX | 修业年限 | NUMBER(1) | 该专业的学生在校学习的年限，如：3 |
| ZDZY_CODE | 重点专业类型CODE | VARCHAR2(20) | 1：国家级，2：省级，3：地市级，4：校级 |
| TSZY_CODE | 特色专业类型CODE | VARCHAR2(20) | 1：国家级，2：省级 |
| IS_XDXTZ | 是否现代学徒制 | NUMBER(1) | 该专业是否为现代学徒试点专业，1：是，0：否 |
| IS_GJHZ | 是否国际合作专业 | NUMBER(1) | 该专业是否为国际合作专业，1：是，0：否 |
| IS_XQHZ | 是否校企合作 | NUMBER(1) | 该专业是否为校企合作，1：是，0：否 |
| DTR_IN_NAMES | 校内专业带头人名称 | VARCHAR2(256) | 校内专业带头人姓名，多个带头人以英文半角逗号隔开，如：张老师，李老师 |
| DTR_OUT_NAMES | 校外专业带头人名称 | VARCHAR2(512) | 校外专业带头人姓名，多个带头人以英文半角逗号隔开，如：张老师，李老师 |
| FZR_NO | 专业负责人NO | VARCHAR2(256) | 专业负责人工号，专业发展中心使用 |
| PINYIN | 拼音 | VARCHAR2(100) | 专业名称拼音简拼 |
| ZYFL_CODE | 专业分类 | VARCHAR2(60) | 1：本科；2：专科；3：专升本；用于人才培养方案 |
| ... | 还有 4 个字段 | | |

### HQ_CODE_MAJOR_DTR

**业务概念**: 专业带头人信息

**说明**: 

**注意事项**: 一个专业的校内、校外带头人可能有多个

**责任部门**: 教务处（通常来源教务系统）

**字段列表**:

| 字段名 | 中文名 | 类型 | 说明 |
|--------|--------|------|------|
| ID | ID | VARCHAR2(60) | 主键，无特殊含义，唯一标识，不可重复 |
| SCHOOL_YEAR | 学年 | VARCHAR2(10) |  |
| TERM_CODE | 学期 | VARCHAR2(20) |  |
| CODE_ | 专业代码 | VARCHAR2(60) | 校标专业代码，和组织机构保持一致 |
| TEA_NO | 带头人工号 | VARCHAR2(60) | 校外负责人可能没有工号 |
| NAME_ | 带头人名称 | VARCHAR2(60) |  |
| TYPE_ | 带头人类型 | VARCHAR2(60) | 1：校内；2：校外 |
| ORDER_ | 顺序 | NUMBER(4) |  |

### HQ_CODE_MAJOR_GROUP

**业务概念**: 专业群信息

**说明**: 专业群信息,相近专业组成一个群体，资源共享，共同发展

**责任部门**: 教务处

**字段列表**:

| 字段名 | 中文名 | 类型 | 说明 |
|--------|--------|------|------|
| ID | ID | VARCHAR2(60) | 主键，唯一 |
| NAME_ | 专业群名称 | VARCHAR2(60) |  |
| FZR_NO | 专业群负责人 | VARCHAR2(60) | 负责人工号 |
| YEAR_MONTH | 建立年月 | VARCHAR2(60) | YYYY-MM |
| MAJOR_GROUP_LEVEL_CODE | 专业群层级编码 |  |  |

### HQ_CODE_MAJOR_GROUP_MAPPER

**业务概念**: 专业群包含的专业

**说明**: 专业群与专业关联信息

**责任部门**: 教务处

**字段列表**:

| 字段名 | 中文名 | 类型 | 说明 |
|--------|--------|------|------|
| ID | ID | VARCHAR2(60) |  |
| MAJOR_GROUP_ID | 专业群ID | VARCHAR2(60) |  |
| MAJOR_CODE | 专业ID | VARCHAR2(60) | 校标专业代码 |

### HQ_CODE_MAJOR_MAPPER

**业务概念**: 学校专业对应的国标专业

**说明**: 校标专业与国标专业对应映射表

**注意事项**: 学校一般把专业方向当成一个专业使用，导致与国标专业数量不一致的问题（采用校标专业与国标专业映射）

**责任部门**: 教务处，通常需要手工对应并确认对应关系

**字段列表**:

| 字段名 | 中文名 | 类型 | 说明 |
|--------|--------|------|------|
| ID | ID | VARCHAR2(60) | 主键，唯一 |
| MAJOR_CODE | 校标专业CODE | VARCHAR2(60) | 校标专业代码 |
| GB_MAJOR_CODE | 国标专业CODE | VARCHAR2(60) | 国标专业代码 |
| GB_MAJOR_NAME | 国标专业名称 | VARCHAR2(100) | 国标专业名称 |
| GB_MAJOR_FX_CODE | 国标专业方向CODE | VARCHAR2(60) | 国标专业方向代码 |
| GB_MAJOR_FX_NAME | 国标专业方向名称 | VARCHAR2(100) | 国标专业方向名称 |
| ORDER_ | 排序号 | NUMBER(4) | 排序号 |
| ISTRUE | 是否可用 | NUMBER(1) | 是否可用，1：是，0：否 |

### HQ_CODE_MAJOR_XN

**业务概念**: 每学年的专业基本信息

**说明**: 学校专业信息表，系统运行使用基础信息，不可缺少

**注意事项**: 学校一般把专业方向当成一个专业使用，导致与国标专业数量不一致的问题（采用校标专业与国标专业映射）

**责任部门**: 教务处（通常来源教务系统）

**字段列表**:

| 字段名 | 中文名 | 类型 | 说明 |
|--------|--------|------|------|
| ID | ID | VARCHAR2(60) | 主键，无特殊含义，唯一标识，不可重复；和组织机构保持一致 |
| CODE_ | 专业代码 | VARCHAR2(60) | 校标专业代码，和组织机构保持一致 |
| NAME_ | 名称 | VARCHAR2(100) | 专业名称 |
| DEPT_ID | 院系DM | VARCHAR2(60) | 所属院系代码 |
| ORDER_ | 排序号 | NUMBER(4) | 排序号，学校对页面专业的显示顺序如有要求，可在此维护序号 |
| ISTRUE | 是否可用 | NUMBER(1) | 用于标识当前可用的专业，1：是，0：否 |
| YEAR_PZ | 批准年 | NUMBER(4) | 批准开设专业的年份，如：2017 |
| YEAR_ZS | 首次招生年 | NUMBER(4) | 首次招生年份，如：2018 |
| YEAR_TZ | 停止招生年 | NUMBER(4) | 停止招生年份，如：2019 |
| XYNX | 修业年限 | NUMBER(1) | 该专业的学生在校学习的年限，如：3 |
| ZDZY_CODE | 重点专业类型CODE | VARCHAR2(20) | 1：国家级，2：省级，3：地市级，4：校级 |
| TSZY_CODE | 特色专业类型CODE | VARCHAR2(20) | 1：国家级，2：省级 |
| IS_XDXTZ | 是否现代学徒制 | NUMBER(1) | 该专业是否为现代学徒试点专业，1：是，0：否 |
| IS_GJHZ | 是否国际合作专业 | NUMBER(1) | 该专业是否为国际合作专业，1：是，0：否 |
| IS_XQHZ | 是否校企合作 | NUMBER(1) | 该专业是否为校企合作，1：是，0：否 |
| DTR_IN_NAMES | 校内专业带头人名称 | VARCHAR2(256) | 校内专业带头人姓名，多个带头人以英文半角逗号隔开，如：张老师，李老师 |
| DTR_OUT_NAMES | 校外专业带头人名称 | VARCHAR2(512) | 校外专业带头人姓名，多个带头人以英文半角逗号隔开，如：张老师，李老师 |
| FZR_NO | 专业负责人NO | VARCHAR2(256) | 专业负责人工号，专业发展中心使用 |
| PINYIN | 拼音 | VARCHAR2(100) | 专业名称拼音简拼 |
| ZYFL_CODE | 专业分类 | VARCHAR2(60) | 1：本科；2：专科；3：专升本；用于人才培养方案 |
| ... | 还有 5 个字段 | | |

### HQ_CODE_MAJOR_YEAR

**业务概念**: 每年的专业基本信息

**说明**: 学校专业信息表，系统运行使用基础信息，不可缺少

**注意事项**: 学校一般把专业方向当成一个专业使用，导致与国标专业数量不一致的问题（采用校标专业与国标专业映射）

**责任部门**: 教务处（通常来源教务系统）

**字段列表**:

| 字段名 | 中文名 | 类型 | 说明 |
|--------|--------|------|------|
| ID | ID | VARCHAR2(60) | 主键，无特殊含义，唯一标识，不可重复；和组织机构保持一致 |
| CODE_ | 专业代码 | VARCHAR2(60) | 校标专业代码，和组织机构保持一致 |
| NAME_ | 名称 | VARCHAR2(100) | 专业名称 |
| DEPT_ID | 院系DM | VARCHAR2(60) | 所属院系代码 |
| ORDER_ | 排序号 | NUMBER(4) | 排序号，学校对页面专业的显示顺序如有要求，可在此维护序号 |
| ISTRUE | 是否可用 | NUMBER(1) | 用于标识当前可用的专业，1：是，0：否 |
| YEAR_PZ | 批准年 | NUMBER(4) | 批准开设专业的年份，如：2017 |
| YEAR_ZS | 首次招生年 | NUMBER(4) | 首次招生年份，如：2018 |
| YEAR_TZ | 停止招生年 | NUMBER(4) | 停止招生年份，如：2019 |
| XYNX | 修业年限 | NUMBER(1) | 该专业的学生在校学习的年限，如：3 |
| ZDZY_CODE | 重点专业类型CODE | VARCHAR2(20) | 1：国家级，2：省级，3：地市级，4：校级 |
| TSZY_CODE | 特色专业类型CODE | VARCHAR2(20) | 1：国家级，2：省级 |
| IS_XDXTZ | 是否现代学徒制 | NUMBER(1) | 该专业是否为现代学徒试点专业，1：是，0：否 |
| IS_GJHZ | 是否国际合作专业 | NUMBER(1) | 该专业是否为国际合作专业，1：是，0：否 |
| IS_XQHZ | 是否校企合作 | NUMBER(1) | 该专业是否为校企合作，1：是，0：否 |
| DTR_IN_NAMES | 校内专业带头人名称 | VARCHAR2(256) | 校内专业带头人姓名，多个带头人以英文半角逗号隔开，如：张老师，李老师 |
| DTR_OUT_NAMES | 校外专业带头人名称 | VARCHAR2(512) | 校外专业带头人姓名，多个带头人以英文半角逗号隔开，如：张老师，李老师 |
| FZR_NO | 专业负责人NO | VARCHAR2(256) | 专业负责人工号，专业发展中心使用 |
| PINYIN | 拼音 | VARCHAR2(100) | 专业名称拼音简拼 |
| ZYFL_CODE | 专业分类 | VARCHAR2(60) | 1：本科；2：专科；3：专升本；用于人才培养方案 |
| ... | 还有 5 个字段 | | |

### HQ_CODE_XNXQ

**业务概念**: 学年学期

**说明**: 每学期的开始、结束时间。用途：记录学期教学周时间和学期数据计算范围；影响：系统无法运行

**注意事项**: 及时更新最新数据

**责任部门**: 教务处（通常来源教务排课部门）

**字段列表**:

| 字段名 | 中文名 | 类型 | 说明 |
|--------|--------|------|------|
| ID | ID | VARCHAR2(20) | 主键，无特殊含义，唯一标识，不可重复； |
| SCHOOL_YEAR | 学年 | VARCHAR2(40) | 例：2019-2020 |
| TERM_CODE | 学期 | VARCHAR2(40) | 01/02 |
| TEACH_BEGIN_DATE | 教学开始时间 | VARCHAR2(40) | 格式：YYYY-MM-DD |
| TEACH_END_DATE | 教学结束时间 | VARCHAR2(40) | 格式：YYYY-MM-DD |
| TEACH_WEEK_FIRST_NO | 教学周起始星期几 | VARCHAR2(40) | 1/7（星期一或星期天） |
| BEGIN_DATE | 学期统计开始时间 | VARCHAR2(40) | 格式：YYYY-MM-DD（上下2个学期的统计开始时间与结束时间要无缝衔接） |
| END_DATE | 学期统计结束时间 | VARCHAR2(40) | 格式：YYYY-MM-DD |

### HQ_GB_MAJOR_CATALOGUE

**业务概念**: 国标专业目录

**说明**: 国标专业目录表。用途：学校最基础的行政/教学组织机构，影响：系统无法运行

**注意事项**: 包含“学校/部门/院系/教学单位（基础教学部、体育教学部等）/科室/专业”

**责任部门**: 党办（通常来源人事处、教务处）

**字段列表**:

| 字段名 | 中文名 | 类型 | 说明 |
|--------|--------|------|------|
| ID | ID | VARCHAR2(60) | 主键，无特殊含义，唯一标识，不可重复； |
| CODE_ | 代码 | VARCHAR2(60) | 代码不能重复 |
| NAME_ | 名称 | VARCHAR2(100) |  |
| PID | 父节点 | VARCHAR2(60) |  |
| PATH_ | 全息码 | VARCHAR2(200) | 例：0001/00010001 |
| LEVEL_ | 层次 | NUMBER(2) | 0/1/2/3（不可变更） |
| LEVEL_TYPE | 层次类型 | VARCHAR2(20) |  |
| ISTRUE | 可用 | NUMBER(1) | 1/0 |
| ORDER_ | 排序号 | NUMBER(4) | 例：1/2/3…… |
| PINYIN | 拼音 | VARCHAR2(60) |  |
| SHORT_NAME | 简称 | VARCHAR2(60) |  |
| SHORT_PINYIN | 简称拼音 | VARCHAR2(60) |  |
| PYCC_CODE | 培养层次CODE | VARCHAR2(60) | 1：博士；2：硕士；3：本科；4：专科；9：其他（不可变更） |
| YEAR_ | 开设年份 | NUMBER(4) |  |

### HQ_JC_HOLIDAY

**业务概念**: 节假日信息

**说明**: 每学期内的各个节假日开始、结束时间（不含日常周六、周日）。用途：记录未上课的相关事件；影响：课表数据的逻辑验证

**注意事项**: 及时更新最新数据

**责任部门**: 院办（通常来源校历制定部门）

**字段列表**:

| 字段名 | 中文名 | 类型 | 说明 |
|--------|--------|------|------|
| ID | ID | VARCHAR2(60) | 主键，无特殊含义，唯一标识，不可重复； |
| NAME_ | 名称 | VARCHAR2(100) | 例：国庆节 |
| SCHOOL_YEAR | 学年 | VARCHAR2(10) | 格式：YYYY-YYYY |
| TERM_CODE | 学期 | VARCHAR2(10) | 格式：01/02 |
| BEGIN_DATE | 开始时间 | VARCHAR2(10) | 格式：YYYY-MM-DD |
| END_DATE | 结束时间 | VARCHAR2(10) | 格式：YYYY-MM-DD |
| HOLIDAY_TYPE | 节假日类型 | VARCHAR2(60) |  |
| BZ | 备注 | VARCHAR2(200) |  |
| ID_USER_CREATE | 创建人 |  |  |
| CREATE_TIME | 创建时间 |  |  |
| ID_USER_UPDATE | 更新人 |  |  |
| UPDATE_TIME | 更新时间 |  |  |

### HQ_JC_JS_ZZJG

**业务概念**: 教学场地（校区、教学楼、楼层、教室）信息

**说明**: 教室组织机构信息。用途：教学地点信息，影响：相关数据无法显示

**注意事项**: 包含“学校XX/校区XQ/教学楼JXL/楼层LC/教室JS”

**责任部门**: 教务处（通常来源教务排课部门）

**字段列表**:

| 字段名 | 中文名 | 类型 | 说明 |
|--------|--------|------|------|
| ID | ID | VARCHAR2(60) | 主键，无特殊含义，唯一标识，不可重复； |
| CODE_ | 代码 | VARCHAR2(60) | 不能重复 |
| NAME_ | 名称 | VARCHAR2(100) |  |
| PID | 父节点 | VARCHAR2(60) |  |
| PATH_ | 全息码 | VARCHAR2(200) | 例：0001/00010001 |
| LEVEL_ | 层次 | NUMBER(2) | 0/1/2/3 |
| LEVEL_TYPE | 层次类型 | VARCHAR2(20) | XX/XQ/JXL/LC/JS |
| ISTRUE | 可用 | NUMBER(1) | 1/0 |
| ORDER_ | 排序号 | NUMBER(4) | 例：1/2/3…… |
| JSLX_CODE | 教室类型 | VARCHAR2(20) | 1：多媒体教室；2：语音室；3：实验室；4：计算机房；5：普通教室；6：专用教室；9：其他（不可变更 |
| ZW_COUNT | 座位数 | NUMBER(4) |  |
| JXL_ID | 教学楼 | VARCHAR2(60) |  |
| XQ_ID | 校区 | VARCHAR2(60) |  |
| CREATE_YEAR_MONTH | 创建年月 | VARCHAR2(7) | 例：2020-10 |

### HQ_JC_XX

**业务概念**: 学校基本信息

**说明**: 学校基本信息

**注意事项**: 这些信息学校都会有

**责任部门**: 党办（通常来源党办部门、人才培养状态数据库、高基报表）

**字段列表**:

| 字段名 | 中文名 | 类型 | 说明 |
|--------|--------|------|------|
| ID | ID | VARCHAR2(60) | 主键，无特殊含义，唯一标识，不可重复； |
| DM | 学校标识码 | VARCHAR2(20) | 教育部编制的在全国范围内唯一的、始终不变的10位学校标识码 |
| NAME_ | 学校名称 | VARCHAR2(60) | 在教育行政部门备案的学校全称 |
| SHORT_NAME | 学校简称 | VARCHAR2(60) | 自定义学校简称 |
| YWM | 学校英文名 | VARCHAR2(60) | 在教育行政部门备案的英文名称 |
| ORIGIN_PID | 所在省/自治区/直辖市_ID | VARCHAR2(20) | 行政区划代码（6位） |
| ORIGIN_ID | 所在城市/区/地市_ID | VARCHAR2(20) | 行政区划代码（6位） |
| XX_BXLX_CODE | 学校办学类型CODE | VARCHAR2(60) | 01 普通高等学校（大学、学院、独立学院、高等专科学校、高等职业学校、分校、大专班）、02 成人高等 |
| XX_XZLB_CODE | 学校性质类别CODE | VARCHAR2(60) | 01综合大学/02理工院校/03农业院校/04林业院校/05医药院校/06师范院校/07语文院校/  |
| JBZ_NAME | 学校举办者名称 | VARCHAR2(200) | 例：河南省郑州市二七区政府（参考高基报表或咨询党办机构） |
| XX_JBZXX_CODE | 学校举办者性质CODE | VARCHAR2(60) | 01 教育部门、02 其它部门、03 地方企业、04 民办 |
| XX_JBZJB_CODE | 学校举办者级别CODE | VARCHAR2(60) | 01 政府、02 行业、03 企业（集团）、04 公民个人、09其他 |
| JYXZBM | 属地管理教育行政部门名称 | VARCHAR2(200) | 例：河南省郑州市二七区教育局（参考高基报表或咨询党办机构） |
| JYXZBM_ORIGIN_ID | 属地管理教育行政部门代码 | VARCHAR2(20) | 属地管理教育行政部门所在地的行政区划代码（6位） |
| XXMC_CURRENT_YEAR_MONTH | 当前校名启用年月 | VARCHAR2(7) | 格式：YYYY-MM |
| CREATE_YEAR_MONTH | 建校年月 | VARCHAR2(7) | 格式：YYYY-MM |
| JXJC | 建校基础 | VARCHAR2(200) | 高等职业院校的筹建基础，具体包括哪几所学校 |
| MOTTO | 校训 | VARCHAR2(200) |  |
| ADDRESS | 学校地址 | VARCHAR2(200) | 学校登记注册的详细地址 |
| POSTALCODE | 邮政编码 | NUMBER(6) |  |
| ... | 还有 13 个字段 | | |

### HQ_JC_XX_LSYG

**业务概念**: 学校发展历史

**说明**: 学校历史沿革信息。用途：***，影响：相关系统功能

**注意事项**: 这些信息学校都会有

**责任部门**: 党办（通常来源党办部门、学校网站）

**字段列表**:

| 字段名 | 中文名 | 类型 | 说明 |
|--------|--------|------|------|
| ID | ID | VARCHAR2(60) | 主键，无特殊含义，唯一标识，不可重复； |
| NAME_ | 简介 | VARCHAR2(2000) |  |
| YEAR_MONTH | 获得年月 | VARCHAR2(20) | 格式：YYYY-MM |

### HQ_JC_XX_RY

**业务概念**: 学校荣誉

**说明**: 学校荣誉。用途：***，影响：相关系统功能

**注意事项**: 这些信息学校都会有

**责任部门**: 党办（通常来源党办部门、学校网站）

**字段列表**:

| 字段名 | 中文名 | 类型 | 说明 |
|--------|--------|------|------|
| ID | ID | VARCHAR2(60) | 主键，无特殊含义，唯一标识，不可重复； |
| XXRY_GRADE_CODE | 学校荣誉级别CODE | VARCHAR2(20) | 1：国家级；2：省部级；3：市厅局级；9：其他 |
| TITLE | 荣誉简介 | VARCHAR2(200) |  |
| DETAILS | 荣誉详情 | VARCHAR2(2000) |  |
| YEAR_MONTH | 获得年月 | VARCHAR2(20) | 格式：YYYY-MM |
| XXRY_TYPE_CODE | 荣誉类型 | VARCHAR2(20) |  |
| IS_PROJECT_APPROVAL | 是否立项 | NUMBER(1) |  |
| IS_TASK_THE_HEAD | 是否牵头 | NUMBER(1) |  |
| IS_JOIN | 是否参与 | NUMBER(1) |  |
| IS_ASSUME_HOLD | 是否承办 | NUMBER(1) |  |

### HQ_JX_JXZ

**业务概念**: 教学周

**说明**: 学校上课周次基本信息，一般从学期开学开始计算

**注意事项**: 教学周第一天:星期一/星期日

**责任部门**: 教务处（通常来源教务系统）

**字段列表**:

| 字段名 | 中文名 | 类型 | 说明 |
|--------|--------|------|------|
| ID | ID | VARCHAR2(60) | 主键，唯一 |
| SCHOOL_YEAR | 学年 | VARCHAR2(9) |  |
| TERM_CODE | 学期 | VARCHAR2(10) |  |
| WEEK | 周次 | NUMBER(2) | 1/2/3/... |
| BEGIN_DATE | 周开始日期 | VARCHAR2(10) | 格式:yyyy-mm-dd |
| END_DATE | 周结束日期 | VARCHAR2(10) | 格式:yyyy-mm-dd |
| ISTRUE | 是否可用 | NUMBER(1) |  |

### HQ_JX_JXZ_DAY

**业务概念**: 教学周包含的每天的时间

**说明**: 学校上课周次基本信息，一般从学期开学开始计算

**注意事项**: 教学周第一天:星期一/星期日

**责任部门**: 教务处（通常来源教务系统）

**字段列表**:

| 字段名 | 中文名 | 类型 | 说明 |
|--------|--------|------|------|
| ID | ID | VARCHAR2(60) | 主键，唯一 |
| SCHOOL_YEAR | 学年 | VARCHAR2(9) |  |
| TERM_CODE | 学期 | VARCHAR2(10) |  |
| WEEK | 周次 | NUMBER(2) | 1/2/3/... |
| DATE_ | 日期 | VARCHAR2(10) | 格式:yyyy-mm-dd |
| DAY_OF_WEEK | 星期 | NUMBER(1) | 1/2/3/…7 |
| ISTRUE | 是否可用 | NUMBER(1) |  |

### HQ_JX_KCB

**业务概念**: 课程表

**说明**: 课程表信息（含学生选修课信息）

**责任部门**: 教务处（通常来源教务系统）

**字段列表**:

| 字段名 | 中文名 | 类型 | 说明 |
|--------|--------|------|------|
| ID | ID | VARCHAR2(600) | 主键，唯一 |
| SCHOOL_YEAR | 学年 | VARCHAR2(9) |  |
| TERM_CODE | 学期 | VARCHAR2(10) |  |
| COURSE_CODE | 课程CODE | VARCHAR2(60) |  |
| TEACHCLASS_NAME | 教学班名称 | VARCHAR2(600) | 默认教务排课的上课班级，若有分组，则为“上课班级+分组名” |
| TEACHCLASS_ID | 教学班ID | VARCHAR2(600) | 学年+学期+课程+教学班名称，程序的解析逻辑 |
| DEPT_ID | 课程承担单位ID | VARCHAR2(60) |  |
| WEEKS | 周次明细(逗号分隔) | VARCHAR2(100) |  |
| DAY_OF_WEEK | 上课星期 | NUMBER(1) | 1 |
| PERIOD | 上课节次段 | VARCHAR2(10) | 1-2 |
| BEGIN_PERIOD | 开始节次 | NUMBER(2) | 1 |
| END_PERIOD | 截止节次 | NUMBER(2) | 2 |
| LECTURE_TYPE_CODE | 授课方式 | VARCHAR2(20) |  |
| CLASSROOM_ID | 上课教室 | VARCHAR2(600) |  |
| COURSE_TYPE_CODE | 课程类型_CODE | VARCHAR2(20) |  |
| COURSE_ATTR_CODE | 课程属性_CODE | VARCHAR2(20) |  |
| COURSE_NATURE_CODE | 课程性质_CODE | VARCHAR2(20) |  |
| WEEK_COUNT | 上课周数 | NUMBER(4) |  |
| ONCE_PERIOD_COUNT | 一次上课节次数 | NUMBER(4) | 2 |
| PERIOD_COUNT | 总节次数 | NUMBER(4) |  |
| ... | 还有 2 个字段 | | |

### HQ_JX_KCB_PERIOD

**业务概念**: 每天的每节课信息

**说明**: 每“一大节课”的课表数据，例：1-2节

**责任部门**: 教务处（通常来源教务系统）

**字段列表**:

| 字段名 | 中文名 | 类型 | 说明 |
|--------|--------|------|------|
| ID | ID | VARCHAR2(600) | 主键，唯一 |
| SCHOOL_YEAR | 学年 | VARCHAR2(9) |  |
| TERM_CODE | 学期 | VARCHAR2(10) |  |
| COURSE_CODE | 课程CODE | VARCHAR2(60) |  |
| TEACHCLASS_NAME | 教学班名称 | VARCHAR2(600) | 默认教务排课的上课班级，若有分组，则为“上课班级+分组名” |
| TEACHCLASS_ID | 教学班ID | VARCHAR2(600) | 学年+学期+课程+教学班名称，程序的解析逻辑 |
| DEPT_ID | 课程承担单位ID | VARCHAR2(60) |  |
| WEEKS | 周次明细(只有一周) | VARCHAR2(100) |  |
| DAY_OF_WEEK | 上课星期 | NUMBER(1) | 1 |
| PERIOD | 上课节次段 | VARCHAR2(10) | 1-2 |
| BEGIN_PERIOD | 开始节次 | NUMBER(2) | 1 |
| END_PERIOD | 截止节次 | NUMBER(2) | 2 |
| LECTURE_TYPE_CODE | 授课方式 | VARCHAR2(20) |  |
| CLASSROOM_ID | 上课教室 | VARCHAR2(600) |  |
| COURSE_TYPE_CODE | 课程类型_CODE | VARCHAR2(20) |  |
| COURSE_ATTR_CODE | 课程属性_CODE | VARCHAR2(20) |  |
| COURSE_NATURE_CODE | 课程性质_CODE | VARCHAR2(20) |  |
| WEEK_COUNT | 上课周数 | NUMBER(4) |  |
| ONCE_PERIOD_COUNT | 一次上课节次数 | NUMBER(4) | 2 |
| PERIOD_COUNT | 总节次数 | NUMBER(4) |  |
| ... | 还有 5 个字段 | | |

### HQ_JX_KCB_PERIOD_TEA

**业务概念**: 每天的每节课的授课教师

**说明**: 节次课表的授课教师，由程序自动从课表和课表教师解析生成，主要用于智慧课堂，评价等系统

**责任部门**: 教务处（通常来源教务系统）

**字段列表**:

| 字段名 | 中文名 | 类型 | 说明 |
|--------|--------|------|------|
| ID | ID | VARCHAR2(600) |  |
| KCB_PERIOD_ID | 节次课表ID | VARCHAR2(600) |  |
| TEA_NO | 教职工号 | VARCHAR2(60) |  |
| SCHOOL_YEAR | 学年 | VARCHAR2(9) |  |
| TERM_CODE | 学期 | VARCHAR2(10) |  |
| ISTRUE | 是否可用 | NUMBER(1) |  |

### HQ_JX_KCB_TEA

**业务概念**: 课程表的授课教师

**说明**: 教师授课信息表，由程序自动从课表解析生成，主要用于智慧课堂，专题分析等系统

**责任部门**: 教务处（通常来源教务系统）

**字段列表**:

| 字段名 | 中文名 | 类型 | 说明 |
|--------|--------|------|------|
| ID | ID | VARCHAR2(600) |  |
| KCB_ID | 课程表ID | VARCHAR2(600) |  |
| TEA_NO | 教职工号 | VARCHAR2(60) |  |
| SCHOOL_YEAR | 学年 | VARCHAR2(9) |  |
| TERM_CODE | 学期 | VARCHAR2(10) |  |
| ISTRUE | 是否可用 | NUMBER(1) |  |

### HQ_JX_MAJOR_COURSE

**业务概念**: 专业的课程信息

**说明**: 专业课程信息表，课程与专业关联，才具有其相关的属性

**注意事项**: 同一门课程在不同的专业中的属性不一样

**责任部门**: 教务处，部分信息可以从人才状态库补采获取

**字段列表**:

| 字段名 | 中文名 | 类型 | 说明 |
|--------|--------|------|------|
| ID | ID | VARCHAR2(60) |  |
| CODE_ | 课程代码 | VARCHAR2(60) |  |
| NAME_ | 课程名称 | VARCHAR2(100) |  |
| ZDKC_GRADE_CODE | 重点课程级别CODE | VARCHAR2(60) | 1：国家级，2：省部级，3：地市级；4：院校级，5：一般课程 |
| JPKC_GRADE_CODE | 精品课程级别CODE | VARCHAR2(60) | 1：国家级，2：省部级，3：地市级；4：院校级，5：一般课程 |
| COURSE_TYPE_CODE | 课程类型CODE | VARCHAR2(60) | A类（纯理论课）/B类（（理论＋实践）课）/ C类（纯实践课） |
| COURSE_ATTR_CODE | 课程属性CODE | VARCHAR2(60) | 公共课、专业基础课、专业课。 |
| COURSE_NATURE_CODE | 课程性质CODE | VARCHAR2(60) | 课程性质（单一选项）：必修课/专业选修课/公共选修课。 |
| FZR_NO | 课程负责人NO | VARCHAR2(60) |  |
| PERIOD_COUNT | 课时数 | NUMBER(10) |  |
| PERIOD_THEORY | 理论课时数 | NUMBER(10) |  |
| PERIOD_PRACTICE | 实践课时数 | NUMBER(10) |  |
| IS_CORE | 是否核心课程 | NUMBER(1) |  |
| IS_XQHZ | 是否校企合作 | NUMBER(1) |  |
| IS_KZRT | 是否课证融通 | NUMBER(1) |  |
| CREDIT | 学分 | NUMBER(4,1) |  |
| DEPT_ID | 课程承担单位ID | VARCHAR2(60) |  |
| ORDER_ | 排序号 | NUMBER(4) |  |
| ISTRUE | 是否可用 | NUMBER(1) |  |
| MAJOR_CODE | 所属专业 | VARCHAR2(60) |  |
| ... | 还有 4 个字段 | | |

### HQ_JX_PERIOD

**业务概念**: 上课时间信息

**说明**: 学校上课时间段基本信息，一般有冬夏时令之分(5.1/10.1)，不同校区/教学楼上课时间可能不一致

**注意事项**: 冬夏季时间来源系统参数表

**责任部门**: 教务处（通常来源教务系统）

**字段列表**:

| 字段名 | 中文名 | 类型 | 说明 |
|--------|--------|------|------|
| ID | ID | VARCHAR2(60) |  |
| PERIOD | 节次段 | VARCHAR2(60) | 1-3 |
| XJ_BEGIN_HOUR_MIN | 夏季开始上课时间 | VARCHAR2(20) | 8:00 |
| XJ_END_HOUR_MIN | 夏季结束上课时间 | VARCHAR2(20) | 10:20 |
| DJ_BEGIN_HOUR_MIN | 冬季开始上课时间 | VARCHAR2(20) | 8:20 |
| DJ_END_HOUR_MIN | 冬季结束上课时间 | VARCHAR2(20) | 10:40 |
| XQ_IDS | 校区 | VARCHAR2(600) | 多个校区ID，英文逗号分隔，与教学楼互斥，全校统一时间可为空 |
| JXL_IDS | 教学楼 | VARCHAR2(600) | 多个教学楼ID，英文逗号分隔，与校区互斥，全校统一时间可为空 |

### HQ_JX_PJ_JSPJ

**业务概念**: 同行评价、督导评价、检查评价明细

**说明**: 同行评价、督导评价、检查评价 明细

**字段列表**:

| 字段名 | 中文名 | 类型 | 说明 |
|--------|--------|------|------|
| ID | ID | VARCHAR2(64) | 主键，无特殊含义，唯一标识，不可重复； |
| RESULT_ID | 结果表ID | VARCHAR2(64) |  |
| ASSESS_PERSON_ID | 评价人ID | VARCHAR2(64) | 评价人（教职工号） |
| STATUS | 评价状态 | NUMBER(1) | 评价状态（1 已评、0 未评） |
| SCORE | 评价分值 | NUMBER(10,4) | 评分 |
| CONTENT | 建议意见 | VARCHAR2(64) | 建议意见 |

### HQ_JX_PJ_PJ

**业务概念**: 评教结果信息

**说明**: 

**字段列表**:

| 字段名 | 中文名 | 类型 | 说明 |
|--------|--------|------|------|
| ID | ID | VARCHAR2(64) | 主键，无特殊含义，唯一标识，不可重复； |
| OBJECT_TYPE_CODE | 评价对象类型 | VARCHAR2(64) | 评价对象类型 两种(课程节次表、教师) |
| OBJECT_ID | 评价对象ID | VARCHAR2(64) | 被评对象id(评价对象ID是节次课表ID（随堂评价）或教师ID(期中评价、期末评价、同行评价、督导评 |
| SCORE | 综合平均分 | NUMBER(10,4) | 平均分保留两位小数 |
| ASSESS_TYPE_CODE | 评价类型 | VARCHAR2(64) | 评价类型代码 学生评教（随堂评价、期中评价、期末评价）、教师评教（同行评价、督导评价、检查评价） |
| SCHOOL_YEAR | 学年 | VARCHAR2(64) | 学年 |
| TERM_CODE | 学期 | VARCHAR2(64) | 学期 |
| TEA_NO | 被评对象-教师 | VARCHAR2(64) | 评价对象：教师评价、教师课程评价;新增的字段【2022-01-13】 |
| COURSE_CODE | 被评对象-课程 | VARCHAR2(64) | 评价对象：教师课程评价;新增的字段【2022-01-13】 |
| TEACHCLASS_ID | 被评对象-教学班ID | VARCHAR2(256) | 评价对象：随堂评价;新增的字段【2022-01-13】 |
| WEEKS | 被评对象-上课周次（只有一周） | VARCHAR2(10) | 评价对象：随堂评价；值：1、2、5、9等任意周次;新增的字段【2022-01-13】 |
| DAY_OF_WEEK | 被评对象-上课星期 | NUMBER(1) | 评价对象：随堂评价；值：1、2、3、4、5、6、7;新增的字段【2022-01-13】 |
| PERIOD | 被评对象-上课节次 | VARCHAR2(10) | 评价对象：随堂评价；值：1-2、1-4、3-4……;新增的字段【2022-01-13】 |

### HQ_JX_PJ_XSPJ

**业务概念**: 学生评教（随堂评价、期中评价、期末评价）明细

**说明**: 随堂评价、期中评价、期末评价 明细

**字段列表**:

| 字段名 | 中文名 | 类型 | 说明 |
|--------|--------|------|------|
| ID | ID | VARCHAR2(64) | 主键，无特殊含义，唯一标识，不可重复； |
| RESULT_ID | 结果表ID | VARCHAR2(64) |  |
| ASSESS_PERSON_ID | 评价人ID | VARCHAR2(64) | 评价人（学生学号） |
| STATUS | 评价状态 | NUMBER(1) | 评价状态（1 已评、0 未评） |
| SCORE | 评价分值 | NUMBER(10,4) | 评分 |
| CONTENT | 建议意见 | VARCHAR2(64) | 建议意见 |

### HQ_JX_TEACHCLASS

**业务概念**: 教学班信息

**说明**: 由程序自动从课表解析生成，主要用于智慧课堂，专题分析等系统

**责任部门**: 教务处（通常来源教务系统）

**字段列表**:

| 字段名 | 中文名 | 类型 | 说明 |
|--------|--------|------|------|
| ID | ID | VARCHAR2(512) |  |
| CODE_ | 教学班编号 | VARCHAR2(512) |  |
| NAME_ | 教学班名称 | VARCHAR2(600) | 默认教务排课的上课班级，若有分组，则为“上课班级+分组名” |
| COURSE_CODE | 课程CODE | VARCHAR2(60) |  |
| SCHOOL_YEAR | 学年 | VARCHAR2(9) |  |
| TERM_CODE | 学期 | VARCHAR2(2) |  |
| ISTRUE | 是否可用 | NUMBER(1) |  |

### HQ_JX_TEACHCLASS_MAJOR

**业务概念**: 教学班所属的专业

**说明**: 由程序自动从课表解析生成，主要用于智慧课堂，专题分析等系统

**责任部门**: 教务处（通常来源教务系统）

**字段列表**:

| 字段名 | 中文名 | 类型 | 说明 |
|--------|--------|------|------|
| ID | ID | VARCHAR2(512) |  |
| TEACHCLASS_ID | 教学班ID | VARCHAR2(512) |  |
| MAJOR_CODE | 专业CODE | VARCHAR2(60) |  |
| SCHOOL_YEAR | 学年 | VARCHAR2(9) |  |
| TERM_CODE | 学期 | VARCHAR2(10) |  |
| YEAR_ | 年 | NUMBER(4) |  |
| ISTRUE | 是否可用 | NUMBER(1) |  |

### HQ_JX_TEACHCLASS_STU

**业务概念**: 教学班的上课学生

**说明**: 学生课程表信息，主要用于解析教学班-学生

**责任部门**: 教务处（通常来源教务系统）

**字段列表**:

| 字段名 | 中文名 | 类型 | 说明 |
|--------|--------|------|------|
| ID | ID | VARCHAR2(600) |  |
| SCHOOL_YEAR | 学年 | VARCHAR2(9) |  |
| TERM_CODE | 学期 | VARCHAR2(10) |  |
| COURSE_CODE | 课程CODE | VARCHAR2(60) |  |
| TEACHCLASS_NAME | 教学班名称 | VARCHAR2(600) | 默认教务排课的上课班级，若有分组，则为“上课班级+分组名” |
| TEACHCLASS_ID | 教学班ID | VARCHAR2(600) | 学年+学期+课程+教学班名称，程序的解析逻辑 |
| STU_NO | 学号 | VARCHAR2(60) |  |
| ISTRUE | 是否可用 | NUMBER(1) |  |

### HQ_JX_TEACHCLASS_TEA

**业务概念**: 教学班的授课教师

**说明**: 由程序自动从课表解析生成，主要用于智慧课堂，专题分析等系统

**责任部门**: 教务处（通常来源教务系统）

**字段列表**:

| 字段名 | 中文名 | 类型 | 说明 |
|--------|--------|------|------|
| ID | ID | VARCHAR2(512) |  |
| SCHOOL_YEAR | 学年 | VARCHAR2(9) |  |
| TERM_CODE | 学期 | VARCHAR2(2) |  |
| COURSE_CODE | 课程CODE | VARCHAR2(60) |  |
| TEACHCLASS_NAME | 教学班名称 | VARCHAR2(600) | 默认教务排课的上课班级，若有分组，则为“上课班级+分组名” |
| TEACHCLASS_ID | 教学班ID | VARCHAR2(600) | 学年+学期+课程+教学班名称，程序的解析逻辑 |
| TEA_NO | 职工号 | VARCHAR2(60) |  |
| ISTRUE | 是否可用 | NUMBER(1) |  |

### HQ_JX_TEACHCLASS_XZB

**业务概念**: 教学班所属的行政班

**说明**: 由程序自动从课表解析生成，主要用于人才培养等系统

**责任部门**: 教务处（通常来源教务系统）

**字段列表**:

| 字段名 | 中文名 | 类型 | 说明 |
|--------|--------|------|------|
| ID | ID | VARCHAR2(512) |  |
| TEACHCLASS_ID | 教学班ID | VARCHAR2(512) |  |
| CLASS_ID | 行政班代码 | VARCHAR2(60) |  |
| SCHOOL_YEAR | 学年 | VARCHAR2(9) |  |
| TERM_CODE | 学期 | VARCHAR2(10) |  |
| YEAR_ | 年 | NUMBER(4) |  |
| ISTRUE | 是否可用 | NUMBER(1) |  |

### HQ_OUT_MAJOR_RECORDS

**业务概念**: 专业备案信息

**说明**: 全部专业备案表，网上获取（爬虫），系统已经自动处理

**字段列表**:

| 字段名 | 中文名 | 类型 | 说明 |
|--------|--------|------|------|
| ID | ID | VARCHAR2(60) | 主键，唯一 |
| SCHOOL_CODE | 学校CODE | VARCHAR2(60) | 学校代码 |
| SCHOOL_NAME | 学校名称 | VARCHAR2(100) |  |
| MAJOR_CODE | 专业CODE | VARCHAR2(60) | 国标专业代码 |
| YEAR | 招生年份 | NUMBER(4) | 专业招生年份 |
| XYNX | 修业年限 | NUMBER(1) | 该专业的学生在校学习的年限，如：3 |

### HQ_RS_CHANGE

**业务概念**: 教职工的聘用状态变动记录

**说明**: 教职工的状态变动记录。状态包括：退休、离休、死亡、返聘、调出、辞职、离职、开除、下落不明、在职、延聘、待退休、长病假、因公出国、停薪留职、待岗、甚他

**注意事项**: 要求采集5年的变动数据

**责任部门**: 人事处（通常来源人事处）

**字段列表**:

| 字段名 | 中文名 | 类型 | 说明 |
|--------|--------|------|------|
| ID | ID | VARCHAR2(60) | 主键，无特殊含义，唯一标识，不可重复； |
| TEA_NO | 工号 | VARCHAR2(60) |  |
| TEA_STATUS_CHANGE_CODE | 变动类型 | VARCHAR2(60) | 退休；离职；返聘…… |
| DATE_ | 变动日期 | VARCHAR2(10) | 例：2019-10-10 |
| BZ | 备注 | VARCHAR2(200) |  |

### HQ_RS_EDU_DEGREE_CHANGE

**业务概念**: 教职工教育经历信息

**说明**: 教职工教育经历信息。用途：解析历年师资情况；影响：历年教师数据

**责任部门**: 人事处（通常来源人事处）

**字段列表**:

| 字段名 | 中文名 | 类型 | 说明 |
|--------|--------|------|------|
| ID | ID | VARCHAR2(60) | 主键，无特殊含义，唯一标识，不可重复； |
| TEA_NO | 工号 | VARCHAR2(60) |  |
| BEGIN_YEAR_MONTH | 开始年月 | VARCHAR2(7) | 例：2017-09 |
| END_YEAR_MONTH | 截止年月 | VARCHAR2(7) | 例：2019-07 |
| EDU_ID | 获得学历_ID | VARCHAR2(60) | 博士研究生：01，硕士研究生：10，本科：20，专科：30，中专：40，技工：50，高中，60（不可 |
| DEGREE_ID | 获得学位_ID | VARCHAR2(60) | 名誉博士：1，博士：2，硕士：3，学士：4，双学士：5（不可变更） |
| SCHOOL | 学校 | VARCHAR2(200) |  |
| MAJOR | 专业 | VARCHAR2(200) |  |
| NAME_ | 姓名 | VARCHAR2(60) |  |
| EDU_NATURE | 学历性质 | VARCHAR2(20) |  |
| LENGTH_SCHOOLING | 学制 | NUMBER(1) |  |
| AWARD_ORGAN_NAME | 授学位单位名称 | VARCHAR2(100) |  |
| AWARD_AREA | 授学位国家/地区 | VARCHAR2(100) |  |
| SUBJECT_CATEGORY_CODE | 学科门类 | VARCHAR2(20) |  |
| SCHOOL_TYPE_CODE | 院校类型 | VARCHAR2(20) |  |

### HQ_RS_FDYBZR

**业务概念**: 辅导员或班主任的任职信息

**说明**: 辅导员-班主任任职信息。用途：***；影响：***

**责任部门**: 学生处（通常来源学生处、学工系统、教务系统）

**字段列表**:

| 字段名 | 中文名 | 类型 | 说明 |
|--------|--------|------|------|
| ID | ID | VARCHAR2(60) | 主键，无特殊含义，唯一标识，不可重复； |
| TEA_NO | 工号 | VARCHAR2(60) |  |
| FDYBZR_CODE | 辅导员-班主任CODE | VARCHAR2(20) | 1：辅导员；2：班主任 |
| SCHOOL_YEAR | 学年 | VARCHAR2(10) | 例：2017-2018 |
| TERM_CODE | 学期 | VARCHAR2(10) | 01/02 |

### HQ_RS_FDYBZR_CLASS

**业务概念**: 辅导员或班主任所带班级

**说明**: 辅导员-班主任带班班级信息。用途：***；影响：***

**注意事项**: 学期中换班主任情况：根据学校实际数据记录，无需额外处理

**责任部门**: 学生处（通常来源学生处、学工系统、教务系统）

**字段列表**:

| 字段名 | 中文名 | 类型 | 说明 |
|--------|--------|------|------|
| ID | ID | VARCHAR2(60) | 主键，无特殊含义，唯一标识，不可重复； |
| FDYBZR_ID | 辅导员班主任表ID | VARCHAR2(60) |  |
| CLASS_ID | 班级ID | VARCHAR2(20) |  |

### HQ_RS_HONOR

**业务概念**: 教职工社会荣誉信息

**说明**: 教职工社会荣誉信息。用途：解析部门绩效考核；影响：内部质量核心绩效考核

**责任部门**: 党办（通常来源党办）

**字段列表**:

| 字段名 | 中文名 | 类型 | 说明 |
|--------|--------|------|------|
| ID | ID | VARCHAR2(60) | 主键，无特殊含义，唯一标识，不可重复； |
| DEPT_ID | 申报部门ID | VARCHAR2(60) | 对应：部门/院系/教学单位，行政组织结构表ID（HQ_CODE_DEPT） |
| JYS_ID | 教育教学部ID | VARCHAR2(60) |  |
| JX_NAME | 奖项名称 | VARCHAR2(200) |  |
| DATE_BEGIN | 开始时间 | VARCHAR2(10) | 例：2017-09-01 |
| DATE_END | 结束时间 | VARCHAR2(10) | 例：2018-09-01 |
| PRJG_NAME | 聘任机构 | VARCHAR2(200) |  |
| HONOR_PID_ID | 类别ID | VARCHAR2(60) | 专家库成员、学会或协会 |
| HONOR_ID | 类别子类ID | VARCHAR2(60) |  |
| HONOR_LEVEL_CODE | 社会荣誉级别CODE | VARCHAR2(60) | 1 国家级，2 省部级，3 市厅局级，4 院/校级，9 其他 |
| HJR_NO | 获奖人工号 | VARCHAR2(200) |  |
| HJR_NAME | 获奖人姓名 | VARCHAR2(200) |  |
| APPLY_BZ | 申报备注 | VARCHAR2(200) |  |
| AUDIT_BZ | 审核备注 | VARCHAR2(200) |  |
| BH | 成果编号 | VARCHAR2(60) | 学校用来唯一标识这个成果的编号 |
| YEAR_ | 数据归档年 | NUMBER(4) | 记录数据归档年 |

### HQ_RS_HONOR_RES

**业务概念**: 荣誉成果信息

**说明**: 教职工/部门荣誉成果信息。用途：解析部门绩效考核；影响：内部质量核心绩效考核

**注意事项**: 学校或部门或教职工获得的各项奖项荣誉，不包含教学类相关成果。

**字段列表**:

| 字段名 | 中文名 | 类型 | 说明 |
|--------|--------|------|------|
| ID | ID | VARCHAR2(60) | 主键，无特殊含义，唯一标识，不可重复； |
| DEPT_ID | 申报部门ID | VARCHAR2(60) | 对应：部门/院系/教学单位，行政组织结构表ID（HQ_CODE_DEPT） |
| JYS_ID | 教育教学部ID | VARCHAR2(60) |  |
| WEIGHT | 权重 | NUMBER(10,4) |  |
| JX_NAME | 奖项名称 | VARCHAR2(200) |  |
| DATE_ | 获奖时间 | VARCHAR2(10) | 例：2017-09-01 |
| RANKING | 位次 | VARCHAR2(60) | ？？ |
| FZDW_NAME | 发证单位 | VARCHAR2(200) |  |
| HONOR_RES_PID_ID | 奖项类别ID | VARCHAR2(60) | 表彰获奖个人奖、表彰获奖集体奖、综合获奖个人奖、综合获奖集体奖 |
| HONOR_RES_ID | 奖项级别ID | VARCHAR2(60) | 国家级A类…… |
| HJR_NO | 获奖人工号 | VARCHAR2(200) | 说明：是个人成果时这个字段有值 |
| HJR_NAME | 获奖人姓名 | VARCHAR2(200) | 说明：是个人成果时这个字段有值 |
| HJDW_NAME | 获奖单位 | VARCHAR2(200) | 说明：是部门成果时这个字段有值 |
| APPLY_BZ | 申报备注 | VARCHAR2(200) |  |
| AUDIT_BZ | 审核备注 | VARCHAR2(200) |  |
| BH | 成果编号 | VARCHAR2(60) | 学校用来唯一标识这个成果的编号 |
| YEAR_ | 数据归档年 | NUMBER(4) | 记录数据归档年 |

### HQ_RS_HONOR_RES_CY

**业务概念**: 荣誉成果中的成员

**说明**: 教职工/部门荣誉成果信息。用途：解析部门绩效考核；影响：内部质量核心绩效考核

**责任部门**: 党办（通常来源党办）

**字段列表**:

| 字段名 | 中文名 | 类型 | 说明 |
|--------|--------|------|------|
| ID | ID | VARCHAR2(512) | 主键，无特殊含义，唯一标识，不可重复； |
| HONOR_RES_ID | 荣誉成果ID | VARCHAR2(60) |  |
| PERSON_TYPE_CODE | 成员类型CODE | VARCHAR2(20) | 1（校内教师），2（校外人员），3（校内学生），4（机构/单位） |
| DEPT_ID | 教师部门ID | VARCHAR2(60) |  |
| TEA_NO | 工号 | VARCHAR2(60) | 如果成员类型是教师，则是教师工号 |
| MC | 名称 | VARCHAR2(60) | 如果成员类型是校外人员或者机构单位，则填写 人员或单位的名称；如果是老师或学生，则写老师或学生的名称 |
| STU_NO | 学号 | VARCHAR2(60) | 如果成员类型是学生，则填写学生学号 |
| ORDER_ | 排序 | NUMBER(4) |  |

### HQ_RS_HONOR_RES_JOINDEPT

**业务概念**: 荣誉成果中的参与部门

**说明**: 教职工/部门荣誉成果的参与部门。用途：解析部门绩效考核；影响：内部质量核心绩效考核

**责任部门**: 党办（通常来源党办）

**字段列表**:

| 字段名 | 中文名 | 类型 | 说明 |
|--------|--------|------|------|
| ID | ID | VARCHAR2(60) | 主键，无特殊含义，唯一标识，不可重复； |
| HONOR_RES_ID | 荣誉成果ID | VARCHAR2(60) |  |
| DEPT_ID | 参与部门ID | VARCHAR2(60) | 对应：部门/院系/教学单位，行政组织结构表ID（HQ_CODE_DEPT） |
| JYS_ID | 教育教学部ID | VARCHAR2(60) |  |
| WEIGHT | 权重 | NUMBER(10,4) |  |
| ORDER_ | 排序 | NUMBER(4) |  |

### HQ_RS_PHOTO

**业务概念**: 教职工照片信息

**说明**: 教师照片信息表

**注意事项**: 初期集成时直接讲照片拷贝到相关目录下，批量生成这个表的数据即可

**责任部门**: 组织人事处、信息中心部门，通常学校已有照片数据

**字段列表**:

| 字段名 | 中文名 | 类型 | 说明 |
|--------|--------|------|------|
| ID | ID | VARCHAR2(60) | 主键，唯一，通常取职工号 |
| TEA_NO | 职工号 | VARCHAR2(60) | 职工号，不可重复 |
| STORE_NAME | 存储名称 | VARCHAR2(100) | 例：***.jpg |
| FILE_TYPE | 照片类型 | VARCHAR2(10) | jpg/png…… |
| FILE_KB | 照片大小（KB） | NUMBER(20) |  |
| UNIQUE_ | 照片唯一标识码 | VARCHAR2(60) | 初期默认职工号
通过唯一标识码调用文件下载服务器地址，后期可以统一做处理
http://***/da |
| TIME_ | 更新时间 | VARCHAR2(20) | 例：yyyy-mm-dd hh:mm:ss |
| FILE_CONTENT | 照片内容 | BLOB | 照片二进制存储，通常用于对接【2021-06-17】 |

### HQ_RS_TAKE_OFFICE

**业务概念**: 教职工校内任职记录

**说明**: 教职工校内部门岗位任职记录。用途：解析历年各部门师资情况；影响：历年各部门教师数据

**责任部门**: 人事处（通常来源人事处）

**字段列表**:

| 字段名 | 中文名 | 类型 | 说明 |
|--------|--------|------|------|
| ID | ID | VARCHAR2(60) | 主键，无特殊含义，唯一标识，不可重复； |
| TEA_NO | 工号 | VARCHAR2(60) |  |
| BEGIN_YEAR_MONTH | 任职开始年月 | VARCHAR2(7) | 例：2017-09 |
| END_YEAR_MONTH | 任职截止年月 | VARCHAR2(7) | 例：2018-09 |
| DEPT_ID | 任职部门 | VARCHAR2(60) | 对应：行政组织结构表ID（HQ_CODE_DEPT） |
| KS_ID | 科室 | VARCHAR2(60) | 对应：行政组织结构表ID（HQ_CODE_DEPT） |
| ZW_NAME | 行政职务名称 | VARCHAR2(200) |  |

### HQ_RS_TEA

**业务概念**: 教职工基本信息

**说明**: 教职工个人当前最新的基本信息。用途：最基础、核心的数据，影响：系统无法运行

**注意事项**: 必须包含国标状态的所有教师数据，必须按国标状态存储教师状态信息

**责任部门**: 人事处（通常来源人事系统）

**字段列表**:

| 字段名 | 中文名 | 类型 | 说明 |
|--------|--------|------|------|
| ID | ID | VARCHAR2(60) | 主键，无特殊含义，唯一标识，不可重复； |
| ZZJG_ID | 组织机构ID | VARCHAR2(60) | 对应：行政组织结构表ID（HQ_CODE_DEPT），可能是科室、专业 |
| DEPT_ID | 所属部门 | VARCHAR2(60) | 对应：部门/院系/教学单位，行政组织结构表ID（HQ_CODE_DEPT）（教师不能隶属专业） |
| TEA_NO | 工号 | VARCHAR2(60) | 不能重复 |
| NAME_ | 姓名 | VARCHAR2(60) |  |
| TEA_STATUS_CODE | 教职工状态 | VARCHAR2(20) | 在职（11，含其他原因在岗人员）、延聘（12）、返聘（04）、退休（01）、离职（07）、其他（99 |
| JZGLB_CODE | 教职工类别 | VARCHAR2(20) | 校本部教职工（10）、科研机构人员（20）、校办企业职工（30）、其他附设机构人员（40）、聘请校外 |
| BZLB_CODE | 编制类别 | VARCHAR2(20) | 教学类（10）、行政类（20）、教辅类（30）、工勤类（40）、外聘教师类（80）、科研类（50）、 |
| BZLX_CODE | 编制类型 | VARCHAR2(20) | 在编（1）、人事代理（2）、劳务派遣（3）、其他（9）（行标、可新增、新增编码格式9**、三位数） |
| FORMER_NAME | 曾用名 | VARCHAR2(60) |  |
| SEX_CODE | 性别 | VARCHAR2(20) |  |
| ZWCC_CODE | 职务层次 | VARCHAR2(20) | 如：厅局级副职（代码122，表示学校领导）、县处级正职（代码131，代表部门负责人）、未定职（代码1 |
| ZWJB_CODE | 职务级别 | VARCHAR2(20) | 如：中层正职（代码3，不可变更，表示部门负责人）、中层副职（代码4，不可变更，代表部门负责人副职） |
| ZW_NAME | 行政职务 | VARCHAR2(200) |  |
| GZGWXZ_CODE | 工作岗位性质 | VARCHAR2(200) | 科研：1；教学：2；设计：3；管理：4（国标未完、可扩增校标） |
| JZGLY_CODE | 教职工来源 | VARCHAR2(200) | 录用应届毕业生：10；应届本科生：11；应届硕士生：12；应届博士生：13；其他进校人员：99（部标 |
| PLACE | 籍贯 | VARCHAR2(200) |  |
| NATION_CODE | 民族 | VARCHAR2(20) |  |
| POLITICS_CODE | 政治面貌 | VARCHAR2(20) |  |
| CJDPRQ_DATE | 参加党派时间 | VARCHAR2(10) |  |
| ... | 还有 75 个字段 | | |

### HQ_RS_TEACH_RES

**业务概念**: 教学成果信息

**说明**: 教职工/部门教学成果信息。用途：解析部门绩效考核；影响：内部质量核心绩效考核

**责任部门**: 教务处（通常来源教务处、教务系统）

**字段列表**:

| 字段名 | 中文名 | 类型 | 说明 |
|--------|--------|------|------|
| ID | ID | VARCHAR2(60) | 主键，无特殊含义，唯一标识，不可重复； |
| DEPT_ID | 申报部门ID | VARCHAR2(60) | 对应：部门/院系/教学单位，行政组织结构表ID（HQ_CODE_DEPT） |
| JYS_ID | 教育教学部ID | VARCHAR2(60) |  |
| WEIGHT | 权重 | NUMBER(10,4) |  |
| JX_NAME | 奖项名称 | VARCHAR2(200) |  |
| IS_SETUP | 是否立项 | VARCHAR2(60) | 1/0 |
| DATE_ | 获奖时间 | VARCHAR2(10) | 例：2017-09-01 |
| RANKING | 位次 | VARCHAR2(60) |  |
| SJDW_NAME | 授奖单位 | VARCHAR2(200) |  |
| TEACH_RES_PID_ID | 奖项类别ID | VARCHAR2(60) | 专业建设成果、教材、技能大赛及作品获奖、课题…… |
| TEACH_RES_ID | 细分类别ID | VARCHAR2(60) | 学生职业技能竞赛、教师技能大赛、信息化教学大赛、精品资源共享课…… |
| TEACH_RES_NAME | 细分类别名称 | VARCHAR2(60) |  |
| TEACH_RES_GRAND_ID | 奖项级别ID | VARCHAR2(60) | 国家级、一等奖…… |
| FZR_NO | 负责人工号 | VARCHAR2(60) |  |
| FZR_NAME | 负责人姓名 | VARCHAR2(60) |  |
| OTHER_NOS | 其他成员NOS | VARCHAR2(500) |  |
| OTHER_NAMES | 其他成员MCS | VARCHAR2(500) |  |
| BH | 成果编号 | VARCHAR2(200) | 学校用来唯一标识这个成果的编号 |
| HJR_NO | 获奖人工号 | VARCHAR2(200) |  |
| HJR_NAME | 获奖人姓名 | VARCHAR2(200) |  |
| ... | 还有 9 个字段 | | |

### HQ_RS_TEACH_RES_CY

**业务概念**: 教学成果中的成员

**说明**: 教职工/部门教学成果成员信息。用途：解析部门绩效考核；影响：内部质量核心绩效考核

**责任部门**: 党办（通常来源党办）

**字段列表**:

| 字段名 | 中文名 | 类型 | 说明 |
|--------|--------|------|------|
| ID | ID | VARCHAR2(512) | 主键，无特殊含义，唯一标识，不可重复； |
| TEACH_RES_ID | 荣誉成果ID | VARCHAR2(60) |  |
| PERSON_TYPE_CODE | 成员类型CODE | VARCHAR2(20) | 1（校内教师），2（校外人员），3（校内学生），4（机构/单位） |
| DEPT_ID | 教师部门ID | VARCHAR2(60) |  |
| TEA_NO | 工号 | VARCHAR2(60) | 如果成员类型是教师，则是教师工号 |
| MC | 名称 | VARCHAR2(60) | 如果成员类型是校外人员或者机构单位，则填写 人员或单位的名称；如果是老师或学生，则写老师或学生的名称 |
| STU_NO | 学号 | VARCHAR2(60) | 如果成员类型是学生，则填写学生学号 |
| ORDER_ | 排序 | NUMBER(4) |  |

### HQ_RS_TEACH_RES_JOINDEPT

**业务概念**: 教学成果中的参与部门

**说明**: 教职工/部门教学成果的参与部门。用途：解析部门绩效考核；影响：内部质量核心绩效考核

**责任部门**: 党办（通常来源党办）

**字段列表**:

| 字段名 | 中文名 | 类型 | 说明 |
|--------|--------|------|------|
| ID | ID | VARCHAR2(60) | 主键，无特殊含义，唯一标识，不可重复； |
| TEACH_RES_ID | 教学成果ID | VARCHAR2(60) |  |
| DEPT_ID | 参与部门ID | VARCHAR2(60) | 对应：部门/院系/教学单位，行政组织结构表ID（HQ_CODE_DEPT） |
| JYS_ID | 教育教学部ID | VARCHAR2(60) |  |
| WEIGHT | 权重 | NUMBER(10,4) |  |
| ORDER_ | 排序 | NUMBER(4) |  |

### HQ_RS_TEA_CONTRACT

**业务概念**: 合同信息

**说明**: 合同信息

**责任部门**: 人事处

**字段列表**:

| 字段名 | 中文名 | 类型 | 说明 |
|--------|--------|------|------|
| ID | ID | VARCHAR2(512) | 主键，无特殊含义，唯一标识，不可重复； |
| TEA_NO | 工号 | VARCHAR2(60) |  |
| NAME_ | 名称 | VARCHAR2(60) |  |
| CONTRACT_NO | 合同编号 | VARCHAR2(60) |  |
| CONTRACT_TYPE_CODE | 合同类型 | VARCHAR2(20) |  |
| BEGIN_DATE | 合同开始时间 | VARCHAR2(10) |  |
| END_DATE | 合同截止时间 | VARCHAR2(10) |  |
| CONTRACT_DEADLINE_TYPE_CODE | 合同期限类型 | VARCHAR2(20) |  |
| CONTRACT_IDENTIFICATION_CODE | 合同标识类型 | VARCHAR2(60) |  |
| CONTRACT_MONTH_COUNT | 合同月数 | NUMBER(2) |  |
| SIGN_DATE | 签订时间 | VARCHAR2(10) |  |
| DUTIES | 职责 | VARCHAR2(100) |  |

### HQ_RS_TEA_FAMILY

**业务概念**: 家庭成员信息

**说明**: 教职工家庭成员信息

**责任部门**: 人事处

**字段列表**:

| 字段名 | 中文名 | 类型 | 说明 |
|--------|--------|------|------|
| ID | ID | VARCHAR2(512) | 主键，无特殊含义，唯一标识，不可重复； |
| TEA_NO | 工号 | VARCHAR2(60) |  |
| RELATION | 与本人关系 | VARCHAR2(60) |  |
| NAME_ | 姓名 | VARCHAR2(60) |  |
| BIRTH_DATE | 出生日期 | VARCHAR2(10) |  |
| COMPANY_NAME | 工作单位 | VARCHAR2(200) |  |
| DUTIES | 职务 | VARCHAR2(200) |  |
| POLITICS_CODE | 政治面貌 | VARCHAR2(20) |  |

### HQ_RS_TEA_MAJOR_XN

**业务概念**: 每个专业各学年的任职教职工

**说明**: 每个专业各个学年的教职工数据。用途：方便的提取专业下的教师，影响：指标计算

**注意事项**: 教学类教师从课表提取，行政管理类暂放

**责任部门**: 教务处（通常来源教务系统）

**字段列表**:

| 字段名 | 中文名 | 类型 | 说明 |
|--------|--------|------|------|
| ID | ID | VARCHAR2(60) | 主键，无特殊含义，唯一标识，不可重复； |
| MAJOR_CODE | 专业代码 | VARCHAR2(60) | 对应：专业表代码或组织机构表专业代码 |
| TEA_NO | 工号 | VARCHAR2(60) |  |
| IS_TEACH | 是教学类 | NUMBER(1) | 1：是；0：否 |
| IS_DEPT | 是行政类 | NUMBER(1) | 1：是；0：否 |
| SCHOOL_YEAR | 学年 | VARCHAR2(20) | 例：2019-2020 |

### HQ_RS_TEA_MAJOR_YEAR

**业务概念**: 每个专业历年的任职教职工

**说明**: 每个专业历年的教职工数据。用途：方便的提取专业下的教师，影响：指标计算

**注意事项**: 教学类教师从课表提取，行政管理类暂放

**责任部门**: 教务处（通常来源教务系统）

**字段列表**:

| 字段名 | 中文名 | 类型 | 说明 |
|--------|--------|------|------|
| ID | ID | VARCHAR2(60) | 主键，无特殊含义，唯一标识，不可重复； |
| MAJOR_CODE | 专业代码 | VARCHAR2(60) | 对应：专业表代码或组织机构表专业代码 |
| TEA_NO | 工号 | VARCHAR2(60) |  |
| IS_TEACH | 是教学类 | NUMBER(1) | 1：是；0：否 |
| IS_DEPT | 是行政类 | NUMBER(1) | 1：是；0：否 |
| YEAR_ | 自然年 | VARCHAR2(20) | 例：2019 |

### HQ_RS_TEA_XQ

**业务概念**: 每学期的教职工基本信息

**说明**: 教职工个人学期备份信息。用途：最基础、核心的数据，影响：系统无法运行

**注意事项**: 必须包含国标状态的所有教师数据，必须按国标状态存储教师状态信息，必须保证有10个学期数据

**责任部门**: 人事处（通常来源人事系统）

**字段列表**:

| 字段名 | 中文名 | 类型 | 说明 |
|--------|--------|------|------|
| ID | ID | VARCHAR2(60) | 主键，无特殊含义，唯一标识，不可重复； |
| ZZJG_ID | 组织机构ID | VARCHAR2(60) | 对应：行政组织结构表ID（HQ_CODE_DEPT），可能是科室、专业 |
| DEPT_ID | 所属部门 | VARCHAR2(60) | 对应：部门/院系/教学单位，行政组织结构表ID（HQ_CODE_DEPT）（教师不能隶属专业） |
| TEA_NO | 工号 | VARCHAR2(60) | 不能重复 |
| NAME_ | 姓名 | VARCHAR2(60) |  |
| TEA_STATUS_CODE | 教职工状态 | VARCHAR2(20) | 在职（11，含其他原因在岗人员）、延聘（12）、返聘（04）、退休（01）、离职（07）、其他（99 |
| JZGLB_CODE | 教职工类别 | VARCHAR2(20) | 校本部教职工（10）、科研机构人员（20）、校办企业职工（30）、其他附设机构人员（40）、聘请校外 |
| BZLB_CODE | 编制类别 | VARCHAR2(20) | 教学类（10）、行政类（20）、教辅类（30）、工勤类（40）、外聘教师类（80）、科研类（50）、 |
| BZLX_CODE | 编制类型 | VARCHAR2(20) | 在编（1）、人事代理（2）、劳务派遣（3）、其他（9）（行标、可新增、新增编码格式9**、三位数） |
| FORMER_NAME | 曾用名 | VARCHAR2(60) |  |
| SEX_CODE | 性别 | VARCHAR2(20) |  |
| ZWCC_CODE | 职务层次 | VARCHAR2(20) | 如：厅局级副职（代码122，表示学校领导）、县处级正职（代码131，代表部门负责人）、未定职（代码1 |
| ZWJB_CODE | 职务级别 | VARCHAR2(20) | 如：中层正职（代码3，不可变更，表示部门负责人）、中层副职（代码4，不可变更，代表部门负责人副职） |
| ZW_NAME | 行政职务 | VARCHAR2(200) |  |
| GZGWXZ_CODE | 工作岗位性质 | VARCHAR2(200) | 科研：1；教学：2；设计：3；管理：4（国标未完、可扩增校标） |
| JZGLY_CODE | 教职工来源 | VARCHAR2(200) | 录用应届毕业生：10；应届本科生：11；应届硕士生：12；应届博士生：13；其他进校人员：99（部标 |
| PLACE | 籍贯 | VARCHAR2(200) |  |
| NATION_CODE | 民族 | VARCHAR2(20) |  |
| POLITICS_CODE | 政治面貌 | VARCHAR2(20) |  |
| CJDPRQ_DATE | 参加党派时间 | VARCHAR2(10) |  |
| ... | 还有 77 个字段 | | |

### HQ_RS_TEA_YEAR

**业务概念**: 每年的教职工基本信息

**说明**: 教职工个人年度备份信息。用途：最基础、核心的数据，影响：系统无法运行

**注意事项**: 必须包含国标状态的所有教师数据，必须按国标状态存储教师状态信息，必须保证有5年数据

**责任部门**: 人事处（通常来源人事系统）

**字段列表**:

| 字段名 | 中文名 | 类型 | 说明 |
|--------|--------|------|------|
| ID | ID | VARCHAR2(60) | 主键，无特殊含义，唯一标识，不可重复； |
| ZZJG_ID | 组织机构ID | VARCHAR2(60) | 对应：行政组织结构表ID（HQ_CODE_DEPT），可能是科室、专业 |
| DEPT_ID | 所属部门 | VARCHAR2(60) | 对应：部门/院系/教学单位，行政组织结构表ID（HQ_CODE_DEPT）（教师不能隶属专业） |
| TEA_NO | 工号 | VARCHAR2(60) | 不能重复 |
| NAME_ | 姓名 | VARCHAR2(60) |  |
| TEA_STATUS_CODE | 教职工状态 | VARCHAR2(20) | 在职（11，含其他原因在岗人员）、延聘（12）、返聘（04）、退休（01）、离职（07）、其他（99 |
| JZGLB_CODE | 教职工类别 | VARCHAR2(20) | 校本部教职工（10）、科研机构人员（20）、校办企业职工（30）、其他附设机构人员（40）、聘请校外 |
| BZLB_CODE | 编制类别 | VARCHAR2(20) | 教学类（10）、行政类（20）、教辅类（30）、工勤类（40）、外聘教师类（80）、科研类（50）、 |
| BZLX_CODE | 编制类型 | VARCHAR2(20) | 在编（1）、人事代理（2）、劳务派遣（3）、其他（9）（行标、可新增、新增编码格式9**、三位数） |
| FORMER_NAME | 曾用名 | VARCHAR2(60) |  |
| SEX_CODE | 性别 | VARCHAR2(20) |  |
| ZWCC_CODE | 职务层次 | VARCHAR2(20) | 如：厅局级副职（代码122，表示学校领导）、县处级正职（代码131，代表部门负责人）、未定职（代码1 |
| ZWJB_CODE | 职务级别 | VARCHAR2(20) | 如：中层正职（代码3，不可变更，表示部门负责人）、中层副职（代码4，不可变更，代表部门负责人副职） |
| ZW_NAME | 行政职务 | VARCHAR2(200) |  |
| GZGWXZ_CODE | 工作岗位性质 | VARCHAR2(200) | 科研：1；教学：2；设计：3；管理：4（国标未完、可扩增校标） |
| JZGLY_CODE | 教职工来源 | VARCHAR2(200) | 录用应届毕业生：10；应届本科生：11；应届硕士生：12；应届博士生：13；其他进校人员：99（部标 |
| PLACE | 籍贯 | VARCHAR2(200) |  |
| NATION_CODE | 民族 | VARCHAR2(20) |  |
| POLITICS_CODE | 政治面貌 | VARCHAR2(20) |  |
| CJDPRQ_DATE | 参加党派时间 | VARCHAR2(10) |  |
| ... | 还有 76 个字段 | | |

### HQ_RS_YPFP

**业务概念**: 教职工延聘返聘记录

**说明**: 教职工的延聘返聘记录。用途：解析历年师资情况；影响：历年教师数据

**责任部门**: 人事处（通常来源人事处）

**字段列表**:

| 字段名 | 中文名 | 类型 | 说明 |
|--------|--------|------|------|
| ID | ID | VARCHAR2(60) | 主键，无特殊含义，唯一标识，不可重复； |
| TEA_NO | 工号 | VARCHAR2(60) |  |
| YPFP_CODE | 延聘返聘类型 | VARCHAR2(60) | 延聘：12；返聘：4 |
| BEGIN_DATE | 开始日期 | VARCHAR2(10) | 例：2019-10-10 |
| END_DATE | 结束日期 | VARCHAR2(10) | 例：2019-10-10 |
| BZ | 备注 | VARCHAR2(200) |  |

### HQ_RS_ZYJSZW_CHANGE

**业务概念**: 教职工职称评定信息

**说明**: 教职工职称评定信息。用途：解析历年师资情况；影响：历年教师数据

**责任部门**: 人事处（通常来源人事处）

**字段列表**:

| 字段名 | 中文名 | 类型 | 说明 |
|--------|--------|------|------|
| ID | ID | VARCHAR2(60) | 主键，无特殊含义，唯一标识，不可重复； |
| TEA_NO | 工号 | VARCHAR2(60) |  |
| ZYJSZW_ID | 职称_ID | VARCHAR2(20) | 如：教授、副教授、高级实验师、实验师、经济师、助理经济师…… |
| YEAR_MONTH | 评定年月 | VARCHAR2(7) | 例：2017-09 |
| END_YEAR_MONTH | 首次聘任年月 | VARCHAR2(7) | 例：2018-07 |
| ZYJSZW_JB_CODE | 专业技术职务级别 | VARCHAR2(20) | 正高级/副高级/中级/初级/员级/未定职级专业技术人员 |
| NAME_ | 姓名 | VARCHAR2(60) |  |

### HQ_XS_CHANGE

**业务概念**: 学生学籍异动信息

**说明**: 学籍异动信息

**注意事项**: 要求采集3年异动数据

**责任部门**: 学籍管理部门

**字段列表**:

| 字段名 | 中文名 | 类型 | 说明 |
|--------|--------|------|------|
| ID | ID | VARCHAR2(64) | 主键，唯一 |
| STU_NO | 学号 | VARCHAR2(64) | 学号 |
| STU_CHANGE_CODE | 异动类别_CODE | VARCHAR2(20) | 学籍异动类别代码 |
| CHANGE_REASON_CODE | 异动原因_CODE | VARCHAR2(20) | 学籍异动原因代码 |
| SCHOOL_YEAR | 学年 | VARCHAR2(9) | 异动学年 |
| TERM_CODE | 学期 | VARCHAR2(10) | 异动学期 |
| DATE_ | 异动日期 | VARCHAR2(10) | 异动日期，yyyy-mm-dd 如：2019-06-17 |
| SP_DATE | 审批日期 | VARCHAR2(10) | 审批日期，yyyy-mm-dd 如：2019-06-17 |
| SPWH | 审批文号 | VARCHAR2(60) | 异动审批文号 |
| OLD_SCHOOL | 原学校 | VARCHAR2(60) | 异动前的学校名称 |
| OLD_DEPT_ID | 原院系 | VARCHAR2(20) | 异动前的院系代码 |
| OLD_MAJOR_CODE | 原专业 | VARCHAR2(20) | 异动前的专业代码 |
| OLD_CLASS_ID | 原班级 | VARCHAR2(20) | 异动前的班级代码 |
| OLD_GRADE | 原年级 | VARCHAR2(4) | 异动前所在年级 |
| OLD_XZ | 原学制 | NUMBER(1) | 异动前的学制 |
| NOW_SCHOOL | 现学校 | VARCHAR2(60) | 异动后的学校名称 |
| NOW_DEPT_ID | 现院系 | VARCHAR2(20) | 异动后的院系代码 |
| NOW_MAJOR_CODE | 现专业 | VARCHAR2(20) | 异动后的专业代码 |
| NOW_CLASS_ID | 现班级 | VARCHAR2(20) | 异动后的班级代码 |
| NOW_GRADE | 现年级 | VARCHAR2(4) | 异动后所在年级 |
| ... | 还有 7 个字段 | | |

### HQ_XS_PHOTO

**业务概念**: 学生照片信息

**说明**: 学生照片信息表

**注意事项**: 初期集成时直接讲照片拷贝到相关目录下，批量生成这个表的数据即可

**责任部门**: 学籍、信息中心部门，通常学校已有照片数据

**字段列表**:

| 字段名 | 中文名 | 类型 | 说明 |
|--------|--------|------|------|
| ID | ID | VARCHAR2(60) | 主键，唯一，通常取学号 |
| STU_NO | 学号 | VARCHAR2(60) | 学号，不可重复 |
| STORE_NAME | 存储名称 | VARCHAR2(100) | 例：***.jpg |
| FILE_TYPE | 照片类型 | VARCHAR2(10) | jpg/png…… |
| FILE_KB | 照片大小（KB） | NUMBER(20) |  |
| UNIQUE_ | 照片唯一标识码 | VARCHAR2(60) | 初期默认学号
通过唯一标识码调用文件下载服务器地址，后期可以统一做处理
http://***/dat |
| TIME_ | 更新时间 | VARCHAR2(20) | 例：yyyy-mm-dd hh:mm:ss |
| FILE_CONTENT | 照片内容 | BLOB | 照片二进制存储，通常用于对接【2021-06-17】 |

### HQ_XS_STU

**业务概念**: 学生基本信息

**说明**: 学生基本信息，系统运行的基础，同时作为用户信息

**责任部门**: 学籍部门，根据学校管理方式不一样，学籍管理也有所不同，有的在教务处，有的在学生处，有的在招生处，需要先明确学籍管理部门

**字段列表**:

| 字段名 | 中文名 | 类型 | 说明 |
|--------|--------|------|------|
| ID | ID | VARCHAR2(20) | 主键，唯一，通常取学号 |
| STU_NO | 学号 | VARCHAR2(60) | 学号，不可重复 |
| NAME_ | 姓名 | VARCHAR2(60) |  |
| FORMER_NAME | 曾用名 | VARCHAR2(60) |  |
| DEPT_ID | 院系ID | VARCHAR2(60) | 所属院系代码 |
| MAJOR_CODE | 专业ID | VARCHAR2(60) | 所属专业代码 |
| CLASS_ID | 班级ID | VARCHAR2(512) | 所属班级代码 |
| PINYIN | 拼音 | VARCHAR2(512) | 姓名简拼 |
| BIRTHDAY | 出生日期 | VARCHAR2(10) | 出生日期，格式：2019-06-17 |
| IDNO | 身份证号 | VARCHAR2(30) |  |
| SEX_CODE | 性别CODE | VARCHAR2(10) | 1：男，2：女 |
| NATION_CODE | 民族CODE | VARCHAR2(10) | 国标民族代码 |
| POLITICS_CODE | 政治面貌CODE | VARCHAR2(10) |  |
| ANMELDEN_CODE | 户口性质CODE | VARCHAR2(10) | 1：农村,2：县镇,3：城市 |
| LENGTH_SCHOOLING | 学制 | NUMBER(1) | 就读专业的学习年限 |
| PYCC_CODE | 培养层次CODE | VARCHAR2(60) | 1：博士；2：硕士；3：本科；4：专科；9：其他（不可变更） |
| RECRUIT_CODE | 招生方式_CODE | VARCHAR2(10) | 高职类：1：基于高考的"知识+技能"招生，2：对口招生，3：单独考试招生，4：综合评价招生，5：中高 |
| STU_FROM_CODE | 生源类型_CODE | VARCHAR2(10) | 高职类：1：普通高中生，2：三校生，3：3+2，4：五年制高职第4学年，5：其他；
中职类：11：本 |
| ENROLL_DATE | 入学日期 | VARCHAR2(10) | 入学日期，yyyy-mm，如：2018-09-01 |
| ENROLL_GRADE | 入学年级 | NUMBER(4) | 入学时所在年级，如：2018 |
| ... | 还有 35 个字段 | | |

### HQ_XS_STU_XQ

**业务概念**: 每学期的学生基本信息

**说明**: 学生基本信息，系统运行的基础，同时作为用户信息

**责任部门**: 学籍部门，根据学校管理方式不一样，学籍管理也有所不同，有的在教务处，有的在学生处，有的在招生处，需要先明确学籍管理部门

**字段列表**:

| 字段名 | 中文名 | 类型 | 说明 |
|--------|--------|------|------|
| ID | ID | VARCHAR2(20) | 主键，唯一，通常取学号 |
| STU_NO | 学号 | VARCHAR2(60) | 学号，不可重复 |
| NAME_ | 姓名 | VARCHAR2(60) |  |
| FORMER_NAME | 曾用名 | VARCHAR2(60) |  |
| DEPT_ID | 院系ID | VARCHAR2(60) | 所属院系代码 |
| MAJOR_CODE | 专业ID | VARCHAR2(60) | 所属专业代码 |
| CLASS_ID | 班级ID | VARCHAR2(512) | 所属班级代码 |
| PINYIN | 拼音 | VARCHAR2(512) | 姓名简拼 |
| BIRTHDAY | 出生日期 | VARCHAR2(10) | 出生日期，格式：2019-06-17 |
| IDNO | 身份证号 | VARCHAR2(18) |  |
| SEX_CODE | 性别CODE | VARCHAR2(10) | 1：男，2：女 |
| NATION_CODE | 民族CODE | VARCHAR2(10) | 国标民族代码 |
| POLITICS_CODE | 政治面貌CODE | VARCHAR2(10) |  |
| ANMELDEN_CODE | 户口性质CODE | VARCHAR2(10) | 1：农村,2：县镇,3：城市 |
| LENGTH_SCHOOLING | 学制 | NUMBER(1) | 就读专业的学习年限 |
| PYCC_CODE | 培养层次CODE | VARCHAR2(60) | 1：博士；2：硕士；3：本科；4：专科；9：其他（不可变更） |
| RECRUIT_CODE | 招生方式_CODE | VARCHAR2(10) | 高职类：1：基于高考的"知识+技能"招生，2：对口招生，3：单独考试招生，4：综合评价招生，5：中高 |
| STU_FROM_CODE | 生源类型_CODE | VARCHAR2(10) | 高职类：1：普通高中生，2：三校生，3：3+2，4：五年制高职第4学年，5：其他；
中职类：11：本 |
| ENROLL_DATE | 入学日期 | VARCHAR2(10) | 入学日期，yyyy-mm，如：2018-09-01 |
| ENROLL_GRADE | 入学年级 | NUMBER(4) | 入学时所在年级，如：2018 |
| ... | 还有 37 个字段 | | |

### HQ_XS_STU_YEAR

**业务概念**: 每年的学生基本信息

**说明**: 学生基本信息，系统运行的基础，同时作为用户信息

**责任部门**: 学籍部门，根据学校管理方式不一样，学籍管理也有所不同，有的在教务处，有的在学生处，有的在招生处，需要先明确学籍管理部门

**字段列表**:

| 字段名 | 中文名 | 类型 | 说明 |
|--------|--------|------|------|
| ID | ID | VARCHAR2(20) | 主键，唯一，通常取学号 |
| STU_NO | 学号 | VARCHAR2(60) | 学号，不可重复 |
| NAME_ | 姓名 | VARCHAR2(60) |  |
| FORMER_NAME | 曾用名 | VARCHAR2(60) |  |
| DEPT_ID | 院系ID | VARCHAR2(60) | 所属院系代码 |
| MAJOR_CODE | 专业ID | VARCHAR2(60) | 所属专业代码 |
| CLASS_ID | 班级ID | VARCHAR2(512) | 所属班级代码 |
| PINYIN | 拼音 | VARCHAR2(512) | 姓名简拼 |
| BIRTHDAY | 出生日期 | VARCHAR2(10) | 出生日期，格式：2019-06-17 |
| IDNO | 身份证号 | VARCHAR2(18) |  |
| SEX_CODE | 性别CODE | VARCHAR2(10) | 1：男，2：女 |
| NATION_CODE | 民族CODE | VARCHAR2(10) | 国标民族代码 |
| POLITICS_CODE | 政治面貌CODE | VARCHAR2(10) |  |
| ANMELDEN_CODE | 户口性质CODE | VARCHAR2(10) | 1：农村,2：县镇,3：城市 |
| LENGTH_SCHOOLING | 学制 | NUMBER(1) | 就读专业的学习年限 |
| PYCC_CODE | 培养层次CODE | VARCHAR2(60) | 1：博士；2：硕士；3：本科；4：专科；9：其他（不可变更） |
| RECRUIT_CODE | 招生方式_CODE | VARCHAR2(10) | 高职类：1：基于高考的"知识+技能"招生，2：对口招生，3：单独考试招生，4：综合评价招生，5：中高 |
| STU_FROM_CODE | 生源类型_CODE | VARCHAR2(10) | 高职类：1：普通高中生，2：三校生，3：3+2，4：五年制高职第4学年，5：其他；
中职类：11：本 |
| ENROLL_DATE | 入学日期 | VARCHAR2(10) | 入学日期，yyyy-mm，如：2018-09-01 |
| ENROLL_GRADE | 入学年级 | NUMBER(4) | 入学时所在年级，如：2018 |
| ... | 还有 36 个字段 | | |

### HQ_XS_STU_ZHCP_CPCJ

**业务概念**: 学生综合测评的各类型的得分

**说明**: 学生综合测评按类型得分汇总

**责任部门**: 学工处

**字段列表**:

| 字段名 | 中文名 | 类型 | 说明 |
|--------|--------|------|------|
| ID | ID | VARCHAR2(100) | 主键，唯一 |
| STU_NO | 学号 | VARCHAR2(60) | 学号 |
| SCHOOL_YEAR | 学年 | VARCHAR2(20) | 学年，2018-2019 |
| TERM_CODE | 学期 | VARCHAR2(20) | 学期，01：第一学期，02：第二学期 |
| SCORE | 总分 | VARCHAR2(20) | 对应测评类型的总分 |
| BASE_SCORE | 基础分 | VARCHAR2(20) | 对应测评类型的基础分 |
| ADD_SCORE | 奖励分 | VARCHAR2(20) | 对应测评类型的奖励分 |
| SUB_SCORE | 扣分 | VARCHAR2(20) | 对应测评类型的扣分 |
| CPLX_ID | 测评类型代码 | VARCHAR2(20) | 测评类型代码 |

### HQ_XS_STU_ZHCP_CPLX

**业务概念**: 学生综合测评的测评类型

**说明**: 综合测评的类型，可为树状。（如：思想政治，科学文化素质等等）

**责任部门**: 学工处

**字段列表**:

| 字段名 | 中文名 | 类型 | 说明 |
|--------|--------|------|------|
| ID | ID | VARCHAR2(60) | 主键，唯一 |
| CODE_ | 测评类型代码 | VARCHAR2(60) | 不能重复，通常与ID一致 |
| NAME_ | 测评类型名称 | VARCHAR2(100) |  |
| LEVEL_ | 层次 | number(1) | 1/2/3/... |
| LEVEL_TYPE | 层次类型 | VARCHAR2(100) |  |
| PID | 父节点 | VARCHAR2(60) | 上级类型ID |
| PATH_ | 全析码 | VARCHAR2(512) | 0001/00010001 |
| ISTRUE | 是否可用 | number(1) |  |
| WEIGHT | 权重 | number(2) | 类型在总分汇总时所占比重 |

### HQ_XS_STU_ZHCP_JJFGZ

**业务概念**: 学生综合测评的评分规则

**说明**: 综合测评加减分具体项目的信息，如：拾金不昧，加10分；迟到，减2分等

**责任部门**: 学工处

**字段列表**:

| 字段名 | 中文名 | 类型 | 说明 |
|--------|--------|------|------|
| ID | ID | VARCHAR2(100) |  |
| CODE_ | 规则代码 | VARCHAR2(20) |  |
| CPLX_ID | 测评类型代码 | VARCHAR2(60) | 测评类型表ID |
| CONTENT | 测评内容 | VARCHAR2(100) |  |
| DEPT_ID | 提交单位 | VARCHAR2(60) | 提交该规则的单位，或者需要审核该规则的单位，通常为学工处 |
| SCORE | 分值 | NUMBER(8,2) | 加分为正数，扣分为负数 |
| ISADD | 加减分标识 | NUMBER(1) | 1：是，0：否 |
| ISTRUE | 状态 | NUMBER(1) | 1：是，0：否 |

### HQ_XS_STU_ZHCP_JJFSJ

**业务概念**: 学生综合测评的加减分明细

**说明**: 综合测评学生加减分项目明细列表

**责任部门**: 学工处

**字段列表**:

| 字段名 | 中文名 | 类型 | 说明 |
|--------|--------|------|------|
| ID | ID | VARCHAR2(100) |  |
| STU_NO | 学号 | VARCHAR2(60) |  |
| JJFGZ_ID | 项目编号 | VARCHAR2(60) | 关联加减分规则表code_字段 |
| CONTENT | 活动内容 | VARCHAR2(200) |  |
| SCORE | 分数 | NUMBER(8,2) |  |
| GRADE | 年级 | NUMBER(4) | 学生所在年级 |
| SCHOOL_YEAR | 学年 | VARCHAR2(9) |  |
| TERM_CODE | 学期 | VARCHAR2(10) |  |
| TIME_ | 时间 | VARCHAR2(20) | yyyy-mm-dd hh24:mi:ss |

### HQ_XS_STU_ZHCP_ZHCJ

**业务概念**: 学生综合测评的总成绩

**说明**: 学生综合测评的总成绩

**责任部门**: 学工处

**字段列表**:

| 字段名 | 中文名 | 类型 | 说明 |
|--------|--------|------|------|
| ID | ID | VARCHAR2(60) | 主键，唯一 |
| STU_NO | 学号 | VARCHAR2(60) | 学号 |
| SCHOOL_YEAR | 学年 | VARCHAR2(20) |  |
| TERM_CODE | 学期 | VARCHAR2(20) |  |
| SCORE | 综合成绩 | number(8,2) | 总分 |

