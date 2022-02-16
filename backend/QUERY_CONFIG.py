# =========================== #
# -*- coding: utf-8 -*-       #
# @Time : 22/2/14 10:43     #
# @Author : 毕磊              #
# @Site : ---                 #
# @File : QUERY_CONFIG.py          #
# @Software: PyCharm  #
# 所有查询的配置定义在此
# =========================== #
import log

#mysql查询条件符号
MYSQL_WHERE_OPERATOR = ['>','<','=','<>','>=','<=']

class QUERY_CONFIG():
    CONF ={
        #高利润查询配置
        'hm' : {
            #查询参数 yb_hb 预报环比 , 2y_tb 2年增长同比
            'param':['np_rate','debt_rate','pe_2s','yb_hb','ls_tb','y2_tb'],
            #where参数, 查询参数转数据库条件参数
            'where':['r.净利率>','r.资产负债率<','PE_2S<','yv.netprofit_hb>',
                     """(r.`营业收入-同比增长`> and r.`净利润-同比增长`> )""",
                     """((lyr.`营业收入-同比增长`+r.`营业收入-同比增长`)> 
                     and (lyr.`净利润-同比增长`+r.`净利润-同比增长`)>)"""],
            #form中查询标签
            'label':['净利率%>','资产负债率%<','PE_2S<','预报净利环比%>','上季营利同比%>','两年营利同比%>'],
            #input 默认值
            'def_val':[35,55,25,5,30,70],
            #order by
            'order':'netprofit_hb desc',
            #数据表格的表头
            'tableCol':['代码','名称','净利率','负债率','PE_2S','预报净利环比','预报扣非环比','净利两年同比','营收两年同比'],
            #对应数据库返回字段
            'dbCol':['股票代码','股票简称','净利率','资产负债率','PE_2S','netprofit_hb','kfprofit_hb','np_2y_tb','in_2y_tb'],
        },
    }

QUERY_CONFIG = QUERY_CONFIG()

#根据查询拼装完整的where条件
def get_where_condition(query_key,params):
    where = ''
    try:
        param_in_where = QUERY_CONFIG.CONF[query_key]['param']
        where_condition = QUERY_CONFIG.CONF[query_key]['where']
    except:
        log.error('query key in QUERY_CONFIG is wrong, or param or where 没设置')
    #获取查询参数的key和对应的index
    for index,key in enumerate(param_in_where) :
        try:
            #查询参数的值
            val = params.get(key)
            if val is None or val=='':continue
            #获取该参数对应的where条件
            where_cond = where_condition[index]
            #增加format符号
            where_cond = _add_str_format_symbol(where_cond)
            #替换占位符为查询值
            where+=' and ' + where_cond.format(a=val)
        except Exception as e:
            continue
    return where

def get_order_condition(query_key,params):
    try:
        order_condition = QUERY_CONFIG.CONF[query_key]['order']
        if order_condition is None :return
    except:
        log.error('query key in QUERY_CONFIG is wrong, or param or where 没设置')
    #回头完善
    order_key = params.get('order_key')
    order_way = params.get('order_way')
    order_condition = ' order by '+order_condition
    return order_condition



def _add_str_format_symbol(str):
    for sym in MYSQL_WHERE_OPERATOR:
        str = str.replace(sym, sym +'{a} ')
    return str

if __name__ == '__main__':
    # print(QUERY_CONFIG.CONF['hm']['where'])
    where  = """and (lyr.`营业收入-同比增长`+r.`营业收入-同比增长`)>
    and (lyr.`净利润-同比增长`+r.`净利润-同比增长`)<"""
    symbols = ['>','<','=','<>']
    for sym in symbols :
        where = where.replace(sym, sym +'{a} ')

    print(where)
    print(where.format(a=65))


