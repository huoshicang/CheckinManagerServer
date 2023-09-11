from component import QueryDataFetchAll, HTTP_STATUS_CODES, INTERNAL_SERVER_ERROR
from component.status_codes import NOT_FOUND


def WeeklyData(Data: dict) -> dict:
    """
    获取用户周报信息
    """
    username = Data['username']
    starttime = Data['starttime']
    endtime = Data['endtime']

    try:
        Query = LookUpAll(username=username, starttime=starttime, endtime=endtime)

        if Query is None:
            return NOT_FOUND()

        return {
            "code": HTTP_STATUS_CODES['OK'],
            "data": Query,
            "message": "获取成功"
        }

    except:
        return INTERNAL_SERVER_ERROR()


def LookUpAll(username, starttime, endtime):
    """
    获取用户周报信息 查表
    """
    sql = """SELECT
            title, # 标题
            weekly_time , # 提交时间
            content # 内容
            FROM weeklydata
            WHERE username = %s"""

    params = [username]

    if starttime:
        sql += " AND weekly_time >= %s"
        params.append(starttime)
    if endtime:
        sql += " AND weekly_time <= %s"
        params.append(endtime)

    return QueryDataFetchAll(sql=sql, params=tuple(params))
