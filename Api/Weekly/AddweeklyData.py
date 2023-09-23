from component import QueryDataFetchOne, HTTP_STATUS_CODES, INTERNAL_SERVER_ERROR, Update
from component.mysql import Indate


def AddWeekly(Data: dict) -> dict:
    """
    添加签到用户信息
    """
    title = Data['title']
    content = Data['content']
    username = Data['username']
    weekly_time = Data['weekly_time']

    QueryOne = LookUpOne(params=tuple((username,title,)))

    if QueryOne is not None:
        return {
            "code": HTTP_STATUS_CODES['BAD_REQUEST'],
            "data": [],
            "message": "周报信息已存在"
        }

    try:
        AddInfo = Add(params=tuple((
            username,
            title,
            content,
            weekly_time
        )))

        if AddInfo == "操作成功":
            return {
                "code": HTTP_STATUS_CODES['OK'],
                "data": [],
                "message": "添加成功"
            }
        else:
            return {
                "code": HTTP_STATUS_CODES['INTERNAL_SERVER_ERROR'],
                "data": [],
                "message": f"添加失败：{AddInfo}"
            }


    except:
        return INTERNAL_SERVER_ERROR()


def LookUpOne(params):
    """
    获取周报信息
    """
    return QueryDataFetchOne(
        sql="""SELECT
        content
        FROM weeklydata
        WHERE username = %s AND title = %s;""",
        params=params)


def Add(params):
    """
    添加周报数据
    """
    return Indate(Sql=f"""INSERT INTO weeklydata
        (username, title, content, weekly_time)
        VALUES
        (%s,%s,%s,%s);""", params=params)
