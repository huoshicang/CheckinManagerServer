from component import QueryDataFetchOne, HTTP_STATUS_CODES, INTERNAL_SERVER_ERROR, Update
from component.mysql import Indate


def AddMonth(Data: dict) -> dict:
    """
    添加月报信息
    """

    info = {
        'totality': len(Data),
        'success': {
            'num': 0,
        },
        # 失败
        'lose': {
          'num': 0,
          'title': []
        },
        # 已存在
        'exist': {
          'num': 0,
          'title': []
        },
        # 缺少参数
        'lack': {
          'num': 0,
          'title': []
        },
    }

    errorList = []

    for i in Data:
        title = i['title']
        content = i['content']
        username = i['username']
        weekly_time = i['weekly_time']

        if title is '' or content is '' or username is '' or weekly_time is None:
            info['lack']['num'] += 1
            if title is '':
                info['lack']['title'].append(username)
            else:
                info['lack']['title'].append(title)
            errorList.append(i)
            continue

        QueryOne = LookUpOne(params=tuple((username, title,)))

        if QueryOne is not None:
            info['exist']['num'] += 1
            info['exist']['title'].append(title)
            continue

        try:
            AddInfo = Add(params=tuple((
                username,
                title,
                content,
                weekly_time
            )))

            if AddInfo == "操作成功":
                info['success']['num'] += 1
            else:
                info['lose']['num'] += 1
                info['lose']['title'].append(title)
                errorList.append(i)

        except:
            return INTERNAL_SERVER_ERROR()

    if info["success"]['num'] == info["totality"]:
        return {
            "code": HTTP_STATUS_CODES['OK'],
            "data": [],
            "message": "添加成功"
        }
    else:
        return {
            "code": HTTP_STATUS_CODES['BAD_REQUEST'],
            "data": errorList,
            "message": info
        }


def LookUpOne(params):
    """
    获取月报信息
    """
    return QueryDataFetchOne(
        sql="""SELECT
        month_id
        FROM monthdata
        WHERE username = %s AND title = %s;""",
        params=params)


def Add(params):
    """
    添加月报数据
    """
    return Indate(Sql=f"""INSERT INTO monthdata
        (username, title, content, month_time)
        VALUES
        (%s,%s,%s,%s);""", params=params)
