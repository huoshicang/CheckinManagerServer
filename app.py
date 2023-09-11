from flask import Flask, render_template
from flask_cors import CORS

from Router.UserLog import UserLogRouter

app = Flask(__name__)
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


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=7860, debug=True)