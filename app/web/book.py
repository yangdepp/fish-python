# create by 'yang' in 2018/6/16

from flask import jsonify, Blueprint

from helper import is_isbn_or_key
from yushu_book import YuShuBook

__author__ = 'yang'

# 蓝图 blueprint  蓝本
# 第一个参数是蓝图的名称
# 第二个参数是蓝图所在的包
web = Blueprint('web', __name__)


@web.route('/book/search/<q>/<page>')
def search(q, page):
    """
        q：普通关键字  isbn
        page:当前页数
    """
    isbn_or_key = is_isbn_or_key(q)
    if isbn_or_key == 'isbn':
        result = YuShuBook.search_by_isbn(q)
    else:
        result = YuShuBook.search_by_keyword(q)
    return jsonify(result)
