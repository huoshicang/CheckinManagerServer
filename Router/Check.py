from flask import Blueprint, request

from Api import Modify, GetCheckInfo, DelCheck
from component import BAD_REQUEST

# 创建一个蓝图对象
UserCheck = Blueprint('UserCheck', __name__)


@UserCheck.route(rule='/user/CheckInfo', methods=['GET'])
def GetCheck():
    """
    获取用户签到信息
    """
    UserName = request.args.get('username')

    if UserName is not None:
        return GetCheckInfo(UserName=UserName)
    else:
        return BAD_REQUEST()


@UserCheck.route(rule='/user/ModifyInfo', methods=['POST'])
def ModifyInfo():
    """
    修改签到用户信息
    """
    if request.get_data() == b'':
        return BAD_REQUEST()

    data = None

    if 'application/json' in request.content_type:
        data = request.json
    elif 'multipart/form-data' in request.content_type:
        data = request.form

    for key in data.keys():

        if key in ['latitude', 'longitude', 'note']:
            continue

        if data[key] is "":
            return BAD_REQUEST()

    return Modify(Data=data)


@UserCheck.route(rule='/user/delCheck', methods=['POST'])
def DelInfo():
    """
    删除签到用户
    """

    if request.get_data() == b'':
        return BAD_REQUEST()

    data = None

    if 'application/json' in request.content_type:
        data = request.json
    elif 'multipart/form-data' in request.content_type:
        data = request.form

    if data == {} or not data["id"] or not data["name"]:
        return BAD_REQUEST()

    return DelCheck(Data=data)
