# -*- coding: utf-8 -*-
from sqlalchemy import Column, String, SmallInteger, Integer, ForeignKey
from sqlalchemy.orm import relationship, backref

from app.api.v1 import user
from app.libs.error_code import NotFound, AuthFailed
from app.models.base import Base, db

__author__ = 'Apple'

class User(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)
    open_id = Column(String(60), unique=True, nullable=False)
    auth = Column(SmallInteger, default=1)
    weixin = Column(String(60), nullable=False)

    def keys(self):
        return ['pid', 'auth']

    @staticmethod
    def is_exist_pid(pid):
        openId = User.query.filter(User.open_id == pid).first()
        return openId

    @staticmethod
    def verify(pid):
        user = User.query.filter_by(open_id=pid).first_or_404()
        if not user.id:
            raise AuthFailed()
        scope = 'AdminScope' if user.auth == 2 else 'UserScope'
        return {'uid': user.id, 'scope': scope}

    @staticmethod
    def register_by_mina(pid):
            with db.auto_commit():
                user = User()
                user.pid = pid
                db.session.add(user)

class UserInfo(Base):
    __tablename__ = 'user_info'

    # 性别
    MAN = 1
    GIRL = 2

    # 婚姻状况
    MARRIED = 1
    UNMARRIED = 2

    # 购房状况
    BOUGHTHOUSE = 1
    NOTBOUGHTHOUSE = 2

    # 购车状况
    BOUGHTCAR = 1
    NOTBOUGHTCAR = 2

    id = Column(Integer, primary_key=True)
    iden_id = Column(String(8), nullable=False)
    nickname = Column(String(24), nullable=False)
    sex = Column(Integer(2), default= GIRL)
    age = Column(String(10), nullable=False)
    height = Column(String(5), nullable=False)
    education = Column(String(5), nullable=False)
    salary_min = Column(String(8), nullable=False)
    salary_max = Column(String(8), nullable=False)
    address = Column(String(30), nullable=False)
    marital_status = Column(Integer(2), default= UNMARRIED)
    children_status = Column(String(10), nullable=False)
    house_status = Column(Integer(2), default= NOTBOUGHTHOUSE)
    car_status = Column(Integer(2), default= NOTBOUGHTCAR)


class UserTag(Base):
    __tablename__ = 'user_tag'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'), nullable=False)
    user = relationship('User')
    life = Column(String(5), nullable=False)
    sport = Column(String(5), nullable=False)
    arder = Column(String(5), nullable=False) # 休闲
    diet = Column(String(5), nullable=False) # 饮食

class UserTagInfo(Base):
    __tablename__ = 'user_tag_info'

    id = Column(Integer, primary_key=True)
    life = Column(String(5), nullable=False)
    sport = Column(String(5), nullable=False)
    arder = Column(String(5), nullable=False) # 休闲
    diet = Column(String(5), nullable=False) # 饮食


class LoveConnect(Base):
    __tablename__ = 'love_connect'

    id = Column(Integer, primary_key=True)

    active_love_id = Column(Integer, ForeignKey('users.id'))  # user_id confirm_id 同时关联一个表
    active_love_id = relationship(
        User, primaryjoin='User.id==love_connect.unactive_love_id',
        backref=backref('love_connect_active', cascade='all,delete-orphan'))

    unactive_love_id = Column(Integer, ForeignKey('users.id'))
    unactive_love_id = relationship(
        User, primaryjoin='User.id==love_connect.unactive_love_id',
        backref=backref('love_connect_unactive', cascade='all,delete-orphan'))

class UserPhotos(Base):
    __tablename__ = 'user_photos'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'), nullable=False)
    user = relationship('User')
    image  = Column(String(50))


