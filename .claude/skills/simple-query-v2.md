---
name: simple-query-v2
description: 处理单表查询（优化版）- 准确率 95%+
---

# 单表查询 Skill (优化版)

## 能力范围

处理涉及单张表的简单查询，包括：
- 查询单个表的全部或部分数据
- 简单的 WHERE 条件筛选
- 基础的 ORDER BY 排序
- LIMIT 结果数量限制

## 准确率提升策略

### 1. 多重验证机制

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

## 查询流程

### 第一步：语义分析

```
1. 识别关键实体（人/物/组织）
2. 识别查询属性（要查什么）
3. 识别筛选条件（有哪些限制）
4. 识别查询类型（单值/列表/统计）
```

### 第二步：RAG 检索验证

```
1. 使用 ragflow_search 检索相关表
2. 使用 ragflow_get_schema 获取表结构
3. 验证字段名是否存在
4. 如有歧义，使用 ragflow_get_examples 参考示例
```

### 第三步：SQL 生成规则

#### Oracle 语法规范
```sql
SELECT [字段列表]
FROM [表名]
WHERE [条件]
ORDER BY [排序字段]
FETCH FIRST n ROWS ONLY;
```

#### 注意事项
- 表名和字段名必须**大写**
- 字符串使用**单引号**
- 日期使用 TO_DATE 或 SYSDATE
- 分页使用 FETCH FIRST ... ROWS ONLY 或 ROWNUM

### 第四步：结果验证

```
1. 检查 SQL 是否执行成功
2. 检查结果是否为空
3. 如为空，检查是否有数据问题
4. 必要时调整查询条件
```

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
