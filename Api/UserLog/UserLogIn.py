import datetime

from component import QueryDataFetchOne, Update, HTTP_STATUS_CODES, INTERNAL_SERVER_ERROR
import jwt


def LogIn(Data: dict, ) -> dict:
    """
    登录系统
    """
    username = Data['userName']
    password = Data['passWord']

    try:
        Query = LookUp(params=tuple((username,)))

        if Query is None:
            return {
                "code": HTTP_STATUS_CODES['NOT_FOUND'],  # 使用 HTTP 404 表示未找到
                "data": [],
                "message": "用户名不存在"
            }

        elif Query['password'] == password:

            obj = {
                "username": Query["username"],
                "phone": Query["phone"],
                'exp': (datetime.datetime.utcnow() + datetime.timedelta(hours=12)).timestamp()
            }

            token = Up(obj=obj, username=username)  # 生成token

            Query['token'] = token  # 返回token

            del Query["password"]  # 脱敏

            return {
                "code": HTTP_STATUS_CODES['OK'],
                "data": Query,
                "message": "登录成功"
            }
        else:
            return {
                "code": HTTP_STATUS_CODES['UNAUTHORIZED'],
                "data": [],
                "message": "密码不正确"
            }

    except:
        return INTERNAL_SERVER_ERROR()


def LookUp(params):
    """
    查询系统用户信息
    """
    return QueryDataFetchOne(
        sql="""SELECT
        username, # 用户名
        phone, # 手机号
        password,# 密码
        role, # 角色
        gxy_info # 工学云是否有信息
        FROM sys_user
        WHERE username = %s;""",
        params=params)


def Up(obj, username):
    """
    更新token
    """
    token = jwt.encode(obj, "Miss", algorithm='HS256')
    Update(f"""UPDATE sys_user SET 
    token = '{token}'
    WHERE 
    username = %s;""", params=tuple((username,)))
    return token
