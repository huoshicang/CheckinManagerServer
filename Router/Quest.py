from flask import Blueprint, request

from Api.Quest.GetCheckQuest import GetCheckQuest
from component import BAD_REQUEST

# 创建一个蓝图对象
Quest = Blueprint('Quest', __name__)


@Quest.route(rule='/quest/check', methods=['POST'])
def CheckQuest():
    """
    获取用户签到信息
    """
    if request.get_data() == b'':
        return BAD_REQUEST()

    data = None

    if 'application/json' in request.content_type:
        data = request.json
    elif 'multipart/form-data' in request.content_type:
        data = request.form
    # or not data["role"]
    if data == {}  or not data["name"]:
        return BAD_REQUEST()

    return GetCheckQuest(Data=data)


# @UserCheck.route(rule='/user/ModifyInfo', methods=['POST'])
# def ModifyInfo():
#     """
#     修改签到用户信息
#     """
#     if request.get_data() == b'':
#         return BAD_REQUEST()
#
#     data = None
#
#     if 'application/json' in request.content_type:
#         data = request.json
#     elif 'multipart/form-data' in request.content_type:
#         data = request.form
#
#     for key in data.keys():
#
#         if key in ['latitude', 'longitude', 'note']:
#             continue
#
#         if data[key] is "":
#             return BAD_REQUEST()
#
#     return Modify(Data=data)


# @UserCheck.route(rule='/user/delCheck', methods=['POST'])
# def DelInfo():
#     """
#     删除签到用户
#     """
#
#     if request.get_data() == b'':
#         return BAD_REQUEST()
#
#     data = None
#
#     if 'application/json' in request.content_type:
#         data = request.json
#     elif 'multipart/form-data' in request.content_type:
#         data = request.form
#
#     if data == {} or not data["id"] or not data["name"]:
#         return BAD_REQUEST()
#
#     return DelCheck(Data=data)
