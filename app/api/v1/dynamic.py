# -*- coding: utf-8 -*-
from app.libs.redprint import Redprint

__author__ = 'Apple'

api = Redprint('identity')

@api.route('/get')
def get_book():
     return 'get book'