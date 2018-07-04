# create by 'yang' in 2018/7/03
from sqlalchemy.orm import relationship

from app.models.base import Base
from sqlalchemy import Column, Integer, Boolean, ForeignKey, String

__author__ = 'yang'


class Gift(Base):
    id = Column(Integer, primary_key=True)
    user = relationship('User')
    uid = Column(Integer, ForeignKey('user.id'))
    isbn = Column(String(15), nullable=False)
    launched = Column(Boolean, default=False)  # 表示礼物有没有送出去

    # book = relationship('Book')
    # bid = Column(Integer, ForeignKey('Book.isbn'))
