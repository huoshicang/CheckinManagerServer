from component import QueryDataFetchOne, HTTP_STATUS_CODES, INTERNAL_SERVER_ERROR, Update
from component.mysql import Indate


def ModifyMonth(Data: dict) -> dict:
    """
    添加月报
    """
    weekly_id = Data['month_id']
    title = Data['title']
    content = Data['content']
    username = Data['username']
    enable = Data['enable']
    weekly_time = Data['month_time']

    QueryOne = LookUpOne(params=tuple((weekly_id,)))

    if QueryOne is None:
        return {
            "code": HTTP_STATUS_CODES['BAD_REQUEST'],
            "data": [],
            "message": "周报信息不存在"
        }

    try:
        ModifyInfo = Add(params=tuple((
            title,
            content,
            username,
            enable,
            weekly_time,
            weekly_id,
        )))

        if ModifyInfo == "操作成功":
            return {
                "code": HTTP_STATUS_CODES['OK'],
                "data": [],
                "message": "修改成功"
            }
        else:
            return {
                "code": HTTP_STATUS_CODES['INTERNAL_SERVER_ERROR'],
                "data": [],
                "message": f"修改失败：{ModifyInfo}"
            }


    except:
        return INTERNAL_SERVER_ERROR()


def LookUpOne(params):
    """
    获取月报信息
    """
    return QueryDataFetchOne(
        sql="""SELECT
        title
        FROM monthdata
        WHERE month_id = %s;""",
        params=params)


def Add(params):
    """
    添加月报数据
    """
    return Update(Sql="""UPDATE monthdata SET
                title = %s,
                content = %s,
                username = %s,
                enable = %s,
                month_time = %s
                WHERE month_id = %s;""", params=params)
