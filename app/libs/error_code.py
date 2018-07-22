# -*- coding: utf-8 -*-
from werkzeug.exceptions import HTTPException

from app.libs.error import APIException

__author__ = 'Apple'

# 400 参数错误
# 401 未授权
# 403 禁止访问
# 404 没有找到资源
# 500 服务器错误
# 200 查询成功
# 201 创建 更新成功
# 204 删除成功
# 301 302 重定向
class Success(APIException):
    code = 201
    msg = "ok"
    error_code = 0

class DeleteSuccess(Success):
    code = 202
    error_code = -1

class ClientTypeError(APIException):
    code = 400
    msg = (
        'client is invalid'
    )
    error_code = 1006

class ServerError(APIException):
    code = 500
    msg = (
        'service error'
    )
    error_code = 998


class ParameterException(APIException):
    code = 400
    msg = 'invalid parameter'
    error_code = 1000

class NotFound(APIException):
    code = 404
    msg = 'the resource are not_found 0_0...'
    error_code = 1001

class AuthFailed(APIException):
    code = 401
    msg = 'authorization failed'
    error_code = 1005

class Forbidden(APIException):
    code = 403
    msg = 'forbidden, not in scope'
    error_code = 1004