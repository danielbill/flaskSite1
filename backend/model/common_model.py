# =========================== #
# -*- coding: utf-8 -*-       #
# @Time : 22/2/20 9:39     #
# @Author : 毕磊              #
# @Site : ---                 #
# @File : common_model.mypy          #
# @Software: PyCharm  #
#
# =========================== #
import mypy.db.mysql_db_manager as mydb
import backend.model.view_data_manager as vdm
import log

def get_view_data(view_key,param:dict):
    log.debug('view key is %s ' %view_key)
    view_conf = vdm.VIEW_CONF.get(view_key)
    if view_conf is None : return
    param_in = view_conf.get('param')
    param_out ={}
    param_query = {}
    for p in param_in:
        val = param.get(p)
        if val is None : continue
        param_query[p]=val
    sqls = view_conf.get('query')
    if sqls is None or len(sqls)==0:return
    for key in sqls.keys():
        sql = sqls.get(key)
        sql = sql.format(**param_query)
        df = mydb.queryToDataframe(sql)
        param_out[key] = df.fillna(0)#空值填充为0, 只为了视图使用,持久层应该保持空值
    log.debug(param_out)
    return param_out



if __name__ == '__main__':
    get_view_data('stock.company_detail',{'code':'000960'})
