# =========================== #
# -*- coding: utf-8 -*-       #
# @Time : 22/2/11 13:09     #
# @Author : 毕磊              #
# @Site : ---                 #
# @File : bp_selection.mypy          #
# @Software: PyCharm  #
#
# =========================== #
import log
from flask import request
from flask import (Blueprint, render_template)
import backend.model.selection_model as slMol
bp = Blueprint('sl', __name__, url_prefix='/sl')

#high grow low price
@bp.route('/hglp', methods=('GET', 'POST'))
def hglp():
    return render_template('selection/ls_hglp.html')

#高利润率选股
@bp.route('/hm', methods=('GET', 'POST'))
def high_margin():
    # return render_template('selection/high_margin.html')
    return render_template('selection/test.html')


