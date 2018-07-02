# create by 'yang' in 2018/6/16
import json

from flask import jsonify, request, render_template

from app.libs.helper import is_isbn_or_key
from app.spider.yushu_book import YuShuBook
from app.view_models.book import BookCollection
from . import web
from app.forms.book import SearchForm

__author__ = 'yang'


@web.route('/book/search')
def search():
    # 调用校验层
    form = SearchForm(request.args)
    books = BookCollection()

    if form.validate():
        q = form.q.data.strip()
        page = form.page.data
        isbn_or_key = is_isbn_or_key(q)
        yushu_book = YuShuBook()

        if isbn_or_key == 'isbn':
            yushu_book.search_by_isbn(q)
        else:
            yushu_book.search_by_keyword(q, page)

        books.fill(yushu_book, q)
        return json.dumps(books, default=lambda o: o.__dict__)
    else:
        return jsonify(form.errors)


@web.route('/test')
def test():
    r = {
        'name': '',
        'age': 25
    }
    # 引入模板
    return render_template('test.html', data=r)
