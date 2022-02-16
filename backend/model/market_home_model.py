# =========================== #
# -*- coding: utf-8 -*-       #
# @Time : 22/2/3 16:19     #
# @Author : 毕磊              #
# @Site : ---                 #
# @File : market_home_model.py          #
# @Software: PyCharm  #
#
# =========================== #
import log
import py.db.dao.sql_in_stock as sqls
import py.db.mysql_db_manager as mydb


def model_for_view():
    view_data = {}
    df = mydb.queryToDataframe(sqls.sql_stats_xgxd)
    view_data['stats_xgxd'] = df.head(1).to_dict(orient='records')[0]
    log.debug(view_data['stats_xgxd'])
    # session['index_data'] = view_data
    df_info = mydb.queryToDataframe(sqls.sql_latest_market_info)
    df_stat = mydb.queryToDataframe(sqls.sql_latest_stat_market)
    stat_row = df_stat.loc[0]
    date = stat_row['date']
    market = '市场总体'
    stocks = stat_row['stocks']
    capti = stat_row['capti']
    amounts = stat_row['amounts']
    pe_wei = stat_row['pe_wei']
    row = [date,market,stocks,capti,amounts,pe_wei]
    df_info.loc[len(df_info)] = row

    view_data['info'] = df_info
    view_data['stat'] = df_stat
    log.debug(view_data)

    return view_data


if __name__ == '__main__':
    model_for_view()
