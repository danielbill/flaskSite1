# =========================== #
# -*- coding: utf-8 -*-       #
# @Time : 22/2/14 12:09     #
# @Author : 毕磊              #
# @Site : ---                 #
# @File : query_model.mypy          #
# @Software: PyCharm  #
#
# =========================== #
import log
import mypy.db.mysql_db_manager as mydb
import mypy.db.dao.sql_query_in_stock as sqls
import backend.QUERY_CONFIG as qc
import backend.model.extra.extra_manager as em


def df_from_db(query_key, param):
    sqlPro = em.QUERY_EXTRAS.get(query_key)
    if sqlPro is None : sqlPro = em.QUERY_EXTRAS.get('common')
    pro = sqlPro.sql_processor(query_key, param)
    sql = pro.process()
    # print(sql)
    df = mydb.queryToDataframe(sql)
    return df


if __name__ == '__main__':
    df = df_from_db('hm1',{})
    print(df)
