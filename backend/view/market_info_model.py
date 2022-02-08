# =========================== #
# -*- coding: utf-8 -*-       #
# @Time : 22/2/8 7:39     #
# @Author : 毕磊              #
# @Site : ---                 #
# @File : market_info_model.py          #
# @Software: PyCharm  #
#
# =========================== #
import log
import py.db.dao.sql_in_stock as sql
import py.db.mysql_db_manager as mydb
import py.tools.dataFrameTool as dfTool


def get_market_info():
    df_info = mydb.queryToDataframe(sql.sql_latest_market_info)
    df_stat = mydb.queryToDataframe(sql.sql_latest_stat_market)
    stat_row = df_stat.loc[0]
    date = stat_row['date']
    market = '市场总体'
    stocks = stat_row['stocks']
    capti = stat_row['capti']
    amounts = stat_row['amounts']
    pe_wei = stat_row['pe_wei']
    row = [date,market,stocks,capti,amounts,pe_wei]
    df_info.loc[len(df_info)] = row

    view_data = {}
    view_data['info'] = df_info
    view_data['stat'] = df_stat
    log.debug(view_data)
    return view_data


if __name__ == '__main__':
    df = dfTool.get_a_test_df()
    # print(df)
    df.loc[len(df)]=[5,2]
    get_market_info()
