from component import QueryDataFetchOne, HTTP_STATUS_CODES, QueryDataFetchAll, INTERNAL_SERVER_ERROR
from component.status_codes import NOT_FOUND

from component.Time import Da


def GetUserInfo(Data: dict) -> dict:
    name = Data.get('name')
    username = Data.get('username')
    phone = Data.get('phone')
    gxy_info = Data.get('gxy_info')
    page_size = int(Data.get('page_size'))
    page_number = int(Data.get('page_number'))

    role = Administrator(UserName=tuple((name,)))['role']

    if role is None:
        return NOT_FOUND()

    try:
        Query = None

        if role == "admin":
            Query = LookUpAll(params=tuple((username, username,
                                            phone, phone,
                                            gxy_info, gxy_info,
                                            page_size, ((page_number - 1) * page_size))))


        elif role == "user":
            Query = LookUpOne(params=tuple((name,)))

        else:
            return INTERNAL_SERVER_ERROR()

        if Query is None:
            return NOT_FOUND()

        for item in Query:
            item["update_time"] = str(item['update_time'])

        return {
            "code": HTTP_STATUS_CODES['OK'],
            "data": Query,
            "message": "获取成功"
        }

    except:
        return INTERNAL_SERVER_ERROR()


def LookUpAll(params):
    return QueryDataFetchAll(sql="""SELECT id,
                    username,
                    phone,
                    gxy_info,
                    role,
                    update_time
                FROM sys_user
                WHERE
                    is_deleted = false
                AND 
                    (username = '' OR username = %s OR %s = '')
                AND 
                    (phone = '' OR phone = %s OR %s = '')
                AND
                    (gxy_info = '' OR gxy_info = %s OR %s = '')
                LIMIT %s
                OFFSET %s;""",
                             params=params)


def LookUpOne(params):
    """
    获取用户的信息
    """
    return QueryDataFetchOne(
        sql="""SELECT
        id,
        username,
        phone,
        role,
        gxy_info,
        update_time
        FROM sys_user
        WHERE username = %s;""",
        params=params)


def Administrator(UserName):
    """
    获取角色
    """
    return QueryDataFetchOne(
        sql="""SELECT role FROM sys_user WHERE username = %s;""", params=UserName)
