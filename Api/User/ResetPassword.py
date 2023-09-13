from component import QueryDataFetchOne, Update
from component.status_codes import NOT_FOUND, HTTP_STATUS_CODES, BAD_REQUEST2


def ResetPassword(Data: dict):
    id = Data['id']
    username = Data['username']

    password = Administrator(params=tuple((id, username,)))

    if password is None:
        return NOT_FOUND()

    try:
        SetMsg = Set(params=tuple((id, username,)))

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
        sql="""SELECT password FROM sys_user WHERE id = %s AND username = %s;""", params=params)


def Set(params):
    """
    获取角色
    """
    return Update(Sql="""UPDATE sys_user SET
                password = '123456'
                WHERE id = %s AND username = %s;""", params=params)
