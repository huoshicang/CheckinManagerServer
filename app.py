import datetime
import logging

import jwt
from flask import Flask, render_template, request, abort
from flask_cors import CORS


from Router.User import UserRouter
from Router.UserLog import UserLogRouter
from component import HTTP_STATUS_CODES, BAD_REQUEST

app = Flask(__name__)
app.register_blueprint(UserRouter)
app.register_blueprint(UserLogRouter)
app.template_folder = 'templates'
CORS(app, resources={"*": {"origins": "*"}})


@app.route(rule='/test', methods=['POST', "GET"])
def Test():
    return {
        "code": 200,
        "data": "服务运行在：127.0.0.1:7860",
        "message": "成功"
    }


@app.route(rule='/html')
def index():
    return render_template('index.html')


# 处理请求前
@app.before_request
def before_request():
    if ('/user/Login' in request.url or
            '/user/Logup' in request.url or
            '/test' in request.url or
            '/user/AddInfo' in request.url or
            '/user/UpLog' in request.url or
            '/html' in request.url):
        pass

    else:
        Authorization = request.headers.get('Authorization')

        try:
            # 使用密钥解析JWT令牌
            jwt.decode(Authorization, "Miss", algorithms=['HS256'])
            pass
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
    response.headers['Content-Type'] = 'application/json; charset=utf-8'
    return response


if __name__ == '__main__':
    # logging.basicConfig(
    #     level=logging.DEBUG,
    #     format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    #     filename=f"{datetime.date.today()}.log",
    #     filemode='a',
    #     encoding='utf-8',
    # )
    # logging.getLogger(__name__)

    print("运行在7860端口")
    app.run(host='127.0.0.1', port=7860, debug=True)

"""
@app.route('/example', methods=['GET', 'POST'])
def example():
    if request.method == 'GET':
        return 'This is a GET request'
    elif request.method == 'POST':
        return 'This is a POST request'


@app.route('/search')
def search():
    query = request.args.get('q')
    return f'Search query: {query}'


@app.route('/submit', methods=['POST'])
def submit():
    username = request.form.get('username')
    password = request.form.get('password')
    return f'Username: {username}, Password: {password}'


@app.route('/user_agent')
def user_agent():
    user_agent = request.headers.get('User-Agent')
    return f'User-Agent: {user_agent}'


@app.route('/json_data', methods=['POST'])
def json_data():
    data = request.get_json()
    return f'Received JSON data: {data}'

"""
