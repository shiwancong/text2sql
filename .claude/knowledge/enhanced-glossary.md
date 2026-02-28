# 增强版业务术语映射表

## 核心实体映射

### 学校相关
| 用户表达 | 表名 | 字段 | 说明 |
|----------|------|------|------|
| 我校/学校/本校 | HQ_JC_XX | - | 学校基本信息 |
| 网址/域名/校园网 | HQ_JC_XX | DOMAIN | 学校网址 |
| 性质/类别/类型 | HQ_JC_XX | XX_XZLB_CODE | 行政类别 |
| 办学类型 | HQ_JC_XX | XX_BXLX_CODE | 办学类型代码 |
| 地址/所在地 | HQ_JC_XX | ADDRESS | 学校地址 |
| 简称/校名 | HQ_JC_XX | SHORT_NAME | 学校简称 |

### 教师相关
| 用户表达 | 表名 | 字段 | 说明 |
|----------|------|------|------|
| 教师/教工/老师 | HQ_RS_TEA | - | 教师信息 |
| 工号/教工号 | HQ_RS_TEA | TEA_NO | 教师编号 |
| 籍贯/家乡 | HQ_RS_TEA | PLACE | 教师籍贯 |
| 职称/职务 | HQ_RS_TEA | ZW_NAME | 职务名称 |
| 双师型/双师 | HQ_RS_TEA | IS_SSJS | 是否双师型(1是0否) |
| 电话/联系方式 | HQ_RS_TEA | PHONE | 联系电话 |
| 学历/学位 | HQ_RS_TEA | EDU_ID, DEGREE_ID | 学历学位ID |
| 入职时间 | HQ_RS_TEA | IN_DATE | 入职日期 |
| 参加工作时间 | HQ_RS_TEA | WORK_DATE | 工作起始日期 |
| 专业技术职务 | HQ_RS_TEA | ZYJSZW_ID | 专业技术职务代码 |

### 部门组织相关
| 用户表达 | 表名 | 字段 | 说明 |
|----------|------|------|------|
| 部门/单位/组织 | HQ_CODE_DEPT | - | 组织机构表 |
| 院系/学院 | HQ_CODE_DEPT | LEVEL_TYPE='YX' | 筛选院系 |
| 处室/行政部门 | HQ_CODE_DEPT | LEVEL_TYPE='BM' | 筛选行政部门 |
| 教研室/教学部 | HQ_CODE_DEPT_JYS | - | 教研室表 |
| 归属/隶属于/属于 | HQ_CODE_DEPT | PID | 上级部门ID |
| 部门负责人 | HQ_CODE_DEPT | FZR_NO | 负责人工号 |

### 专业相关
| 用户表达 | 表名 | 字段 | 说明 |
|----------|------|------|------|
| 专业 | HQ_CODE_MAJOR | - | 专业信息表 |
| 专业名称 | HQ_CODE_MAJOR | NAME_ | 专业名称 |
| 专业代码 | HQ_CODE_MAJOR | CODE_ | 专业代码 |
| 专业负责人 | HQ_CODE_MAJOR | FZR_NO | 专业负责人工号 |
| 专业带头人 | HQ_CODE_MAJOR | DTR_IN_NAMES | 校内带头人 |
| 国标专业 | HQ_CODE_MAJOR_MAPPER | GB_MAJOR_NAME | 国标专业名称 |
| 专业类别 | HQ_CODE_MAJOR | ZYFL_CODE | 专业分类(本科/专科) |

### 班级相关
| 用户表达 | 表名 | 字段 | 说明 |
|----------|------|------|------|
| 班级 | HQ_CODE_CLASSES | - | 班级信息表 |
| 班级ID | HQ_CODE_CLASSES | ID/NO_ | 班级编号 |
| 班级名称 | HQ_CODE_CLASSES | NAME_ | 班级名称 |
| 培养层次/办学层次 | HQ_CODE_CLASSES | PYCC_CODE | 1博士2硕士3本科4专科 |
| 所属院系/专业 | HQ_CODE_CLASSES | DEPT_ID, MAJOR_CODE | 关联字段 |

### 课程相关
| 用户表达 | 表名 | 字段 | 说明 |
|----------|------|------|------|
| 课程/科目 | HQ_CODE_COURSE | - | 课程基本信息 |
| 课程名称 | HQ_CODE_COURSE | NAME_ | 课程名称 |
| 课程代码 | HQ_CODE_COURSE | CODE_ | 课程代码 |
| 课程表/排课 | HQ_JX_KCB | - | 排课信息 |
| 授课教师/任课教师 | HQ_JX_KCB_TEA | TEA_NO | 教师工号 |
| 教学班/课头 | HQ_JX_TEACHCLASS | - | 教学班信息 |

### 代码值映射

#### 培养层次 (PYCC_CODE)
| 代码 | 名称 | 说明 |
|------|------|------|
| 1 | 博士 | 博士研究生 |
| 2 | 硕士 | 硕士研究生 |
| 3 | 本科 | 本科生 |
| 4 | 专科 | 专科/高职 |
| 9 | 其他 | 其他层次 |

#### 行政类别 (XX_XZLB_CODE)
| 代码 | 名称 |
|------|------|
| 01 | 综合大学 |
| 02 | 理工院校 |
| 03 | 农业院校 |
| 04 | 林业院校 |
| 05 | 医药院校 |
| 06 | 师范院校 |
| 07 | 语文院校 |
| 08 | 财经院校 |
| 09 | 政法院校 |
| 10 | 艺术院校 |
| 11 | 民族院校 |
| 12 | 体育院校 |

#### 性别 (SEX_CODE)
| 代码 | 名称 |
|------|------|
| 1 | 男 |
| 2 | 女 |

#### 学生状态 (STU_STATE_CODE)
| 代码 | 名称 |
|------|------|
| 01 | 在读 |
| 02 | 休学 |
| 03 | 退学 |
| 07 | 毕业 |
| 08 | 结业 |
| 09 | 肄业 |

#### 是否标识 (ISTRUE, IS_NORMAL)
| 值 | 含义 |
|------|------|
| 1 | 是/有效 |
| 0 | 否/无效 |

#### 层级类型 (LEVEL_TYPE)
| 代码 | 名称 |
|------|------|
| BM | 行政部门/处室 |
| YX | 院系 |
| ZY | 专业 |

## 查询意图识别

### 统计类查询
| 用户表达 | SQL 关键字 |
|----------|------------|
| 有多少/数量 | COUNT(*) |
| 平均/均值 | AVG() |
| 总数/合计 | COUNT(*), SUM() |
| 比例/百分比 | CASE WHEN + COUNT/SUM |
| 排名/第几 | ORDER BY + RANK() |

### 列表类查询
| 用户表达 | SQL 关键字 |
|----------|------------|
| 有哪些/列出 | SELECT ... |
| 所有/全部 | 无额外 WHERE |
| 是什么 | 单值查询 + ROWNUM = 1 |

### 筛选类查询
| 用户表达 | SQL 实现 |
|----------|----------|
| 是/为 | WHERE field = value |
| 包含 | WHERE field LIKE '%value%' |
| 在...之间 | WHERE field BETWEEN ... AND ... |
| 大于/小于 | WHERE field >/< value |

### 时间类查询
| 用户表达 | SQL 实现 |
|----------|----------|
| 本学期/当前学期 | 最新记录或日期判断 |
| 今年/本年 | WHERE year = CURRENT_YEAR |
| 今天 | WHERE date = TRUNC(SYSDATE) |
| 最近N天 | WHERE date >= SYSDATE - N |

## 常见查询模板

### 模板1：单属性查询
```sql
-- 问：...的...是什么？
SELECT [字段名] AS [别名]
FROM [表名]
WHERE [条件]
  AND ROWNUM = 1;
```

### 模板2：列表查询
```sql
-- 问：有哪些...？
SELECT [字段列表]
FROM [表名]
WHERE [条件]
ORDER BY [排序字段]
FETCH FIRST [数量] ROWS ONLY;
```

### 模板3：代码关联查询
```sql
-- 问：...的类型名称？
SELECT t.[代码字段], c.NAME_ AS [类型名称]
FROM [表名] t
LEFT JOIN HQ_CODE c ON t.[代码字段] = c.CODE_
                 AND c.GROUP_TYPE = '[代码类型]'
WHERE [条件];
```

### 模板4：人员查询
```sql
-- 问：某人的某属性？
SELECT [属性字段列表]
FROM HQ_RS_TEA
WHERE NAME_ LIKE '%[姓名部分]%';
```

### 模板5：归属查询
```sql
-- 问：...归属于/隶属于哪个部门？
SELECT child.NAME_ AS [下级名称],
       parent.NAME_ AS [上级名称]
FROM [表名] child
LEFT JOIN [表名] parent ON child.PID = parent.ID
WHERE child.NAME_ LIKE '%[名称]%';
```

### 模板6：统计查询
```sql
-- 问：有多少/各有多少？
SELECT [分组字段],
       COUNT(*) AS [数量]
FROM [表名]
WHERE [条件]
GROUP BY [分组字段]
ORDER BY COUNT(*) DESC;
```

## 容错处理

### 拼写变体
| 正确 | 可能的输入 |
|------|------------|
| 教工号 | 工号/教师编号/教师工号 |
| 籍贯 | 老家/家乡/出生地 |
| 双师型 | 双师/双师型教师 |
| 培养层次 | 办学层次/学历层次/学生类型 |
| 班级ID | 班级编号/班级代码 |

### 模糊匹配策略
1. 人名：使用 LIKE '%关键词%'
2. 部门名：尝试多个关键词
3. 专业名：去除方向后缀匹配
4. 课程名：处理I/II/A/B等后缀
