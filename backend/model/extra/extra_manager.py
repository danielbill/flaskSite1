# =========================== #
# -*- coding: utf-8 -*-       #
# @Time : 22/2/18 13:52     #
# @Author : 毕磊              #
# @Site : ---                 #
# @File : extra_manager.py          #
# @Software: PyCharm  #
#
# =========================== #

import backend.model.extra.extra1 as e1
import backend.model.extra.qe_hm as hm
import backend.model.extra.sql_common_processor as commonPro

QUERY_EXTRAS= {
    'common' : commonPro,
    'hm': hm
}


if __name__ == '__main__':
    sqlPro = QUERY_EXTRAS['hm1']
    pro = sqlPro.sql_processor('hm1', {})
    print(pro.process())
