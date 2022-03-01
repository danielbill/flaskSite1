# =========================== #
# -*- coding: utf-8 -*-       #
# @Time : 22/2/24 19:05     #
# @Author : 毕磊              #
# @Site : ---                 #
# @File : qe_rank.mypy          #
# @Software: PyCharm  #
# rank查询的季度号必须是最近完整公布报表的季度,
# =========================== #

import backend.model.extra.sql_common_processor as cp
import mypy.tools.financial_report_tool as frt
import mypy.db.dao.sql_query_in_stock as sqlq

class sql_processor(cp.sql_processor):

    def _assemble_join(self,param,query_conf) ->dict:
        intact_season = frt.get_intact_season()
        param={}
        param['intact_season'] = intact_season
        return param


if __name__ == '__main__':
    s = sql_processor('rank', {'grow_rank':100})
    print(s.process())
