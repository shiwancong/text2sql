#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
SQL 查询验证工具
用于在执行前验证 SQL 的正确性
"""

import re
from typing import Dict, List, Tuple, Optional


class SQLValidator:
    """SQL 查询验证器"""

    def __init__(self):
        # Oracle 关键字列表
        self.oracle_keywords = {
            'SELECT', 'FROM', 'WHERE', 'ORDER', 'BY', 'GROUP', 'HAVING',
            'JOIN', 'LEFT', 'RIGHT', 'INNER', 'OUTER', 'ON', 'AS',
            'AND', 'OR', 'NOT', 'IN', 'LIKE', 'BETWEEN', 'IS', 'NULL',
            'FETCH', 'FIRST', 'ROW', 'ROWS', 'ONLY', 'ROWNUM',
            'CASE', 'WHEN', 'THEN', 'ELSE', 'END',
            'COUNT', 'SUM', 'AVG', 'MAX', 'MIN',
            'SYSDATE', 'TO_DATE', 'TO_CHAR', 'TRUNC'
        }

    def validate_sql(self, sql: str, available_tables: List[str]) -> Tuple[bool, List[str]]:
        """
        验证 SQL 查询

        返回: (是否有效, 错误/警告列表)
        """
        errors = []
        warnings = []

        # 基本语法检查
        if not sql.strip():
            errors.append("SQL 为空")
            return False, errors

        sql_upper = sql.upper()

        # 检查是否有 SELECT
        if 'SELECT' not in sql_upper:
            errors.append("缺少 SELECT 关键字")
            return False, errors

        # 检查是否有 FROM
        if 'FROM' not in sql_upper:
            errors.append("缺少 FROM 关键字")
            return False, errors

        # 检查表名
        tables = self._extract_tables(sql)
        for table in tables:
            if table not in available_tables:
                warnings.append(f"表名 {table} 可能不存在")

        # 检查引号使用
        single_quotes = sql.count("'")
        double_quotes = sql.count('"')
        if double_quotes > 0:
            warnings.append("Oracle 建议使用单引号而非双引号")

        # 检查字符串是否成对
        if single_quotes % 2 != 0:
            errors.append("单引号不匹配")

        # 检查常见的 MySQL 语法
        if 'LIMIT' in sql_upper:
            errors.append("Oracle 不支持 LIMIT，请使用 FETCH FIRST ... ROWS ONLY")

        # 检查 ROWNUM 使用
        if 'ROWNUM' in sql_upper and 'FETCH FIRST' in sql_upper:
            warnings.append("同时使用了 ROWNUM 和 FETCH FIRST，可能结果不正确")

        # 检查大小写
        if not self._check_case_consistency(sql):
            warnings.append("建议表名和字段名使用大写")

        is_valid = len(errors) == 0
        return is_valid, errors + warnings

    def _extract_tables(self, sql: str) -> List[str]:
        """提取 SQL 中的表名"""
        tables = []

        # 简单的表名提取：FROM 后面的词
        from_pattern = r'\bFROM\s+(\w+)'
        tables.extend(re.findall(from_pattern, sql, re.IGNORECASE))

        # JOIN 后面的词
        join_pattern = r'\b(?:JOIN|LEFT\s+JOIN|RIGHT\s+JOIN|INNER\s+JOIN|OUTER\s+JOIN)\s+(\w+)'
        tables.extend(re.findall(join_pattern, sql, re.IGNORECASE))

        return list(set(tables))

    def _check_case_consistency(self, sql: str) -> bool:
        """检查是否使用了大写的表名和字段名"""
        # 提取可能的标识符
        # FROM 和 JOIN 后面的词应该是大写
        from_match = re.search(r'\bFROM\s+([a-z])', sql, re.IGNORECASE)
        if from_match:
            # 检查 FROM 后面紧跟的小写字母
            pattern = r'FROM\s+([a-z][a-z0-9_]*)'
            matches = re.findall(pattern, sql)
            if matches:
                return False
        return True


class QueryResultValidator:
    """查询结果验证器"""

    @staticmethod
    def validate_result(question: str, sql: str, result: list) -> Tuple[bool, str]:
        """
        验证查询结果的合理性

        返回: (是否合理, 分析消息)
        """
        if not result:
            # 检查是否应该有结果
            if QueryResultValidator._should_have_data(question):
                return False, "查询结果为空，可能是筛选条件过严或数据不存在"
            return True, "查询结果为空（符合预期）"

        # 检查结果数量
        if len(result) == 1:
            return True, "查询返回单条结果"
        elif len(result) > 100:
            return True, f"查询返回 {len(result)} 条结果（可能过多）"

        return True, f"查询返回 {len(result)} 条结果"

    @staticmethod
    def _should_have_data(question: str) -> bool:
        """判断查询是否应该有数据"""
        # 学校基本信息查询应该有数据
        keywords = ['学校', '我校', '网址', '名称', '性质', '地址']
        return any(kw in question for kw in keywords)


def format_validation_result(is_valid: bool, messages: List[str]) -> str:
    """格式化验证结果"""
    if is_valid and not messages:
        return "✓ 验证通过"

    result = []
    for msg in messages:
        if '错误' in msg or '缺少' in msg or '不匹配' in msg:
            result.append(f"✗ {msg}")
        else:
            result.append(f"⚠ {msg}")

    return "\n".join(result)


# 使用示例
if __name__ == "__main__":
    validator = SQLValidator()

    # 测试 SQL
    test_sqls = [
        "SELECT NAME_ FROM HQ_RS_TEA WHERE NAME_ LIKE '%孙明涛%'",
        "SELECT name_ from hq_rs_tea",  # 小写字段名
        "SELECT * FROM table LIMIT 10",  # MySQL 语法
    ]

    for sql in test_sqls:
        print(f"\nSQL: {sql}")
        is_valid, messages = validator.validate_sql(sql, ['HQ_RS_TEA', 'HQ_JC_XX'])
        print(format_validation_result(is_valid, messages))
