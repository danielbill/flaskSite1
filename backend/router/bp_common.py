# =========================== #
# -*- coding: utf-8 -*-       #
# @Time : 22/2/20 9:29     #
# @Author : 毕磊              #
# @Site : ---                 #
# @File : bp_common.mypy          #
# @Software: PyCharm  #
# 所有股票相关页面导航从这里走,通用查询除外
# =========================== #
from flask import (
    Blueprint, render_template, request)
import backend.model.common_model as cm

#通用导航(除去复杂参数查询的页面跳转)
bp = Blueprint('com', __name__, url_prefix='/')

#所有详情页面的动态route
@bp.route('/<dir>/<view_key>')
def view(dir,view_key):
    param = request.args

    view = f'{dir}/{view_key}.html'
    whole_view_key = dir+'.'+view_key
    data = cm.get_view_data(whole_view_key,param)
    context ={
        'data' : data,
        'dir': dir,
        'view_key': view_key,
        'whole_view_key':whole_view_key
    }
    return render_template(view,**context)