# create by 'yang' in 2018/6/16
from wtforms import Form, StringField, IntegerField
from wtforms.validators import length, NumberRange

__author__ = 'yang'


class SearchForm(Form):
    q = StringField(validators=[length(min=1, max=30)])
    page = IntegerField(validators=[NumberRange(min=1, max=99)], default=1)
