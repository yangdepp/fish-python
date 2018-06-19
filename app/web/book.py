# create by 'yang' in 2018/6/16

from flask import jsonify, request

from helper import is_isbn_or_key
from yushu_book import YuShuBook
from . import web
from app.forms.book import SearchForm

__author__ = 'yang'


@web.route('/book/search')
def search():
    # 调用校验层
    form = SearchForm(request.args)
    if form.validate():
        q = form.q.data.strip()
        page = form.page.data
        isbn_or_key = is_isbn_or_key(q)
        if isbn_or_key == 'isbn':
            result = YuShuBook.search_by_isbn(q)
        else:
            result = YuShuBook.search_by_keyword(q, page)
        return jsonify(result)
    else:
        return jsonify(form.errors)
