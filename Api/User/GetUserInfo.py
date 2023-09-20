from component import QueryDataFetchOne, HTTP_STATUS_CODES, QueryDataFetchAll, INTERNAL_SERVER_ERROR
from component.status_codes import NOT_FOUND
from component.sql import DynamicSql


def GetUserInfo(Data: dict) -> dict:
    print(Data)
    name = Data['name']
    username = Data['username']
    gxy_info = Data['gxy_info']

    role = Administrator(UserName=tuple((name,)))['role']

    if role is None:
        return NOT_FOUND()

    try:
        Query = None

        if role == "admin":
            # 构建sql语句
            # sql, params = DynamicSql(sql="""SELECT
            # id,
            # username,
            # phone,
            # gxy_info,
            # role,
            # update_time
            # FROM sys_user WHERE is_deleted = false""", data=Data, Don=['name'])

            Query = QueryDataFetchAll(sql="""SELECT id,
            username,
            phone,
            gxy_info,
            role,
            update_time
            FROM sys_user
            WHERE
            is_deleted = false AND 
                (username = '' OR username = %s OR %s = '')
                AND
                (gxy_info = '' OR gxy_info = %s OR %s = '');""", params=tuple((username, username, gxy_info, gxy_info,)))


            print(Query)

        elif role == "user":
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
        return INTERNAL_SERVER_ERROR()


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
        DATE_FORMAT(update_time, '%Y-%m-%d %H:%i:%s') AS update_time
        FROM sys_user
        WHERE username = %s;""",
        params=params)


def Administrator(UserName):
    """
    获取角色
    """
    return QueryDataFetchOne(
        sql="""SELECT role FROM sys_user WHERE username = %s;""", params=UserName)
