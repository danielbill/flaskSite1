# =========================== #
# -*- coding: utf-8 -*-       #
# @Time : 22/2/3 16:19     #
# @Author : 毕磊              #
# @Site : ---                 #
# @File : index_model.py          #
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
    return view_data


if __name__ == '__main__':
    model_for_view()
