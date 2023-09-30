from component import QueryDataFetchOne, HTTP_STATUS_CODES, QueryDataFetchAll, INTERNAL_SERVER_ERROR
from component.status_codes import NOT_FOUND


def GetUser(Data: dict) -> dict:
    """
    获取信息
    """

    username = Data['username']

    try:
        Personal = PersonalFun(UserName=tuple((username,)))
        if Personal is None:
            Personal = "暂无信息"
        else:
            Personal["update_time"] = str(Personal['update_time'])

        Check = CheckFun(UserName=tuple((username,)))
        if Check is None:
            Check = "暂无信息"
        else:
            Check["save_time"] = str(Check['save_time'])
            Check["check_time"] = str(Check['check_time'])

        Weekly = WeeklyFun(UserName=tuple((username,)))
        WeeklyDict = {
            "Check": [],
            "Sub": []
        }
        if Weekly is None:
            WeeklyDict = "暂无信息"
        else:
            WeeklyDict['Check'].append({
                "name": "开启提交",
                "数量": int(Weekly[0]['enable_true_count'])
            }, )
            WeeklyDict['Check'].append({
                "name": "关闭提交",
                "数量": int(Weekly[0]['enable_false_count'])
            }, )

            WeeklyDict['Sub'].append({
                "name": "已提交",
                "数量": int(Weekly[0]['sub_true_count'])
            }, )
            WeeklyDict['Sub'].append({
                "name": "未提交",
                "数量": int(Weekly[0]['sub_false_count'])
            }, )

        Month = MonthFun(UserName=tuple((username,)))
        MonthDict = {
            "Check": [],
            "Sub": []
        }
        if Month is None:
            MonthDict = "暂无信息"
        else:
            MonthDict['Check'].append({
                "name": "开启签到",
                "数量": int(Month[0]['enable_true_count'])
            }, )
            MonthDict['Check'].append({
                "name": "关闭签到",
                "数量": int(Month[0]['enable_false_count'])
            }, )

            MonthDict['Sub'].append({
                "name": "已提交",
                "数量": int(Month[0]['sub_true_count'])
            }, )
            MonthDict['Sub'].append({
                "name": "未提交",
                "数量": int(Month[0]['sub_false_count'])
            }, )

        return {
            "code": HTTP_STATUS_CODES['OK'],
            "data": {
                "Personal": Personal,
                "Check": Check,
                "Weekly": WeeklyDict,
                "Month": MonthDict,
            },
            "message": "获取成功"
        }

    except:
        INTERNAL_SERVER_ERROR()


def PersonalFun(UserName):
    """
    获取个人信息
    """
    return QueryDataFetchOne(
        sql="""SELECT 
            username,
            phone,
            role,
            update_time
        FROM 
            gxy.sys_user  
        WHERE username = %s;""", params=UserName)


def CheckFun(UserName):
    """
    获取签到信息
    """
    return QueryDataFetchOne(
        sql="""SELECT 
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
            save_time,
            check_time
        FROM 
            gxy.gxy_user 
        WHERE name = %s;""", params=UserName)


def WeeklyFun(UserName):
    """
    获取个人信息
    """
    return QueryDataFetchAll(
        sql="""SELECT 
            SUM(CASE WHEN enable = 'true' THEN 1 ELSE 0 END) AS enable_true_count,
            SUM(CASE WHEN enable = 'false' THEN 1 ELSE 0 END) AS enable_false_count,
            SUM(CASE WHEN sub = true THEN 1 ELSE 0 END) AS sub_true_count,
            SUM(CASE WHEN sub = false THEN 1 ELSE 0 END) AS sub_false_count
        FROM 
            gxy.weeklydata  
        WHERE username = %s;""", params=UserName)


def MonthFun(UserName):
    """
    获取个人信息
    """
    return QueryDataFetchAll(
        sql="""SELECT 
            SUM(CASE WHEN enable = 'true' THEN 1 ELSE 0 END) AS enable_true_count,
            SUM(CASE WHEN enable = 'false' THEN 1 ELSE 0 END) AS enable_false_count,
            SUM(CASE WHEN sub = true THEN 1 ELSE 0 END) AS sub_true_count,
            SUM(CASE WHEN sub = false THEN 1 ELSE 0 END) AS sub_false_count
        FROM 
            gxy.monthdata  
        WHERE username = %s;""", params=UserName)
