# -*- coding: utf-8 -*-
from sqlalchemy import Column, String, SmallInteger, Integer, ForeignKey
from sqlalchemy.orm import relationship, backref

from app.api.v1 import user
from app.libs.error_code import NotFound, AuthFailed
from app.models.base import Base, db

__author__ = 'Apple'

# 身份证信息的验证
class CertificateIdentification(Base):
    __tablename__ = 'certificate_identification'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'), nullable=False)
    user = relationship('User')
    image = Column(String(50))

# 学历信息的验证
class CertificateEducation(Base):
    __tablename__ = 'certificate_education'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'), nullable=False)
    user = relationship('User')
    image = Column(String(50))

# 手机信息
class CertificatePhone(Base):
    __tablename__ = 'certificate_phone'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'), nullable=False)
    user = relationship('User')
    phone = Column(String(50))
    code = Column(String(6))

# 房产信息的验证
class CertificateHouse(Base):
    __tablename__ = 'certificate_house'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'), nullable=False)
    user = relationship('User')
    image = Column(String(50))

# 车子信息的验证
class CertificateCar(Base):
    __tablename__ = 'certificate_car'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'), nullable=False)
    user = relationship('User')
    image = Column(String(50))

# 验证信息统计表
class CertificateCount(Base):
    __tablename__ = 'certificate_count'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'), nullable=False)
    user = relationship('User')
    count = Column(Integer(10))

