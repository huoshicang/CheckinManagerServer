from flask import Blueprint, request

from Api.CheckIn.AddCheckInfo import AddCheckInfo

from Api.User.ChangePassword import ChangePassword
from Api.User.GetUserInfo import GetUserInfo
from Api.User.ModifyUserInfo import Modify
from Api.User.DelUserInfo import DelUserInfo
from Api.User.ResetPassword import ResetPassword
from Api.User.UpUserInfo import UpInfo


from component import BAD_REQUEST

# 创建一个蓝图对象
UserRouter = Blueprint('UserRouter', __name__)


@UserRouter.route(rule='/user/AddInfo', methods=['POST'])
def AddInfo():
    """
    添加签到用户
    """
    if request.get_data() == b'':
        return BAD_REQUEST()

    data = None

    if 'application/json' in request.content_type:
        data = request.json
    elif 'multipart/form-data' in request.content_type:
        data = request.form

    for i in data:
        if ("latitude" == i or
                "note" == i or
                "longitude" == i):
            continue
        if data[i] == '':
            return BAD_REQUEST()

    return AddCheckInfo(Data=data)


@UserRouter.route(rule='/user/UpLog', methods=['GET'])
def UpLog():
    """
    修改用户的信息标识
    """
    UserName = request.args.get('username')

    if UserName is not None:
        return UpInfo(UserName=UserName)
    else:
        return BAD_REQUEST()


@UserRouter.route(rule='/user/info', methods=['POST'])
def UserInfo():
    """
    获取系统用户
    """

    if request.get_data() == b'':
        return BAD_REQUEST()

    data = None

    if 'application/json' in request.content_type:
        data = request.json
    elif 'multipart/form-data' in request.content_type:
        data = request.form

    return GetUserInfo(Data=data)


@UserRouter.route(rule='/user/delSys', methods=['POST'])
def DelInfo():
    """
    删除系统用户
    """

    if request.get_data() == b'':
        return BAD_REQUEST()

    data = None

    if 'application/json' in request.content_type:
        data = request.json
    elif 'multipart/form-data' in request.content_type:
        data = request.form

    if data == {} or not data["id"] or not data["username"]:
        return BAD_REQUEST()

    return DelUserInfo(Data=data)


@UserRouter.route(rule='/user/modify', methods=['POST'])
def ModifyInfo():
    """
    修改系统用户信息
    """
    if request.get_data() == b'':
        return BAD_REQUEST()

    data = None

    if 'application/json' in request.content_type:
        data = request.json
    elif 'multipart/form-data' in request.content_type:
        data = request.form

    if data == {} or not data["id"] or not data["phone"] or not data["username"]:
        return BAD_REQUEST()

    return Modify(Data=data)


@UserRouter.route(rule='/user/reset', methods=['POST'])
def ResetPassrowd():
    """
    重置密码
    """
    if request.get_data() == b'':
        return BAD_REQUEST()

    data = None

    if 'application/json' in request.content_type:
        data = request.json
    elif 'multipart/form-data' in request.content_type:
        data = request.form

    if data == {} or not data["id"] or not data["username"]:
        return BAD_REQUEST()

    return ResetPassword(Data=data)


@UserRouter.route(rule='/user/change', methods=['POST'])
def ChangetPassrowd():
    """
    修改密码
    """
    if request.get_data() == b'':
        return BAD_REQUEST()

    data = None

    if 'application/json' in request.content_type:
        data = request.json
    elif 'multipart/form-data' in request.content_type:
        data = request.form

    if data == {} or not data["userName"] or not data["passWord"] or not data["phone"]:
        return BAD_REQUEST()

    return ChangePassword(Data=data)




