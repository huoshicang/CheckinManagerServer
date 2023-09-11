from Api import LogIn, LogUp, LogOut
from flask import Blueprint, request

from component import BAD_REQUEST

# 创建一个蓝图对象
UserLogRouter = Blueprint('UserLogRouter', __name__)


@UserLogRouter.route(rule='/user/Login', methods=['POST'])
def UserLogIn():
    """
    登录
    """
    if request.get_data() == b'':
        return BAD_REQUEST()

    data = None

    if 'application/json' in request.content_type:
        data = request.json
    elif 'multipart/form-data' in request.content_type:
        data = request.form

    if data == {} or not data["userName"] or not data["passWord"]:
        return BAD_REQUEST()

    return LogIn(Data=data)


@UserLogRouter.route(rule='/user/Logup', methods=['POST'])
def UserLogUp():
    """
    注册
    """
    if request.get_data() == b'':
        return BAD_REQUEST()

    data = None

    if 'application/json' in request.content_type:
        data = request.json
    elif 'multipart/form-data' in request.content_type:
        data = request.form

    if data == {} or not data["userName"] or not data["phone"] or not data["passWord"]:
        return BAD_REQUEST()

    return LogUp(Data=data)


#
# @UserLogRouter.route(rule='/user/logout', methods=['GET'])
# def UserLogOut():
#     UserName = request.args.get('username')
#
#     if not UserName:
#         return BAD_REQUEST()
#
#     return LogOut(UserName=UserName)
