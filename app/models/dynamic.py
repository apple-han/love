# -*- coding: utf-8 -*-
from sqlalchemy import ForeignKey, Column, String, Integer
from sqlalchemy.orm import relationship, backref

from app.models.base import Base
from app.models.user import User

__author__ = 'Apple'


# 用户动态信息表
class Dynamic(Base):
    __tablename__ = 'dynamic'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'), nullable=False)
    user = relationship('User')
    content = Column(String(258))
    image = Column(String(50))

# 用户动态信息点赞表
class Give(Base):
    __tablename__ = 'give'

    id = Column(Integer, primary_key=True)
    give_id = Column(Integer, ForeignKey('users.id'))
    give_id = relationship(
        User, primaryjoin='User.id==give.give_id',
        backref=backref('dynamic_give_id', cascade='all,delete-orphan'))

    ungive_id = Column(Integer, ForeignKey('users.id'))
    ungive_id = relationship(
        User, primaryjoin='User.id==give.ungive_id',
        backref=backref('dynamic_ungive_id', cascade='all,delete-orphan'))

    count = Column(Integer(10))





