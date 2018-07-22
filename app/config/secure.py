# -*- coding: utf-8 -*-
__author__ = 'Apple'

# 数据库相关配置
SQLALCHEMY_DATABASE_URI = 'mysql+cymysql://root:123456@localhost:3306/love_arrive'
SECRET_KEY = 'jfoiqwkmjdslvnfsdajasdjfklqwjifekm'
SQLALCHEMY_TRACK_MODIFICATIONS = True
DEBUG = True

# 微信配置
APPID = "wx7fffe0ad6255bb0d"
APPSECRET = "eed1ffe3f0b3d9e7d59583fdfd6fb3c8"
LOGINURL = "https://api.weixin.qq.com/sns/jscode2session?" \
            "appid={0}&secret={1}&js_code={2}&grant_type=authorization_code"