# =========================== #
# -*- coding: utf-8 -*-       #
# @Time : 22/2/18 19:53     #
# @Author : 毕磊              #
# @Site : ---                 #
# @File : sql_common_processor.py          #
# @Software: PyCharm  #
#
# =========================== #
import backend.model.extra.sql_processor as sp
import py.db.dao.sql_query_in_stock as sqlq
import log

#mysql查询条件符号
MYSQL_WHERE_OPERATOR = ['>','<','=','<>','>=','<=']

class sql_processor(sp.SQL_PROCESSOR):
    def _assemble_where(self, param, query_conf) -> str:
        return self._where_helper(param,query_conf)


    def _where_helper(self,param,query_conf):
        where = ''
        try:
            param_in_where = query_conf['param']
            where_condition = query_conf['where']
        except:
            log.error('query key in QUERY_CONFIG is wrong, or param or where 没设置')
        #获取查询参数的key和对应的index
        for index,key in enumerate(param_in_where) :
            try:
                #查询参数的值
                val = param.get(key)
                if val is None or val=='':continue
                #获取该参数对应的where条件
                where_cond = where_condition[index]
                #增加format符号
                where_cond = self._add_str_format_symbol(where_cond)
                #替换占位符为查询值
                where+=' and ' + where_cond.format(a=val)
            except Exception as e:
                continue

        return where


    def _add_str_format_symbol(self,str):
        for sym in MYSQL_WHERE_OPERATOR:
            str = str.replace(sym, sym +'{a} ')
        return str


if __name__ == '__main__':
    sql = sqlq.QUERY_SQLS.get('hm1')
    sp = sql_processor(query_key='hm1', param={'np_rate':50})
    print(sp.process())