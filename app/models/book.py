# create by 'yang' in 2018/6/16
from sqlalchemy import Column, Integer, String
from flask_sqlalchemy import SQLAlchemy

__author__ = 'yang'

db = SQLAlchemy()


class Book(db.Model):
    id = Column(Integer, primary_key=True, autoincrement=True)  # autoincrement自增长
    title = Column(String(50), nullable=False)  # 标题
    author = Column(String(30), default='未名')  # 作者
    binding = Column(String(20))  # 装帧版本
    publisher = Column(String(50))  # 出版社
    price = Column(String(20))  # 价格
    pages = Column(Integer)  # 页数
    pubdate = Column(String(20))  # 出版年月
    isbn = Column(String(15), nullable=False, unique=True)  # 编号  unique不重复
    summary = Column(String(1000))  # 简介
    image = Column(String(50))  # 图片

    def sample(self):
        pass
