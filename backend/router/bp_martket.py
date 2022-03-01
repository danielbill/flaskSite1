# =========================== #
# -*- coding: utf-8 -*-       #
# @Time : 22/2/4 11:35     #
# @Author : 毕磊              #
# @Site : ---                 #
# @File : bp_martket.mypy          #
# @Software: PyCharm  #
# 配置市场全貌相关的router
# =========================== #
from flask import (
    Blueprint, render_template)

import backend.model.market_home_model as homeModl

bp = Blueprint('market', __name__, url_prefix='/market')

@bp.route('/')
@bp.route('/home')
def home():
    return render_template('market/market_view.html',data=homeModl.model_for_view())

if __name__ == '__main__':
    quit(0)
