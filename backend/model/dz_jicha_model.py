# =========================== #
# -*- coding: utf-8 -*-       #
# @Time : 22/2/10 17:13     #
# @Author : 毕磊              #
# @Site : ---                 #
# @File : dz_jicha_model.mypy          #
# @Software: PyCharm  #
#
# =========================== #
import log
import mypy.db.mysql_db_manager as mydb
import mypy.db.dao.sql_in_stock as sqls
import mypy.tools.dataFrameTool as dfTool

def get_future_jicha(data_type):
    view_data={}
    if data_type is None or len(data_type) == 0: data_type='near_basis_rate'
    sql = sqls.sql_future_jicha % data_type
    log.debug(sql)
    df = mydb.queryToDataframe(sql)
    if len(df)>0 :
        row = df.loc[0]
        view_data['date']=row['date']
        view_data['value']=dfTool.df_list_to_echarts_valuestr(df,data_type)
        view_data['name']=dfTool.df_list_to_echarts_valuestr(df,'名称')
        view_data['type']=translate_type(data_type)
    # log.debug(view_data)
    return view_data

def translate_type(type):
    switcher = {
        'near_basis_rate': "最近合约基差率",
        'dom_basis_rate': "主力合约基差率",
        'near_basis': "最近合约基差",
        'dom_basis': "主力合约基差"
    }
    return switcher.get(type, 'wrong value')





if __name__ == '__main__':
    get_future_jicha(None)
