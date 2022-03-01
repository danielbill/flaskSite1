# =========================== #
# -*- coding: utf-8 -*-       #
# @Time : 22/2/14 10:26     #
# @Author : 毕磊              #
# @Site : ---                 #
# @File : bp_query.mypy          #
# @Software: PyCharm  #
# 所有查询走这里
# =========================== #

from flask import (
    Blueprint, render_template,request,Response,url_for)

import backend.model.trend_model as trdModl
import mypy.tools.dataFrameTool as dfTool
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
    # include_page  = 'query/'+query_key+'.html'
    ajaxUrl = 'ajaxapi/'+query_key
    thisQueryConf = qc.QUERY_CONFIG.CONF.get(query_key)
    context ={
        'data' : data,
        'qc' :thisQueryConf,
        'query_key': query_key,
    }
    #该查询指定的返回页面,多查询共用同一定制页面时
    page = thisQueryConf.get('page')
    if page is None:
        page = _getPage(query_key)#按照query_key算出可能的详情页,但未必存在
    log.debug(f'bq query go to {page}')
    try:
        return render_template(page,**context)
    except Exception as e:#走公共查询页
        log.debug(str(e))
        return render_template('query/query_form_and_table_tmpt1.html',**context)

def _getPage(query_key):
    dir = 'query'
    page = '.html'
    dir_sep = query_key.find('.')
    if  dir_sep !=-1 :
        dir = query_key[0:dir_sep]
        page = query_key[dir_sep+1:]+page
    else:
        page = query_key+page
    return dir+'/'+page


if __name__ == '__main__':
    # print(_getPage('strategy.detail'))
    s = 'detail'
    print(s[0:s.find('.')])
    print(s[s.find('.')+1:])







