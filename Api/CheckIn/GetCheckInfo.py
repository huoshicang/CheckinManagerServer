from component import QueryDataFetchOne, HTTP_STATUS_CODES, QueryDataFetchAll, INTERNAL_SERVER_ERROR
from component.status_codes import NOT_FOUND


def GetCheckInfo(UserName: str) -> dict:
    """
    获取签到用户
    """
    role = Administrator(UserName=tuple((UserName,)))

    if role is None:
        return NOT_FOUND()

    try:
        Query = None

        if role['role'] == "admin":
            Query = LookUpAll()
        elif role['role'] == "user":
            Query = LookUpOne(params=tuple((UserName,)))
        else:
            INTERNAL_SERVER_ERROR()

        if Query is None:
            return NOT_FOUND()

        return {
            "code": HTTP_STATUS_CODES['OK'],
            "data": Query,
            "message": "获取成功"
        }

    except:
        INTERNAL_SERVER_ERROR()


def LookUpOne(params):
    """
    获取用户的信息
    """
    return QueryDataFetchOne(
        sql="""SELECT
        id,
        enable,
        name,
        phone,
        country,
        province,
        city,
        area,
        address,
        longitude,
        latitude,
        note,
        type,
        pushKey,
        save_time
        FROM gxy_user
        WHERE name = %s AND is_deleted = false;""",
        params=params)


def LookUpAll():
    """
    :return: 获取所有用户的信息
    """
    return QueryDataFetchAll(
        sql="""SELECT
        id,
        enable,
        name,
        phone,
        country,
        province,
        city,
        area,
        address,
        longitude,
        latitude,
        note,
        type,
        pushKey,
        save_time
        FROM gxy_user
        WHERE is_deleted = false;""")


def Administrator(UserName):
    """
    获取角色
    """
    return QueryDataFetchOne(
        sql="""SELECT role FROM sys_user WHERE username = %s;""", params=UserName)
