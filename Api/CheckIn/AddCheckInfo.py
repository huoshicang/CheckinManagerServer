from component import QueryDataFetchOne, HTTP_STATUS_CODES, INTERNAL_SERVER_ERROR, Update
from component.mysql import Indate


def AddCheckInfo(Data: dict) -> dict:
    """
    添加签到用户信息
    """
    enable = Data['enable']
    name = Data['name']
    phone = Data['phone']
    password = Data['password']
    country = Data['country']
    province = Data['province']
    city = Data['city']
    area = Data['area']
    address = Data['address']
    longitude = Data['longitude']
    latitude = Data['latitude']
    note = Data['note']
    typee = Data['type']
    pushKey = Data['pushKey']

    QueryOne = LookUpOne(params=tuple((name,)))

    if QueryOne is not None:
        return {
            "code": HTTP_STATUS_CODES['BAD_REQUEST'],
            "data": [],
            "message": "用户已存在"
        }

    try:
        AddInfo = Add(params=tuple((
            enable,
            name,
            phone,
            password,
            country,
            province,
            city,
            area,
            address,
            longitude,
            latitude,
            note,
            typee,
            pushKey,
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
    获取用户信息
    """
    return QueryDataFetchOne(
        sql="""SELECT
        id,
        name
        FROM gxy_user
        WHERE name = %s;""",
        params=params)


def Add(params):
    """
    添加用户数据
    """
    return Indate(Sql=f"""INSERT INTO gxy_user
        (enable,
        name,
        phone ,
        password ,
        country,
        province ,
        city ,
        area ,
        address ,
        longitude ,
        latitude ,
        note ,
        type,
        pushKey)
        VALUES
        (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s);""", params=params)
