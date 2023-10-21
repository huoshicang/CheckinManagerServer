import datetime
import json
import logging

import jwt
from flask import Flask, request
from flask_cors import CORS

from Router.Month import MonthRouter
from Router.User import UserRouter
from Router.Check import UserCheck
from Router.UserLog import UserLogRouter
from Router.Weekly import WeeklyRouter
# from Router.Quest import Quest
from Router.Info import InfoRouter
from component import HTTP_STATUS_CODES, BAD_REQUEST

app = Flask(__name__)
app.register_blueprint(UserRouter)
app.register_blueprint(UserCheck)
app.register_blueprint(UserLogRouter)
app.register_blueprint(WeeklyRouter)
app.register_blueprint(MonthRouter)
# app.register_blueprint(Quest)
app.register_blueprint(InfoRouter)
app.template_folder = 'templates'

CORS(app, resources={"*": {"origins": "*"}})


@app.route(rule='/test', methods=['POST', "GET"])
def Test():
    return {
        "code": 200,
        "data": "服务运行在：127.0.0.1:7860",
        "message": "成功"
    }


@app.route(rule='/log', methods=['POST'])
def Log():
    Lis = []
    # if request.get_data() == b'':
    #     return BAD_REQUEST()
    
    # data = None
    
    # if 'application/json' in request.content_type:
    #     data = request.json
    # elif 'multipart/form-data' in request.content_type:
    #     data = request.form
    file_path = f"{datetime.date.today()}.log"  # 替换成你的日志文件路径
    lines_to_read = 100

    # 使用deque来存储最新的100行
    from collections import deque

    recent_lines = deque(maxlen=lines_to_read)

    # 打开文件并逐行读取
    with open(file_path, 'r') as file:
        for line in file:
            recent_lines.append(line.strip())

    # recent_lines现在包含了文件的最新100行
    for line in recent_lines:
        Lis.append(line)

    return {
        'data': Lis
    }


# 处理请求前
@app.before_request
def before_request():
    # logging.info("===" * 30)
    # logging.info(request.environ.get('REQUEST_METHOD'), request.environ.get('PATH_INFO'), request.environ.get('SERVER_PROTOCOL'))
    # logging.info(request.environ.get('REMOTE_ADDR'))

    if ('/user/Login' == request.path or
            '/user/Logup' == request.path or
            'user/change' == request.path or
            '/test' == request.path or
            '/user/AddInfo' == request.path or
            '/user/UpLog' == request.path):
        pass

    else:

        Authorization = request.headers.get('Authorization')

        try:
            # 使用密钥解析JWT令牌
            token = jwt.decode(Authorization, "Miss", algorithms=['HS256'])
            # 获取token
            # logging.info(request.environ.get('HTTP_AUTHORIZATION'))
            # 时间戳转时间
            # token['exp'] = datetime.datetime.fromtimestamp(token['exp']).strftime("%Y-%m-%d %H:%M:%S")
            # logging.info(token)

        except jwt.ExpiredSignatureError:
            return {
                "code": HTTP_STATUS_CODES['UNAUTHORIZED'],  # 使用 HTTP 404 表示未找到
                "data": [],
                "message": "token已过期"
            }
        except jwt.InvalidTokenError:
            return {
                "code": HTTP_STATUS_CODES['UNAUTHORIZED'],  # 使用 HTTP 404 表示未找到
                "data": [],
                "message": "无效的token"
            }


@app.after_request
def set_response_charset(response):
    response.headers['Content-Type'] = 'text/plain; charset=utf-8'
    return response


if __name__ == '__main__':
    logging.basicConfig(
        level=logging.DEBUG,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        filename=f"{datetime.date.today()}.log",
        filemode='a',
        encoding='utf-8',
    )
    log = logging.getLogger(__name__)

    msg = r"""
                          _ooOoo_
                         o8888888o
                         88" . "88
                         (| -_- |)
                          O\ = /O
                      ____/`---'\____
                    .   ' \\| |// `.
                     / \\||| : |||// \
                   / _||||| -:- |||||- \
                     | | \\\ - /// | |
                   | \_| ''\---/'' | |
                    \ .-\__ `-` ___/-. /
                 ___`. .' /--.--\ `. . __
              ."" '< `.___\_<|>_/___.' >'"".
             | | : `- \`.;`\ _ /`;.`/ - ` : | |
               \ \ `-. \_ __\ /__ _/ .-` / /
       ======`-.____`-.___\_____/___.-`____.-'======
                          `=---='

       .............................................
              佛祖保佑             永无BUG
       .............................................
           佛曰:
           写字楼里写字间          写字间里程序员；
           程序人员写程序          又拿程序换酒钱。
           酒醒只在网上坐          酒醉还来网下眠；
           酒醉酒醒日复日          网上网下年复年。
           但愿老死电脑间          不愿鞠躬老板前；
           奔驰宝马贵者趣          公交自行程序员。
           别人笑我忒疯癫          我笑自己命太贱；
           不见满街漂亮妹          哪个归得程序员？
    """

    print(msg)
    # print("运行在7860")
    app.run(host='0.0.0.0', port=7860, debug=True)