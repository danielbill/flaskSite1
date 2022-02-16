# =========================== #
# -*- coding: utf-8 -*-       #
# @Time : 22/2/4 11:31     #
# @Author : 毕磊              #
# @Site : ---                 #
# @File : bp_ajax_api.py          #
# @Software: PyCharm  #
#
# =========================== #

from flask import (
    Blueprint, request,Response)

import backend.model.trend_model as trdModl
import py.tools.dataFrameTool as dfTool
import backend.tool.modelTool as mt
import backend.model.selection_model as slMod
import backend.model.query_model as qMod
import json

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
    print('in ajax query  key is ' , query_key)
    param = request.args
    df  = qMod.df_from_db(query_key,param)
    data = mt.df_to_layui_table_data(df)
    return data