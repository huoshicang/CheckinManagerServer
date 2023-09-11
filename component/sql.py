def DynamicSql(sql: str, data: dict, Don: list):
    """
    构建sql语句
    """
    dict_items = list(data.items())  # 转换为列表以获取索引
    params = []
    for index, (key, value) in enumerate(data.items()):

        if key in Don:
            continue
        elif bool(value):
            if " WHERE " not in sql:
                sql += f" WHERE "

            sql += f"{key} = %s "
            params.append(value)

            if index < len(dict_items) - 1:
                next_key, next_value = dict_items[index + 1]
                if bool(next_value):
                    sql += "AND "

    sql += ';'

    print(sql)

    return sql, tuple(params)
