# -*- coding: utf-8 -*-
from flask import Blueprint, jsonify, g

from app.libs.error_code import DeleteSuccess
from app.libs.redprint import Redprint
from app.libs.token_auth import auth
from app.models.base import db
from app.models.user import User

__author__ = 'Apple'

api = Redprint('user')

@api.route('/<int:uid>', methods=['GET'])
@auth.login_required
def super_get_user(uid):
     user = User.query.filter_by(id = uid).first_or_404()
     return jsonify(user)


@api.route('/<int:uid>', methods=['GET'])
@auth.login_required
def get_user(uid):
     user = User.query.filter_by(id = uid).first_or_404()
     return jsonify(user)


# 管理员
@api.route('/<int:uid>', methods=['DELETE'])
def super_delete_user(uid):
     pass

@api.route('', methods=['DELETE'])
@auth.login_required
def delete_user():
     uid = g.user.uid
     # g 线程隔离
     with db.auto_commit():
          user = User.query.filter_by(id=uid).first_or_404()
          user.delete()
     return DeleteSuccess()