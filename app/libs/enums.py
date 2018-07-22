# -*- coding: utf-8 -*-
from enum import Enum

__author__ = 'Apple'

class ClientTypeEnum(Enum):
    USER_MOBILE = 100

    # 微信小程序
    USER_MINA = 200
    # 微信公众号
    USER_WX = 201