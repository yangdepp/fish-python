from flask import Flask, jsonify
from helper import is_isbn_or_key
from yushu_book import YuShuBook

__author__ = 'yang'

app = Flask(__name__)
app.config.from_object('config')


# mvc的概念中，视图函数就是c的意思
@app.route('/book/search/<q>/<page>')
def search(q, page):
    """
        q：普通关键字  isbn
        page
    """
    isbn_or_key = is_isbn_or_key(q)
    if isbn_or_key == 'isbn':
        result = YuShuBook.search_by_isbn(q)
    else:
        result = YuShuBook.search_by_keyword(q)
    return jsonify(result)
    # return json.dumps(result), 200, {'content-type': 'application/json'}


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=app.config['DEBUG'])
