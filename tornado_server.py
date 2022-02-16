# =========================== #
# -*- coding: utf-8 -*-       #
# @Time : 22/2/9 15:23     #
# @Author : 毕磊              #
# @Site : ---                 #
# @File : tornado_server.py          #
# @Software: PyCharm  #
#
# =========================== #

#coding=utf-8
#!/usr/bin/python
from tornado.wsgi import WSGIContainer
from tornado.httpserver import HTTPServer
from tornado.ioloop import IOLoop
import sys,os
from app import app
http_server = HTTPServer(WSGIContainer(app))
http_server.listen(5000)  #flask默认的端口
IOLoop.instance().start()
