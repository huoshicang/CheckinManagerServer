from component import QueryDataFetchOne, HTTP_STATUS_CODES, QueryDataFetchAll, INTERNAL_SERVER_ERROR
from component.status_codes import NOT_FOUND


def GetCheckInfo(Data: dict) -> dict:
    """
    获取签到用户
    """

    name = Data['name']
    phone = Data['phone']
    enable = Data['enable']
    role = Data['role']

    role = Administrator(UserName=tuple((role,)))

    if role is None:
        return NOT_FOUND()

    try:
        Query = None

        if role['role'] == "admin":
            Query = LookUpAll(name, phone, enable)
        elif role['role'] == "user":
            Query = LookUpOne(params=tuple((username,)))
        else:
            return INTERNAL_SERVER_ERROR()

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


def LookUpAll(name, phone, enable):
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
        WHERE is_deleted = false
        AND 
        (name = '' OR name = %s OR %s = '')
         AND 
        (phone = '' OR phone = %s OR %s = '')
         AND
        (enable = '' OR enable = %s OR %s = '');""", params=tuple((name, name,
                                                                    phone, phone,
                                                                    enable, enable,)))


def Administrator(UserName):
    """
    获取角色
    """
    return QueryDataFetchOne(
        sql="""SELECT role FROM sys_user WHERE username = %s;""", params=UserName)
