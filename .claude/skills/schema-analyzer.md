---
name: schema-analyzer
description: 分析表结构，帮助理解数据库设计
---

# 表结构分析 Skill

## 能力范围

- 获取表的完整结构信息
- 解读字段含义和业务语义
- 分析表之间的关联关系
- 生成表结构文档

## 可用 MCP 工具

| 工具 | 说明 | 参数 |
|------|------|------|
| list_tables | 列出所有可访问的表 | 无 |
| describe_table | 获取表结构（字段名、类型、注释） | table_name: string |

## 执行流程

```
1. 接收表名或查询条件
    │
    ▼
2. 使用 list_tables() 确认表存在
    │
    ▼
3. 使用 describe_table() 获取详细结构
    │
    ▼
4. 解析字段信息和注释
    │
    ▼
5. 参考 knowledge/table-relationships.md 查找关联表
    │
    ▼
6. 输出结构化报告
```

## 输出格式

### 表结构报告模板

```markdown
## 表名：TABLE_NAME

### 基本信息
| 属性 | 值 |
|------|-----|
| 中文名称 | xxx |
| 业务描述 | xxx |

### 字段列表

| 字段名 | 类型 | 可空 | 默认值 | 说明 |
|--------|------|------|--------|------|
| ID | NUMBER(10) | N | | 主键 |
| NAME | VARCHAR2(100) | N | | 名称 |
| ... | ... | ... | ... | ... |

### 索引
- PRIMARY_KEY: ID
- INDEX_NAME: FIELD_NAME

### 关联表
| 关联表 | 关联类型 | 关联字段 |
|--------|----------|----------|
| OTHER_TABLE | 1:N | this.id = other.parent_id |
```

## 常见表结构模式

### 主表（实体表）

特征：
- 有主键 ID
- 有名称/编码字段
- 有创建时间、更新时间

示例：学生表、教师表、课程表

### 关系表/中间表

特征：
- 复合主键（多个外键）
- 存储多对多关系
- 可能有附加属性（如时间、状态）

示例：选课表、班级成员表

### 字典表/配置表

特征：
- 键值对结构
- 类型+编码+名称
- 相对静态

示例：民族字典、课程类型表

### 日志表/记录表

特征：
- 时间字段为主
- 记录状态变化
- 数据量较大

示例：操作日志、出勤记录

## 字段命名规范识别

| 前缀/后缀 | 含义 | 示例 |
|-----------|------|------|
| _ID | 主键/外键 | STUDENT_ID |
| _NAME | 名称 | COURSE_NAME |
| _CODE | 编码 | DEPT_CODE |
| _DATE | 日期 | START_DATE |
| _TIME | 时间 | CREATE_TIME |
| _FLAG | 标志位 | IS_ACTIVE |
| _TYPE | 类型 | COURSE_TYPE |
| _COUNT | 计数 | STUDENT_COUNT |

## 数据类型判断

| Oracle 类型 | 含义 | 业务场景 |
|-------------|------|----------|
| NUMBER(p,s) | 数值 | 金额、分数、数量 |
| VARCHAR2(n) | 字符串 | 名称、描述、编码 |
| DATE | 日期时间 | 创建时间、开始日期 |
| CHAR(n) | 固定字符 | 性别、状态码 |
| CLOB | 大文本 | 备注说明 |

## 使用场景

1. **查询前准备**：了解表结构，避免 SQL 错误
2. **数据探索**：发现可用字段和关联关系
3. **文档生成**：自动生成表结构文档
4. **问题诊断**：分析 SQL 问题时的参考

## 示例

用户输入："分析一下 student 表的结构"

输出：
```
正在分析 student 表...

获取表结构成功！student 表包含以下字段：
- ID (NUMBER): 学生ID，主键
- NAME (VARCHAR2): 学生姓名
- GENDER (CHAR): 性别
- BIRTH_DATE (DATE): 出生日期
- MAJOR_ID (NUMBER): 专业ID（外键）
- CLASS_ID (NUMBER): 班级ID（外键）
...

关联表分析：
- 通过 MAJOR_ID 关联到 MAJOR 表
- 通过 CLASS_ID 关联到 CLASS 表

建议查询：
- 查询学生基本信息：SELECT * FROM student WHERE id = ?
- 查询学生专业：SELECT s.name, m.major_name FROM student s JOIN major m ON s.major_id = m.id
```
