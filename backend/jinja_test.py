# =========================== #
# -*- coding: utf-8 -*-       #
# @Time : 22/2/14 19:58     #
# @Author : 毕磊              #
# @Site : ---                 #
# @File : jinja_test.mypy          #
# @Software: PyCharm  #
#
# =========================== #

from jinja2 import Template
import backend.QUERY_CONFIG as qc

tmpt_file = r"""C:\workspace\flaskSite1\templates\query\query_form_and_table_tmpt1.html"""

import os
from jinja2 import Environment, FileSystemLoader



def test_render():
    env = Environment(loader=FileSystemLoader('../'))
    template = env.get_template('templates/query/tmpt_test.html')
    print(template.render(queryConf=qc.QUERY_CONFIG.CONF.get('hm'),lstrip_blocks=True,trim_blocks=True))

def test_emailContent():
    env = Environment(loader=FileSystemLoader('../'))
    template = env.get_template('templates/strategy/strategy_tmpt.html')
    params ={
        'query_key':'strategy.yrglp',
        'qc':qc.QUERY_CONFIG.CONF.get('yrglp')
    }
    print(template.render(**params,lstrip_blocks=True,trim_blocks=True))




if __name__ == '__main__' :
    test_emailContent()