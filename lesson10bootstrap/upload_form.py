# -*- coding: utf-8 -*-

from flask.ext.wtf import Form
from wtforms import FileField, SubmitField
from wtforms.validators import DataRequired


class UploadForm(Form):
    file = FileField(label=u'选择文件')
    submit = SubmitField(label=u'提交')