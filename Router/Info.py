from flask import Blueprint, request

from Api.UserInfo import GetUser
from Api.AdminInfo import GetAdmin
from component import BAD_REQUEST

# 创建一个蓝图对象
InfoRouter = Blueprint('InfoRouter', __name__)


@InfoRouter.route(rule='/info/user', methods=['POST'])
def GetInfoUser():
    """
    获取用户信息
    """

    if request.get_data() == b'':
        return BAD_REQUEST()

    data = None

    if 'application/json' in request.content_type:
        data = request.json
    elif 'multipart/form-data' in request.content_type:
        data = request.form

    if data == {} or not data['username']:
        return BAD_REQUEST()

    return GetUser(Data=data)


@InfoRouter.route(rule='/info/admin', methods=['POST'])
def GetInfoAdmin():
    """
    获取用户信息
    """

    if request.get_data() == b'':
        return BAD_REQUEST()

    data = None

    if 'application/json' in request.content_type:
        data = request.json
    elif 'multipart/form-data' in request.content_type:
        data = request.form

    if data == {} or not data['username']:
        return BAD_REQUEST()

    return GetAdmin(Data=data)
