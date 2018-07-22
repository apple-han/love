# -*- coding: utf-8 -*-
from werkzeug.exceptions import HTTPException

from app import create_app

from app.libs.error import APIException
from app.libs.error_code import ServerError

__author__ = 'Apple'

app = create_app()

@app.errorhandler(Exception)
def framework_error(e):
    # flask 1.0
    # APIException
    # HTTPException
    # Exception
    if isinstance(e, APIException):
        return e
    if isinstance(e, HTTPException):
        code = e.code
        msg = e.description
        error_code = 1007
        return APIException(msg, code, error_code)
    else:
        # log
        # 调试模式
        if not app.config['DEBUG']:
            return ServerError()
        else:
            raise e

if __name__ == '__main__':
    app.run(debug=True)