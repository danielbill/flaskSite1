# =========================== #
# -*- coding: utf-8 -*-       #
# @Time : 22/1/27 16:09     #
# @Author : 毕磊              #
# @Site : ---                 #
# @File : bp_trend.py          #
# @Software: PyCharm  #
# 和股票走势相关的route都在这里编写
# =========================== #

from flask import (
    Blueprint, render_template, request)

import backend.model.trend_model as trdModl

bp = Blueprint('trend', __name__, url_prefix='/trend')

@bp.route('/xgxd', methods=('GET', 'POST'))
def xgxd():
    #获取查询类别
    type = request.args.get('type')
    if type is None or len(type)==0: type =0
    stats_xgxd = trdModl.get_stats_xgxd()
    param ={}
    param['type'] = type
    param['stats_xgxd'] = stats_xgxd
    return render_template('trend/stock_xgxd.html',data=param)