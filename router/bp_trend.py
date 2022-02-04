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
    Blueprint, render_template)

bp = Blueprint('value', __name__, url_prefix='/trend')

@bp.route('/xgxd', methods=('GET', 'POST'))
def register():
    return render_template('trend/stock_xgxd.html')