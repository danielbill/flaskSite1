# =========================== #
# -*- coding: utf-8 -*-       #
# @Time : 22/2/18 13:52     #
# @Author : 毕磊              #
# @Site : ---                 #
# @File : extra_manager.mypy          #
# @Software: PyCharm  #
#
# =========================== #

import backend.model.extra.qe_extra1 as e1
from backend.model.extra import qe_hm,qe_rank
import backend.model.extra.sql_common_processor as commonPro
import os,sys
import importlib
import pkgutil

QUERY_EXTRAS= {
    'common' : commonPro,
}

test_extras ={
    'common' : commonPro,
    'hm': qe_hm,
    'rank':qe_rank,
}

def register_extra_process_in_the_dir():
    pkg = 'backend.model.extra'
    files = os.listdir(os.path.dirname(os.path.realpath(__file__)))
    # print(f'in register_extra_process_in_the_dir get {files}')
    for file in files:
        if file.find('qe_')!=-1:
            py = file[:-3]
            module = importlib.import_module(pkg+'.'+py)
            QUERY_EXTRAS[py[3:]]=module
    # print(QUERY_EXTRAS)

register_extra_process_in_the_dir()


if __name__ == '__main__':
    # register_extra_process_in_the_dir()
    r = 'backend.model.extra'
    for  name in pkgutil.iter_modules([r]):
        print(name)

