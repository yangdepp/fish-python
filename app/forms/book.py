# create by 'yang' in 2018/6/16
from wtforms import Form, StringField, IntegerField
from wtforms.validators import length, NumberRange, DataRequired

__author__ = 'yang'


class SearchForm(Form):
    # validators还可以传入message自定义错误提示
    q = StringField(validators=[DataRequired(), length(min=1, max=30)])
    page = IntegerField(validators=[NumberRange(min=1, max=99)], default=1)
