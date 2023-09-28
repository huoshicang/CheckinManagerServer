from component import QueryDataFetchOne, Update
from component.status_codes import NOT_FOUND, BAD_REQUEST2, INTERNAL_SERVER_ERROR, HTTP_STATUS_CODES


def DelMonth(Data: dict) -> dict:
    """
    删除月报
    """
    delid = Data['month_id']
    username = Data['username']
    Deltitle = Data['title']

    title = AdministratorSys(params=tuple((delid, username, Deltitle)))

    if title is None:
        return NOT_FOUND()

    try:
        DelReq = Del(params=tuple((delid, username, Deltitle)))

        if DelReq == "操作成功":
            return {
                "code": HTTP_STATUS_CODES['OK'],
                "data": [],
                "message": "删除成功"
            }
        else:
            return {
                "code": HTTP_STATUS_CODES['INTERNAL_SERVER_ERROR'],
                "data": [],
                "message": f"删除失败：{DelReq}"
            }
    except:
        return INTERNAL_SERVER_ERROR()


def AdministratorSys(params):
    """
    月报信息
    """
    return QueryDataFetchOne(
        sql="""SELECT title FROM monthdata
        WHERE
            month_id = %s
        AND
            username = %s
        AND
            title = %s;""", params=params)


def Del(params):
    """
    删除月报
    """
    return Update(Sql="""UPDATE monthdata
                SET is_deleted = true
                WHERE 
                    month_id = %s
                AND
                    username = %s
                AND
                    title = %s;""", params=params)
