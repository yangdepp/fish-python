from flask import Flask, make_response

__author__ = 'yang'

app = Flask(__name__)
app.config.from_object('config')


# mvc的概念中，视图函数就是c的意思
@app.route('/hello')
def hello():
    # 基于类的视图（即插视图）
    # status code :200 404 301
    # content-type http headers
    # content-type = text/html （默认）
    # response
    headers = {
        'content-type': 'application/json',
        'location': 'http://www.baidu.com'
    }
    response = make_response('<html></html>', 301)
    response.headers = headers
    return response
    # return '<a href="http://baidu.com">哈哈哈</a>'


if __name__ == '__main__':
    # 生产环境下，fish-python不是入口文件
    # 生产环境下，加此判断，不会启动flask服务器
    app.run(host='0.0.0.0', debug=app.config['DEBUG'])
