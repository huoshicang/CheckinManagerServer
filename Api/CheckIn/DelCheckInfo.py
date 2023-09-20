from component import QueryDataFetchOne, Update
from component.status_codes import NOT_FOUND, BAD_REQUEST2, INTERNAL_SERVER_ERROR, HTTP_STATUS_CODES


def DelCheck(Data: dict) -> dict:
    delid = Data['id']
    name = Data['name']

    nameMes = Administrator(params=tuple((delid,)))

    if nameMes is None:
        return NOT_FOUND()

    if nameMes['name'] == name:
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
        sql="""SELECT name FROM gxy_user WHERE id = %s;""", params=params)


def Del(params):
    """
    删除
    """
    return Update(Sql="""UPDATE gxy_user
                SET is_deleted = true,
                enable = false
                WHERE id = %s;""", params=params)
