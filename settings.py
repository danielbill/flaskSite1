# =========================== #
# -*- coding: utf-8 -*-       #
# @Time : 22/1/25 17:55     #
# @Author : 毕磊              #
# @Site : ---                 #
# @File : settings.py          #
# @Software: PyCharm  #
# =========================== #

DEBUG = True
JSON_AS_ASCII = False

# app.config.from_pyfile('settings.py')
SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:123456@localhost:3306/stock?charset=UTF8MB4'
SQLALCHEMY_TRACK_MODIFICATIONS = True
