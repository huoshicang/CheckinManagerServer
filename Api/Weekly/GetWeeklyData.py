from component import QueryDataFetchAll, HTTP_STATUS_CODES, INTERNAL_SERVER_ERROR, QueryDataFetchOne
from component.status_codes import NOT_FOUND


def GetWeekly(Data: dict) -> dict:
    """
    获取用户周报信息
    """
    username = Data['username']
    searchname = Data['searchname']
    starttime = Data['starttime']
    endtime = Data['endtime']

    role = Administrator(UserName=tuple((username,)))

    try:

        if role['role'] == "admin":
            Query = LookUpAll(searchname=searchname, starttime=starttime, endtime=endtime)
        elif role['role'] == "user":
            Query = LookUpOne(username=username, starttime=starttime, endtime=endtime)
        else:
            return INTERNAL_SERVER_ERROR()

        if Query is None:
            return NOT_FOUND()

        for item in Query:
            item["weekly_time"] = str(item['weekly_time'])

        return {
            "code": HTTP_STATUS_CODES['OK'],
            "data": Query,
            "message": "获取成功"
        }

    except:
        return INTERNAL_SERVER_ERROR()


def LookUpAll(searchname, starttime, endtime):
    """
    获取用户周报信息 查表
    """
    return QueryDataFetchAll(sql="""SELECT
            weekly_id,
            username,
            title, # 标题
            content, # 内容
            weekly_time,
            sub,
            enable # 是否开启
            FROM weeklydata
            WHERE 
                is_deleted = false
            AND
                (username = '' OR username = %s OR %s = '')
             AND 
                (weekly_time = '' OR weekly_time >= %s OR %s = '')
             AND
                (weekly_time = '' OR weekly_time <= %s OR %s = '');""",
                             params=tuple((searchname, searchname, starttime, starttime, endtime, endtime)))


def LookUpOne(username, starttime, endtime):
    """
    获取用户周报信息 查表
    """
    return QueryDataFetchAll(sql="""SELECT
            weekly_id,
            username,
            title, # 标题
            content, # 内容
            weekly_time,
            sub,
            enable # 是否开启
            FROM weeklydata
            WHERE 
                is_deleted = false
            AND
                (username = '' OR username = %s OR %s = '')
             AND 
                (weekly_time = '' OR weekly_time >= %s OR %s = '')
             AND
                (weekly_time = '' OR weekly_time <= %s OR %s = '');""",
                             params=tuple((username, username, starttime, starttime, endtime, endtime)))


def Administrator(UserName):
    """
    获取角色
    """
    return QueryDataFetchOne(
        sql="""SELECT role FROM sys_user WHERE username = %s;""", params=UserName)
