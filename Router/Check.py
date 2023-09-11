from Api.CheckIn.GetCheckInfo import GetCheckInfo
from flask import Blueprint, request

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