from component import HTTP_STATUS_CODES, INTERNAL_SERVER_ERROR, Update, QueryDataFetchOne


def UpInfo(UserName: str) -> dict:
    """
    修改用户的信息标识
    """
    try:
        Query = Administrator(params=tuple((UserName,)))

        print(Query)

        if Query == "操作成功":
            return {
                "code": HTTP_STATUS_CODES['OK'],
                "data": [],
                "message": "修改成功"
            }
        elif Query == "用户名不存在":
            return {
                "code": HTTP_STATUS_CODES['NOT_FOUND'],  # 使用 HTTP 404 表示未找到
                "data": [],
                "message": "用户名不存在"
            }
        else:
            return {
                "code": HTTP_STATUS_CODES['INTERNAL_SERVER_ERROR'],
                "data": [],
                "message": f"修改失败：{Query}"
            }

    except:
        return INTERNAL_SERVER_ERROR()


def Administrator(params):
    """
    获取角色 并修改
    """
    info = QueryDataFetchOne(
        sql="""SELECT
        username # 用户名
        FROM sys_user
        WHERE username = %s;""", params=params)

    if info is not None:
        return Update(
            Sql="""UPDATE sys_user
                SET gxy_info = 'true'
                WHERE username = %s;""", params=params)
    else:
        return "用户名不存在"
