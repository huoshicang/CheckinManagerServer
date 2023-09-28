from component import QueryDataFetchOne, HTTP_STATUS_CODES, QueryDataFetchAll, INTERNAL_SERVER_ERROR
from component.status_codes import NOT_FOUND


def GetCheckQuest(Data: dict) -> dict:
    """
    获取签到用户
    """
    name = Data['name']
    username = Data['username']
    # role = Data['role']

    role = Administrator(UserName=tuple((name,)))

    if role is None:
        return NOT_FOUND()

    try:
        Query = None

        if role['role'] == "admin":
            Query = LookUpAll(username)
        elif role['role'] == "user":
            Query = LookUpOne(params=tuple((name,)))
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
        check_time
        FROM gxy_user
        WHERE name = %s AND is_deleted = false;""",
        params=params)


def LookUpAll(username):
    """
    获取所有用户的信息
    """
    return QueryDataFetchAll(
        sql="""SELECT
        id,
        enable,
        name,
        date(check_time) AS check_time
        FROM gxy_user
        WHERE is_deleted = false
        AND 
        (name = '' OR name = %s OR %s = '');""", params=tuple((username,username,)))


def Administrator(UserName):
    """
    获取角色
    """
    return QueryDataFetchOne(
        sql="""SELECT role FROM sys_user WHERE username = %s;""", params=UserName)
