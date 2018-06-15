from flask import Flask

__author__ = 'yang'

app = Flask(__name__)
app.config.from_object('config')


# mvc的概念中，视图函数就是c的意思
@app.route('/hello')
def hello():
    # 基于类的视图（即插视图）
    return '<a href="http://baidu.com">哈哈哈</a>'


if __name__ == '__main__':
    # 生产环境下，fish-python不是入口文件
    # 生产环境下，加此判断，不会启动flask服务器
    app.run(host='0.0.0.0', debug=app.config['DEBUG'])

