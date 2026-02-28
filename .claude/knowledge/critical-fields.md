# 关键字段必查表

生成SQL前，必须检查以下关键字段，确保查询条件完整。

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
| 其他 | 毕业、退学等 | 根据具体问题确定 |

**示例**：
```sql
-- 查询在校学生
WHERE STU_STATE_CODE = '01'

-- 查询休学学生
WHERE STU_STATE_CODE = '02'
```

---

## 教师相关关键字段

### 教师状态字段

HQ_RS_TEA表没有ISTRUE字段，但可以通过其他字段判断：

| 字段 | 含义 | 使用场景 |
|------|------|---------|
| ZW_NAME | 职称 | 查询有职称的教师：`WHERE ZW_NAME IS NOT NULL` |
| 其他状态字段 | 根据实际情况 | 查看 describe_table 确认 |

---

## 课程相关关键字段

### IS_CORE（核心课程标识）

| 字段值 | 含义 | 用户问题 |
|--------|------|---------|
| 1 | 是核心课程 | "核心课有哪些" → `WHERE IS_CORE = 1` |
| 0 或 NULL | 非核心课程 | - |

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
