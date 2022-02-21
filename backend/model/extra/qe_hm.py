# =========================== #
# -*- coding: utf-8 -*-       #
# @Time : 22/2/18 18:27     #
# @Author : 毕磊              #
# @Site : ---                 #
# @File : qe_hm.py          #
# @Software: PyCharm  #
# 处理hm1查询语句的方法
# =========================== #
import math

import backend.model.extra.sql_common_processor as cp
import py.tools.financial_report_tool as frt
import py.db.dao.sql_query_in_stock as sqlq

class sql_processor(cp.sql_processor):

    def _assemble_join(self, param, query_conf) -> dict:
        this_season = frt.get_latest_report_season()
        last_season = frt.prev_season(this_season)
        next_season = frt.next_season(this_season)
        this_year = int(this_season[0:4])
        last_year_q4 = str(this_year-1)+'12'
        param = {
            'last_year_q4':last_year_q4,
            'this_season':this_season,
            'last_season':last_season,
            'next_season':next_season,
        }
        return param



if __name__ == '__main__':
    sql = sqlq.QUERY_SQLS.get('hm1')
    sp = sql_processor(query_key='hm1', param={'np_rate':50, })
    print(sp.process())


