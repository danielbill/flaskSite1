# =========================== #
# -*- coding: utf-8 -*-       #
# @Time : 22/2/18 18:29     #
# @Author : 毕磊              #
# @Site : ---                 #
# @File : sql_processor.py          #
# @Software: PyCharm  #
#
# =========================== #

from abc import ABCMeta, abstractmethod
from backend.QUERY_CONFIG import QUERY_CONFIG

_where = '{where}'
_order ='{order}'
_limit = '{limit}'
class SQL_PROCESSOR(metaclass=ABCMeta):

    def __init__(self,query_key,param):
        self.query_key = query_key
        self.param = param
        self.query_conf=QUERY_CONFIG.CONF.get(query_key)
        self.sql = self.query_conf.get('sql')

    #sql inner join outer join left join and so on
    def _assemble_join(self,param,query_conf)->dict:
        return {}

    @abstractmethod #where 语句
    def _assemble_where(self,param,query_conf)->str:
        pass

    def _assemble_order(self,param,query_conf)->str:
        orderby='\n     order by '
        order_key = param.get('order_key')
        if order_key is not None:
            order_way = param.get('order_way')
            if order_way is None : order_way = 'desc'
            return orderby+f'{order_key} {order_way}'

        if query_conf.get('order') is not None:
            return orderby+query_conf.get('order')

        return ''


    def _assemble_limit(self,param)->str:
        return " \n     limit 100 "

    def _prepare_sql(self,sql,param,query_conf):
        if sql.find(_where) == -1 :#如果提前写了复杂的查询语句,内置了{where}变量,则跳过
            sql += _where
        if sql.find('order') == -1 :
            sql += _order
        if sql.find('limit') == -1 :
            sql += _limit
        return sql

    #拼装sql
    def process(self)->str:
        sql = self._prepare_sql(self.sql,self.param,self.query_conf)
        sql_param = {}
        join_param = self._assemble_join(self.param,self.query_conf)
        sql_param.update(join_param)
        where_str = self._assemble_where(self.param,self.query_conf)
        sql_param['where']=where_str
        order_str = self._assemble_order(self.param,self.query_conf)
        sql_param['order']=order_str
        limit_str = self._assemble_limit(self.param)
        sql_param['limit']=limit_str
        sql = sql.format(**sql_param)
        return sql

if __name__ == '__main__':
    quit(0)
