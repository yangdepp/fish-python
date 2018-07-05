from . import web


__author__ = 'yang'


@web.route('/')
def index():
    return 'hello yang'


@web.route('/personal')
def personal_center():
    pass
