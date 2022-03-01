# =========================== #
# -*- coding: utf-8 -*-       #
# @Time : 22/2/4 11:31     #
# @Author : 毕磊              #
# @Site : ---                 #
# @File : bp_ajax_api.mypy          #
# @Software: PyCharm  #
#
# =========================== #

from flask import (
    Blueprint, request,Response,make_response)

import backend.model.trend_model as trdModl
import log
import mypy.tools.dataFrameTool as dfTool
import backend.tool.modelTool as mt
import backend.model.selection_model as slMod
import backend.model.query_model as qMod
import backend.db_reload.db_reload_manager as drm
import backend.router.service_manager as svcMag

bp = Blueprint('ajaxapi', __name__, url_prefix='/ajaxapi')

#创新高新低股票列表
@bp.route('/xgxd_list')
def xgxd_list():
    data = {
        'code': 0,
        'msg': 'ok',
        'data': []
    }
    t_type = 0
    arg_type =request.args.get('type')
    if arg_type.isdigit() : t_type = int(arg_type)
    df = trdModl.get_xgxd_list(t_type)
    dfTool.timestamp_to_str(df,'update_time')

    # dfTool.timestamp_to_str(df,'前期高点日期')
    xgxd_json_dict = dfTool.df_to_records(df)
    data['count'] = len(df)
    data['data'] = xgxd_json_dict
    data['type'] = t_type
    # return data,{'Content-Type': 'text/html; charset=utf-8'}
    return data

#当季(预报)高增低估的股票 late season , high grow low price
@bp.route('/ls_hglp')
def ls_hglp():
    param = request.args
    data = mt.df_to_layui_table_data(slMod.get_ls_hglp(param))
    # data = mt.df_to_w2ui_table_data(slMod.get_ls_hglp(param))
    # return Response(json.dumps(data), mimetype='application/json')
    return data

# @bp.route('/hm')
# def high_margin():
#     param = request.args
#     data = mt.df_to_layui_table_data(slMod.get_high_margin_company(param))
#     return data

@bp.route('/<query_key>')
def query(query_key):
    param = request.args
    df  = qMod.df_from_db(query_key,param)
    df = mt.fill_NaNull_withEmptyStr(df)
    data = mt.df_to_layui_table_data(df)
    # response = make_response(data)
    # response.headers["charset"]='UTF-8'
    return data

#前台缺部分数据时,临时刷新后台取数
@bp.route('/reload/<reload_id>')
def db_reload(reload_id):
    print('db reload id is ' , reload_id)
    param = request.args
    drm.reload_db(reload_id,param)
    # response = make_response(data)
    # response.headers["charset"]='UTF-8'
    return '200'

#后台服务,和reload的不一样,后台服务不需要返回结果
@bp.route('/svc/<svc_id>')
def service(svc_id):
    log.debug(f'svc_id is {svc_id}')
    param = request.args
    context={
        'msg':'success',
        'svc_code':100 #成功
    }
    data = svcMag.do_service(svc_id,param)
    context['data']=data
    return context