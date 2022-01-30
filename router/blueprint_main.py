# =========================== #
# -*- coding: utf-8 -*-       #
# @Time : 22/1/27 16:09     #
# @Author : 毕磊              #
# @Site : ---                 #
# @File : blueprint_main.py          #
# @Software: PyCharm  #
# =========================== #

import functools
from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for)

bp = Blueprint('value', __name__, url_prefix='/value')

@bp.route('/高增长', methods=('GET', 'POST'))
def register():
    return render_template('value/高增长.html')