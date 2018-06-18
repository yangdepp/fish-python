# create by 'yang' in 2018/6/16

from flask import jsonify

from helper import is_isbn_or_key
from yushu_book import YuShuBook
from . import web

__author__ = 'yang'


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
