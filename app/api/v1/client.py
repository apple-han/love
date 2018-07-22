# -*- coding: utf-8 -*-
from flask import request

from app.libs.enums import ClientTypeEnum
from app.libs.error_code import Success
from app.libs.redprint import Redprint
from app.models.user import User
from app.validators.forms import ClientForm, UserMinaForm
__author__ = 'Apple'

api = Redprint('client')


@api.route('/register', methods=['POST'])
def create_client():
    form = ClientForm().validate_for_api()
    promise = {
        ClientTypeEnum.USER_MINA: __register_user_by_mina
    }
    promise[form.type.data]()

    # 可以预知的异常  APIException
    # 我们没有意识到的异常 全剧异常 AOP

    return Success()

def __register_user_by_mina():
    form = UserMinaForm().validate_for_api()
    User.register_by_mina(form.pid.data)