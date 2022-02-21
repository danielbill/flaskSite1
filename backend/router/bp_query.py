# =========================== #
# -*- coding: utf-8 -*-       #
# @Time : 22/2/14 10:26     #
# @Author : 毕磊              #
# @Site : ---                 #
# @File : bp_query.py          #
# @Software: PyCharm  #
# 所有查询走这里
# =========================== #

from flask import (
    Blueprint, render_template,request,Response,url_for)

import backend.model.trend_model as trdModl
import py.tools.dataFrameTool as dfTool
import backend.tool.modelTool as mt
import backend.model.query_model as qMod
import backend.QUERY_CONFIG as qc
import json
import log

bp = Blueprint('q', __name__, url_prefix='/q')

#所有查询的动态route, 此方法某人路由到视图,查询由视图中的ajax接口调用
#query参数为1时,不调用ajaxapi查询接口,直接此处查询给出结果
@bp.route('/<query_key>/')
@bp.route('/<query_key>/<int:query>')
def query(query_key,query=0):
    param = request.args
    data = {}
    if query==1:
        log.debug('不使用ajax接口查询,则在此查询')
        data  = qMod.df_from_db(query_key,param)
    view  = 'query/'+query_key+'.html'
    ajaxUrl = 'ajaxapi/'+query_key

    context ={
        'data' : data,
        'qc' :qc.QUERY_CONFIG.CONF.get(query_key),
        'query_key': query_key
    }

    # return render_template('query/query_form_and_table_tmpt1.html',data=data,qc=qc.QUERY_CONFIG.CONF.get(query_key))
    return render_template(f'query/{query_key}.html',**context)

