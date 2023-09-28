from component import QueryDataFetchAll, HTTP_STATUS_CODES, INTERNAL_SERVER_ERROR
from component.status_codes import NOT_FOUND


def GetMonth(Data: dict) -> dict:
    """
    获取用户月报信息
    """
    username = Data['username']
    starttime = Data['starttime']
    endtime = Data['endtime']

    try:
        Query = LookUpAll(username=username, starttime=starttime, endtime=endtime)

        if Query is None:
            return NOT_FOUND()

        for item in Query:
            item["month_time"] = str(item['month_time'])

        return {
            "code": HTTP_STATUS_CODES['OK'],
            "data": Query,
            "message": "获取成功"
        }

    except:
        return INTERNAL_SERVER_ERROR()


def LookUpAll(username, starttime, endtime):
    """
    获取用户月报信息
    """
    return QueryDataFetchAll(sql="""SELECT
            month_id,
            username,
            title, # 标题
            content, # 内容
            month_time,
            sub,
            enable # 是否开启
            FROM monthdata
            WHERE 
                is_deleted = false
            AND
                (username = '' OR username = %s OR %s = '')
             AND 
                (month_time = '' OR month_time >= %s OR %s = '')
             AND
                (month_time = '' OR month_time <= %s OR %s = '');""",
                             params=tuple((username, username, starttime, starttime, endtime, endtime)))
