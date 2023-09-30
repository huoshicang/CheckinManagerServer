from component import QueryDataFetchOne, HTTP_STATUS_CODES, QueryDataFetchAll, INTERNAL_SERVER_ERROR


def GetAdmin(Data: dict) -> dict:
    """
    获取信息
    """

    username = Data['username']

    try:
        Personal = PersonalFun(UserName=tuple((username,)))
        Personal["update_time"] = str(Personal['update_time'])  # 格式化时间
        if Personal is None:
            Personal = "暂无信息"

        SysUser = SysUserFun()
        SysUserDict = {
            "Role": [],
            "CheckInfo": []
        }
        if SysUser is None:
            SysUserDict = "暂无信息"
        else:
            SysUserDict['Role'].append({
                "name": "用户",
                "数量": int(SysUser[0]['role_admin_count'])
            }, )
            SysUserDict['Role'].append({
                "name": "管理员",
                "数量": int(SysUser[0]['role_user_count'])
            }, )

            SysUserDict['CheckInfo'].append({
                "name": "有信息",
                "数量": int(SysUser[0]['gxy_info_false_count'])
            }, )
            SysUserDict['CheckInfo'].append({
                "name": "无信息",
                "数量": int(SysUser[0]['gxy_info_true_count'])
            }, )

        GxyUser = GxyUserFun()
        GxyUserDict = {
            "Check": [],
        }
        if GxyUser is None:
            GxyUserDict = "暂无信息"
        else:
            GxyUserDict['Check'].append({
                "name": "关闭签到",
                "数量": int(GxyUser[0]['enable_false_count'])
            }, )
            GxyUserDict['Check'].append({
                "name": "开启签到",
                "数量": int(GxyUser[0]['enable_true_count'])
            }, )

        Weekly = WeeklyFun()
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

        Month = MonthFun()
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
                "SysUser": SysUserDict,
                "GxyUser": GxyUserDict,
                "Weekly": WeeklyDict,
                "Month": MonthDict,
            },
            "message": "获取成功"
        }

    except:
        return INTERNAL_SERVER_ERROR()


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


def SysUserFun():
    """
    获取系统用户信息
    """
    return QueryDataFetchAll(
        sql="""SELECT 
            SUM(CASE WHEN role = 'admin' THEN 1 ELSE 0 END) AS role_admin_count,
            SUM(CASE WHEN role = 'user' THEN 1 ELSE 0 END) AS role_user_count,
            SUM(CASE WHEN gxy_info = 'false' THEN 1 ELSE 0 END) AS gxy_info_false_count,
            SUM(CASE WHEN gxy_info = 'true' THEN 1 ELSE 0 END) AS gxy_info_true_count
        FROM 
            sys_user;""")


def GxyUserFun():
    """
    获取签到用户信息
    """
    return QueryDataFetchAll(
        sql="""SELECT 
            SUM(CASE WHEN enable = 'false' THEN 1 ELSE 0 END) AS enable_false_count,
            SUM(CASE WHEN enable = 'true' THEN 1 ELSE 0 END) AS enable_true_count
        FROM 
            gxy_user;""")


def WeeklyFun():
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
            weeklydata;""")


def MonthFun():
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
            monthdata""")
