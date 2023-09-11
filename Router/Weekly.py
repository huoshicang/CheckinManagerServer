from Api.Weekly.GetWeeklyData import WeeklyData
from flask import Blueprint, request

from component import BAD_REQUEST

# 创建一个蓝图对象
WeeklyRouter = Blueprint('WeeklyRouter', __name__)


@WeeklyRouter.route(rule='/getWeekly/data', methods=['POST'])
def GetWeekly():
    """
    获取用户周报信息
    """

    if request.get_data() == b'':
        return BAD_REQUEST()

    data = None

    if 'application/json' in request.content_type:
        data = request.json
    elif 'multipart/form-data' in request.content_type:
        data = request.form

    if data == {} or not data["username"]:
        return BAD_REQUEST()

    return WeeklyData(Data=data)
