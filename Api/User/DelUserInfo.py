from component import QueryDataFetchOne, Update
from component.status_codes import NOT_FOUND, BAD_REQUEST2, INTERNAL_SERVER_ERROR, HTTP_STATUS_CODES


def DelUserInfo(Data: dict) -> dict:
    delid = Data['id']
    username = Data['username']

    sys_id_username = AdministratorSys(params=tuple((delid,)))

    gxy_id_username = AdministratorGxy(params=tuple((username,)))

    if sys_id_username is None:
        return NOT_FOUND()

    elif sys_id_username['username'] != username:
        return {
            "code": HTTP_STATUS_CODES['BAD_REQUEST'],
            "data": [],
            "message": "用户名不存在",
        }

    elif sys_id_username['id'] != delid:
        return {
            "code": HTTP_STATUS_CODES['BAD_REQUEST'],
            "data": [],
            "message": "Id与用户名不匹配",
        }

    if sys_id_username['username'] and gxy_id_username is None:
        return EditSysTable(username, delid)

    if sys_id_username['id'] == delid:
        return EditAllTable(username, delid)

    else:
        return BAD_REQUEST2()


def AdministratorSys(params):
    """
    获取系统用户信息
    """
    return QueryDataFetchOne(
        sql="""SELECT id, username FROM sys_user WHERE id = %s;""", params=params)


def AdministratorGxy(params):
    """
    获取签到用户信息
    """
    return QueryDataFetchOne(
        sql="""SELECT name FROM gxy_user WHERE name = %s;""", params=params)


def Del(params):
    """
    删除系统用户
    """
    return Update(Sql="""UPDATE sys_user
                         SET is_deleted = true
                         WHERE username = %s AND id = %s ;""", params=params)


def DelAll(params):
    """
    删除系统和签到用户
    """
    return Update(Sql="""UPDATE sys_user
                         JOIN gxy_user
                         ON sys_user.username = gxy_user.name
                         SET
                            sys_user.is_deleted = true,
                            gxy_user.is_deleted = true,
                            gxy_user.enable = false
                         WHERE 
                            sys_user.username = %s
                         AND
                            sys_user.id = %s
                         AND
                            gxy_user.name = %s;""", params=params)


def EditSysTable(username, delid):
    """
    删除系统用户
    """
    try:
        DelReq = Del(params=tuple((username, delid,)))

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


def EditAllTable(username, delid):
    """
    删除所有用户
    """
    try:
        DelReq = DelAll(params=tuple((username, delid, username,)))

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
