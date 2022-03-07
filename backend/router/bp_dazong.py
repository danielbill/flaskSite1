# =========================== #
# -*- coding: utf-8 -*-       #
# @Time : 22/2/8 17:41     #
# @Author : 毕磊              #
# @Site : ---                 #
# @File : bp_dazong.mypy          #
# @Software: PyCharm  #
#
# =========================== #
import backend.model.dz_storage_model as storageMod
import backend.model.dz_price_model as priceMod
import log
from flask import request
import backend.model.dz_jicha_model as jcMod

from flask import (Blueprint, render_template)

bp = Blueprint('dz', __name__, url_prefix='/dz')

@bp.route('/storage', methods=('GET', 'POST'))
def storage():
    return render_template('dz/dz_storage.html', data=storageMod.model_for_view())

@bp.route('/price', methods=('GET', 'POST'))
def price():
    chg_type = request.args.get('chg_type')
    if chg_type is None or len(chg_type) == 0: chg_type ='chg_d5'
    return render_template('dz/dz_price.html',data=priceMod.get_price_change(chg_type))

@bp.route('/dzb', methods=('GET', 'POST'))
def dzb():
    order_type = request.args.get('order_type')
    if order_type is None or len(order_type) == 0: order_type ='gr_w1'
    return render_template('dz/dz_dzb.html',data=priceMod.get_dzb(order_type))

@bp.route('/jicha', methods=('GET', 'POST'))
def jicha():
    type  = request.args.get('type')
    return render_template('dz/dz_jicha.html', data=jcMod.get_future_jicha(type))