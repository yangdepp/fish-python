# create by 'yang' in 2018/6/16
from flask import Flask

__author__ = 'yang'


def create_app():
    app = Flask(__name__)
    app.config.from_object('config')
    return app
