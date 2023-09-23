
from flask import Blueprint, request

from Api.Weekly.GetWeeklyData import GetWeekly
from Api.Weekly.DelWeeklyData import DelWeekly
from component import BAD_REQUEST

# 创建一个蓝图对象
WeeklyRouter = Blueprint('WeeklyRouter', __name__)


@WeeklyRouter.route(rule='/Weekly/data', methods=['POST'])
def Get_Weekly():
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

    if data == {}:
        return BAD_REQUEST()

    return GetWeekly(Data=data)


@WeeklyRouter.route(rule='/Weekly/del', methods=['POST'])
def Del_Weekly():
    """
    删除周报信息
    """

    if request.get_data() == b'':
        return BAD_REQUEST()

    data = None

    if 'application/json' in request.content_type:
        data = request.json
    elif 'multipart/form-data' in request.content_type:
        data = request.form

    if data == {} or not data['username'] or not data['weekly_id'] or not data['title']:
        return BAD_REQUEST()

    return DelWeekly(Data=data)
