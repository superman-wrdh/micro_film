# _*_ coding: utf-8 _*_
__author__ = 'superman'
__date__ = '2018/3/27 17:06'

from flask import Blueprint

admin = Blueprint("admin",__name__)

import app.admin.views