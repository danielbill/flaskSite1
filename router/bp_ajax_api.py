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
    Blueprint, request)

import backend.view.trend_model as trdModl
import py.tools.dataFrameTool as dfTool

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