from component import QueryDataFetchOne, Update
from component.status_codes import NOT_FOUND, BAD_REQUEST2, INTERNAL_SERVER_ERROR, HTTP_STATUS_CODES


def DelUserInfo(Data: dict) -> dict:
    delid = Data['id']
    username = Data['username']

    name = Administrator(params=tuple((delid,)))

    if name is None:
        return NOT_FOUND()

    if name['username'] == username:
        try:
            DelReq = Del(params=tuple((delid,)))

            if DelReq == "操作成功":
                return {
                    "code": HTTP_STATUS_CODES['OK'],
                    "data": [],
                    "message": "修改成功"
                }
            else:
                return {
                    "code": HTTP_STATUS_CODES['INTERNAL_SERVER_ERROR'],
                    "data": [],
                    "message": f"修改失败：{DelReq}"
                }
        except:
            return INTERNAL_SERVER_ERROR()
    else:
        return BAD_REQUEST2()


def Administrator(params):
    """
    获取角色
    """
    return QueryDataFetchOne(
        sql="""SELECT username FROM sys_user WHERE id = %s;""", params=params)


def Del(params):
    """
    获取角色
    """
    return Update(Sql="""UPDATE sys_user
                SET is_deleted = true
                WHERE id = %s;""", params=params)
