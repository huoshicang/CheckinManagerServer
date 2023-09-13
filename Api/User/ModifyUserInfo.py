from component import QueryDataFetchOne, Update
from component.status_codes import NOT_FOUND, BAD_REQUEST2, HTTP_STATUS_CODES


def Modify(Data: dict):
    id = Data['id']
    username = Data['username']
    phone = Data['phone']

    name = Administrator(params=tuple((id,)))

    if name is None:
        return NOT_FOUND()

    try:
        SetMsg = Set(params=tuple((username, phone, id,)))

        if SetMsg == "操作成功":
            return {
                "code": HTTP_STATUS_CODES['OK'],
                "data": [],
                "message": "修改成功"
            }
        else:
            return {
                "code": HTTP_STATUS_CODES['INTERNAL_SERVER_ERROR'],
                "data": [],
                "message": f"修改失败：{SetMsg}"
            }

    except:
        return BAD_REQUEST2()


def Administrator(params):
    """
    获取角色
    """
    return QueryDataFetchOne(
        sql="""SELECT username FROM sys_user WHERE id = %s;""", params=params)


def Set(params):
    """
    获取角色
    """
    return Update(Sql="""UPDATE sys_user SET
                username = %s,
                phone = %s
                WHERE id = %s;""", params=params)
