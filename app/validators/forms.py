# -*- coding: utf-8 -*-
from wtforms import IntegerField, StringField
from wtforms.validators import DataRequired, length, ValidationError

from app.libs.enums import ClientTypeEnum
from app.models.user import User
from app.validators.base import BaseForm as Form
__author__ = 'Apple'

class ClientForm(Form):

    secret = StringField()
    type = IntegerField(validators=[DataRequired(message="请传递合法的值")])

    def validate_type(self, value):
        try:
            client = ClientTypeEnum(value.data)
        except ValueError as e:
            raise e
        self.type.data = client

class UserMinaForm(ClientForm):
    code = StringField(validators=[DataRequired(message="不允许为空"), length(
        min=5, max=32
    )])
    def validate_pid(self, value):
        if User.query.filter_by(pid=value.data).first():
            raise ValidationError('pid already exist!')