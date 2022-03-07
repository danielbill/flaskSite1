# =========================== #
# -*- coding: utf-8 -*-       #
# @Time : 22/2/10 11:44     #
# @Author : 毕磊              #
# @Site : ---                 #
# @File : dz_price_model.mypy          #
# @Software: PyCharm  #
#
# =========================== #
import log
import mypy.db.mysql_db_manager as mydb
import mypy.db.dao.sql_in_stock as sqls
import mypy.tools.dataFrameTool as dfTool

def get_price_change(chg_type):
    view_data={}
    if len(chg_type) == 0: chg_type='chg_d5'
    sql = sqls.sql_future_price_chg %chg_type
    log.debug(sql)
    df = mydb.queryToDataframe(sql)
    if len(df)>0 :
        row = df.loc[0]
        view_data['date']=row['date']
        view_data['value']=dfTool.df_list_to_echarts_valuestr(df,chg_type)
        view_data['name']=dfTool.df_list_to_echarts_valuestr(df,'名称')
        view_data['type']=translate_type(chg_type)
    log.debug(view_data)
    return view_data

def translate_type(type):
    switcher = {
        'chg_d5': "5个交易日环比",
        'chg_d20': "20个交易日环比",
        'chg_d60': "60个交易日环比",
        'chg_d120': "120个交易日环比",
        'chg_d240': "240个交易日环比",
        'chg_gap_d5': "5个交易日价差",
        'chg_gap_d20': "20个交易日价差",
        'chg_gap_d60': "60个交易日价差",
        'chg_gap_d120': "120个交易日价差",
        'chg_gap_d240': "240个交易日价差"
    }
    return switcher.get(type, 'wrong value')

def get_dzb(order_type=None):
    if order_type is None:
        order_type = 'gr_w1'
    view_data={}
    sql = f"""select * from ppi_dzb_week where date = (select max(date) from ppi_dzb_week)
            order by {order_type} desc"""
    df = mydb.queryToDataframe(sql)
    if len(df)>0 :
        row = df.loc[0]
        view_data['date']=row['date']
        view_data['value']=dfTool.df_list_to_echarts_valuestr(df,order_type)
        view_data['product']=dfTool.df_list_to_echarts_valuestr(df,'product')
        view_data['order_type']=order_type
    # log.debug(view_data)
    return view_data


if __name__ == '__main__':
    get_dzb()
