# =========================== #
# -*- coding: utf-8 -*-       #
# @Time : 22/2/18 13:56     #
# @Author : 毕磊              #
# @Site : ---                 #
# @File : qe_extra1.mypy          #
# @Software: PyCharm  #
#
# =========================== #

import backend.model.extra.sql_common_processor as cp
import mypy.tools.financial_report_tool as frt
import mypy.db.dao.sql_query_in_stock as sqlq

class sql_processor(cp.sql_processor):
    def _assemble_join(self, param, query_conf) -> dict:
        param['k']='kkk'
        return param

if __name__ == '__main__':
    quit(0)
