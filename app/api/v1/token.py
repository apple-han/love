# -*- coding: utf-8 -*-
import json

import requests
from flask import current_app, jsonify

from itsdangerous import TimedJSONWebSignatureSerializer as Serializer

from app.libs.enums import ClientTypeEnum
from app.libs.error_code import ServerError
from app.libs.redprint import Redprint
from app.models.user import User
from app.validators.forms import ClientForm, UserMinaForm

__author__ = 'Apple'

api = Redprint('token')

@api.route('', methods=['POST'])
def get_token():
    form = UserMinaForm().validate_for_api()

    promise = {
        ClientTypeEnum.USER_MINA: get_openId,
    }
    identity = promise[ClientTypeEnum(form.type.data)](
        form.code.data
    )
    pid_reuslt = User.is_exist_pid(identity['openId'])
    if not pid_reuslt:
        User.register_by_mina(identity['openId'])

    Result = User.verify(identity['openId'])

    expiration = current_app.config['TOKEN_EXPIRATION']
    token = generate_auth_token(Result['uid'],
                                identity['openId'],
                                form.type.data,
                                Result['scope'],
                                expiration)
    t = {
        'token': token.decode('ascii')
    }
    # 序列化一下
    return jsonify(t), 201

# 获取用户的openId
def get_openId(code):
        result = requests.get(current_app.config['LOGINURL'].format(
            current_app.config['APPID'],
            current_app.config['APPSECRET'],
            code
        ))
        print(json.loads(result.text)["openid"])
        if not result:
            raise ServerError("微信内部错误")
        return {"openId": json.loads(result.text)["openid"]}

def generate_auth_token(uid, openId, ac_type, scope=None, expiration=72000):
    s = Serializer(current_app.config['SECRET_KEY'], expires_in=expiration)

    return s.dumps({
        'openId': openId,
        'type': ac_type.value,
        'uid': uid,
        'scope': scope
    })

