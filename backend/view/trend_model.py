# =========================== #
# -*- coding: utf-8 -*-       #
# @Time : 22/2/4 12:40     #
# @Author : 毕磊              #
# @Site : ---                 #
# @File : trend_model.py          #
# @Software: PyCharm  #
# 走势相关的数据model
# =========================== #
import py.db.dao.sql_in_stock as sqls
import py.db.mysql_db_manager as mydb

#获取新高新低统计数据
def get_stats_xgxd()->dict:
    df = mydb.queryToDataframe(sqls.sql_stats_xgxd)
    return df.head(1).to_dict(orient='records')[0]

#获取新高新低股的列表,type指8种分类, 月 半年 一年 历史的新高新低
def get_xgxd_list(type):
    table_name = type_to_table(type)
    # log.debug('the tablename is %s' %table_name)
    sql = """select * from %s ORDER BY 股票代码""" %table_name
    df = mydb.queryToDataframe(sql)
    return df


def type_to_table(type):
    types = {
        0 : "ths_cxg_history",
        1 : "ths_cxg_year",
        2 : "ths_cxg_hy",
        3 : "ths_cxg_d30",
        4 : "ths_cxd_history",
        5 : "ths_cxd_year",
        6 : "ths_cxd_hy",
        7 : "ths_cxd_d30"
    }
    return types.get(type, None)



if __name__ == '__main__':
    quit(0)
