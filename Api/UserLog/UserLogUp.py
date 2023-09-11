from component import Update, HTTP_STATUS_CODES, QueryDataFetchOne, INTERNAL_SERVER_ERROR


def LogUp(Data: dict) -> dict:
    """
    添加系统用户
    """
    username = Data["userName"]
    phone = Data["phone"]
    password = Data["passWord"]

    try:
        existing_user = LookUp(params=tuple((username, phone)))

        if existing_user:
            if existing_user["username"] == username:
                return {
                    "code": HTTP_STATUS_CODES['BAD_REQUEST'],
                    "data": [],
                    "message": "用户名已存在"
                }
            elif existing_user['phone'] == phone:
                return {
                    "code": HTTP_STATUS_CODES['BAD_REQUEST'],
                    "data": [],
                    "message": "手机号已存在"
                }

        message = Add(params=tuple((username, phone, password)))

        if message == "操作成功":
            return {
                "code": HTTP_STATUS_CODES['OK'],
                "data": [],
                "message": "注册成功"
            }
        else:
            return {
                "code": HTTP_STATUS_CODES['INTERNAL_SERVER_ERROR'],
                "data": [],
                "message": f"注册失败：{message}"
            }
    except:
        return INTERNAL_SERVER_ERROR()


def LookUp(params):
    """
    查询系统用户
    """
    return QueryDataFetchOne(sql="""SELECT
     username,
     phone
     FROM sys_user
     WHERE username = %s OR phone = %s;""", params=params)


def Add(params):
    """
    添加系统用户
    """
    return Update(Sql=f"""INSERT INTO sys_user
    (username,
    phone,
    password)
    VALUES
    (%s, %s, %s);""", params=params)
