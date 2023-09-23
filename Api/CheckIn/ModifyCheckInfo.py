from component import QueryDataFetchOne, HTTP_STATUS_CODES, Update
from component.status_codes import NOT_FOUND, BAD_REQUEST2


def Modify(Data: dict):
    id = Data['id']
    enable = Data['enable']
    name = Data['name']
    phone = Data['phone']
    password = Data['password']
    country = Data['country']
    province = Data['province']
    city = Data['city']
    area = Data['area']
    address = Data['address']
    latitude = Data['latitude']
    longitude = Data['longitude']
    note = Data['note']
    type = Data['type']
    pushKey = Data['pushKey']

    print('enable',enable)

    passwordMes = Administrator(params=tuple((id, name, phone)))

    if passwordMes is None:
        return NOT_FOUND()


    try:
        SetMsg = Set(params=tuple((enable,
                                   name,
                                   phone,
                                   country,
                                   province,
                                   city,
                                   area,
                                   address,
                                   latitude,
                                   longitude,note,type,pushKey, id, password, password,)))

        if SetMsg == "操作成功":
            return {
                "code": HTTP_STATUS_CODES['OK'],
                "data": [],
                "message": "修改成功"
            }
        else:
            return {
                "code": HTTP_STATUS_CODES['INTERNAL_SERVER_ERROR'],
                "data": [],
                "message": f"修改失败：{SetMsg}"
            }

    except:
        return BAD_REQUEST2()


def Administrator(params):
    """
    获取角色
    """
    return QueryDataFetchOne(
        sql="""SELECT
        password
        FROM
        gxy_user
        WHERE id = %s AND name = %s AND phone = %s;""", params=params)


def Set(params):
    """
    获取角色
    """
    return Update(Sql="""UPDATE gxy_user SET
                enable = %s,
                name = %s,
                phone = %s,
                country = %s,
                province = %s,
                city = %s,
                area = %s,
                address = %s,
                latitude = %s,
                longitude = %s,
                note = %s,
                type = %s,
                pushKey = %s
                WHERE id = %s
                AND (password = %s OR %s = '');""", params=params)
