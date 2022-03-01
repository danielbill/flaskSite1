# =========================== #
# -*- coding: utf-8 -*-       #
# @Time : 22/2/12 10:29     #
# @Author : 毕磊              #
# @Site : ---                 #
# @File : selection_model.mypy          #
# @Software: PyCharm  #
# 当季高增低估,预报选股利器!
# =========================== #
import mypy.db.mysql_db_manager as mydb
import mypy.db.dao.sql_in_stock as sqls
import mypy.db.db_config_helper as dbcf
import log
import mypy.tools.financial_report_tool as frt
import mypy.tools.param_tool as pt


#当季高增低估查询
def get_ls_hglp(param):
    this_report_season = frt.get_latest_report_season()
    prev_report_season = frt.prev_season(this_report_season)
    sql = sqls.sql_ls_hglp %(this_report_season,prev_report_season)
    where = ''
    for key in param.keys():
        val = param.get(key)
        if val is None:continue
        try:
            where +=" and "+ dbcf.cf.get_where_condition('ls_hglp',key)
            where +=str(param.get(key))
        except:
            continue
    sql+=where + " order by pe_2s"
    log.debug(sql)
    df = mydb.queryToDataframe(sql)
    return df

#高利润率且扩张的企业
def get_high_margin_company(param):
    sql = sqls.sql_sl_high_margin
    where = pt.getWhereCondition_by_param('',param,'')
    orderby = 'order by netprofit_hb desc'
    sql += where
    df = mydb.queryToDataframe(sql)
    return df

if __name__ == '__main__':
    get_ls_hglp({'in_hb':10})
