# create by 'yang' in 2018/6/16
from flask import Blueprint

__author__ = 'yang'

# 蓝图 blueprint  蓝本
# 第一个参数是蓝图的名称
# 第二个参数是蓝图所在的包
web = Blueprint('web', __name__)

from app.web import book
from app.web import user
