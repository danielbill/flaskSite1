# =========================== #
# -*- coding: utf-8 -*-       #
# @Time : 22/2/14 12:09     #
# @Author : 毕磊              #
# @Site : ---                 #
# @File : query_model.py          #
# @Software: PyCharm  #
#
# =========================== #
import log
import py.db.mysql_db_manager as mydb
import py.db.dao.sql_query_in_stock as sqls
import backend.QUERY_CONFIG as qc


def df_from_db(query_key, params):
    sql_base = sqls.QUERY_SQLS[query_key]
    if sql_base is None : return
    sql = get_sql(sql_base, query_key, params)
    df = mydb.queryToDataframe(sql)
    print('df length is ',len(df))
    return df

def get_sql(sql_base,query_key,params):
    #有些外连接所需要的如不同季度号需要额外处理,不是来自页面
    sql_base = get_extra_fillo(sql_base,query_key,params)
    #根据查询拼装完整的where条件
    sql_base+=qc.get_where_condition(query_key,params)
    sql_base+=qc.get_order_condition(query_key,params)
    sql_base+=get_limit_condition(query_key,params)
    return sql_base


#设置一个关键字列表,编写对应关键字的处理器,在这个方法中,重新赋值sql
def get_extra_fillo(sql_base,query_key,params):
    return sql_base

#拼装limit条件
def get_limit_condition(query_key,params):
    return ' limit 100'

if __name__ == '__main__':
    # df_from_db('hm',{'np_rate':25,'debt_rate':50})
    print( sqls.QUERY_SQLS.get('111'))
