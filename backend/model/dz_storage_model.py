# =========================== #
# -*- coding: utf-8 -*-       #
# @Time : 22/2/8 18:59     #
# @Author : 毕磊              #
# @Site : ---                 #
# @File : dz_storage_model.mypy          #
# @Software: PyCharm  #
# 大宗期货主页
# =========================== #
import log
import mypy.db.dao.sql_in_stock as sqls
import mypy.db.mysql_db_manager as mydb


def model_for_view():
    view_data = {}
    df  = mydb.queryToDataframe(sqls.sql_latest_storage_chg)
    f_name = ''
    stor_chg = ''
    for index,row in df.iterrows():
        f_name += """'%s',"""  %row['品种']
        stor_chg+=  """'%s',"""  %row['period10_chg_rate']
    f_name = f_name[:-1]
    stor_chg = stor_chg[:-1]
    view_data['f_name'] = f_name
    view_data['stor_chg'] = stor_chg
    log.debug(view_data)
    return view_data


if __name__ == '__main__':
    model_for_view()