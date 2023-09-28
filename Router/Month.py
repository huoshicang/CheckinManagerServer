from flask import Blueprint, request

from Api.Month.GetMonthData import GetMonth
from Api.Month.DelMonthData import DelMonth
from Api.Month.AddMonthData import AddMonth
from Api.Month.ModifyMonthData import ModifyMonth
from component import BAD_REQUEST

# 创建一个蓝图对象
MonthRouter = Blueprint('MonthRouter', __name__)


@MonthRouter.route(rule='/Month/data', methods=['POST'])
def Get_Month():
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

    return GetMonth(Data=data)


@MonthRouter.route(rule='/Month/del', methods=['POST'])
def Del_Month():
    """
    删除月报信息
    """

    if request.get_data() == b'':
        return BAD_REQUEST()

    data = None

    if 'application/json' in request.content_type:
        data = request.json
    elif 'multipart/form-data' in request.content_type:
        data = request.form

    if data == {} or not data['username'] or not data['month_id'] or not data['title']:
        return BAD_REQUEST()

    return DelMonth(Data=data)


@MonthRouter.route(rule='/Month/add', methods=['POST'])
def Add_Month():
    """
    添加周报信息
    """
    if request.get_data() == b'':
        return BAD_REQUEST()

    data = None

    if 'application/json' in request.content_type:
        data = request.json
    elif 'multipart/form-data' in request.content_type:
        data = request.form

    if len(data) == 0:
        return BAD_REQUEST()

    return AddMonth(Data=data)


@MonthRouter.route(rule='/Month/modify', methods=['POST'])
def Modify_Month():
    """
    编辑周报信息
    """
    if request.get_data() == b'':
        return BAD_REQUEST()

    data = None

    if 'application/json' in request.content_type:
        data = request.json
    elif 'multipart/form-data' in request.content_type:
        data = request.form

    if (data == {}
            or not data['month_id']
            or not data['title']
            or not data['content']
            or not data['username']
            or not data['enable']
            or not data['month_time']):
        return BAD_REQUEST()

    return ModifyMonth(Data=data)
