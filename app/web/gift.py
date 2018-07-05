from flask import current_app, flash, redirect, url_for

from app.models.base import db
from app.models.gift import Gift
from . import web
from flask_login import login_required, current_user

__author__ = 'yang'


@web.route('/my/gifts')
@login_required
def my_gifts():
    return 'My Gifts'


@web.route('/gifts/book/<isbn>')
@login_required
def save_to_gifts(isbn):
    if current_user.can_save_to_list(isbn):
        # 事务，操作了两张表，因此要保证数据的一致性
        # rollback 数据库回滚
        with db.auto_commit():
            gift = Gift()
            gift.isbn = isbn
            gift.uid = current_user.id

            # current_user.beans += 0.5
            current_user.beans += current_app.config['BEANS_UPLOAD_ONE_BOOK']
            db.session.add(gift)

    else:
        flash('这本书已经添加至你的赠送清单或已存在于你的心愿清单，请不要重复操作')
    return redirect(url_for('web.book_detail', isbn=isbn))


@web.route('/gifts/<gid>/redraw')
def redraw_from_gifts(gid):
    pass
