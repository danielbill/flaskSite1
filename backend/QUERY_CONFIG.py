# =========================== #
# -*- coding: utf-8 -*-       #
# @Time : 22/2/14 10:43     #
# @Author : 毕磊              #
# @Site : ---                 #
# @File : QUERY_CONFIG.py          #
# @Software: PyCharm  #
# 所有查询的配置定义在此
# =========================== #

class QUERY_CONFIG():
    CONF ={
        #高利润查询配置
        'hm' : {
            'sql':"""(select r.code,r.season,r.name,r.净利率,pe.debt_rate,
                   PE2S,PE4S,PE4S_Y,PE2S_Y,PEkf2S,PEkf4S,PEkf2S_Y,PEkf4S_Y,
                   r.营收环比,r.净利环比,r.扣非环比,
                   y.净利环比 y_nphb,y.扣非环比 y_kfhb,y.营收环比 y_inhb,
                   (lyr.扣非同比+r.扣非同比) kf_2y_tb,
                   (lyr.净利同比+r.净利同比) np_2y_tb,
                   (lyr.营收同比+r.营收同比) in_2y_tb
            from my_season_report r
                     inner join estimate_pe pe on r.code = pe.code
                     left join my_season_report lyr on (lyr.code=r.code and lyr.season='{last_year_q4}')
                     left join my_yubao y on y.code = r.code and y.season = '{next_season}'
            where r.season='{this_season}'
              and (r.净利率>20 and r.净利率<90 and pe.debt_rate<65)
              {where}
            )
            union
            (select r.code,r.season,r.name,r.净利率,pe.debt_rate,
                   PE2S,PE4S,PE4S_Y,PE2S_Y,PEkf2S,PEkf4S,PEkf2S_Y,PEkf4S_Y,
                   r.营收环比,r.净利环比,r.扣非环比,
                   y.净利环比 y_nphb,y.扣非环比 y_kfhb,y.营收环比 y_inhb,
                   (lyr.扣非同比+r.扣非同比) kf_2y_tb,
                   (lyr.净利同比+r.净利同比) np_2y_tb,
                   (lyr.营收同比+r.营收同比) in_2y_tb
            from my_season_report r
                     inner join estimate_pe pe on r.code = pe.code
                     left join my_season_report lyr on (lyr.code=r.code and lyr.season='{last_year_q4}')
                     left join my_yubao y on y.code = r.code and y.season = {this_season}
            where r.season='{last_season}' 
            and (r.净利率>20 and r.净利率<90 and pe.debt_rate<65)
            and r.code not in
              (select code from my_season_report where season='{this_season}')
            {where}    
            )   """,
            #查询参数 yb_hb 预报环比 , 2y_tb 2年增长同比
            'param':['np_rate','debt_rate','pe_2s','yb_hb','ls_tb','y2_tb'],
            #where参数, 查询参数转数据库条件参数
            'where':['r.净利率>','pe.debt_rate<','PE2S<','y.净利环比>',
                     """(r.营收同比> and r.净利同比> )""",
                     """((lyr.营收同比+r.营收同比)> 
                     and (lyr.净利同比+r.净利同比)>)"""],
            #form中查询标签
            'label':['净利率%>','资产负债率%<','PE_2S<','预报净利环比%>','上季营利同比%>','两年营利同比%>'],
            #input 默认值
            'def_val':[30,60,30,-5,30,100],
            #order by
            'order':'in_2y_tb desc',
            #数据表格的表头
            'tableCol':['季度','代码','名称','净利率','负债率','PE_2S',
                        '净利环比','扣非环比','预报净利环比','预报扣非环比','净利两年同比','营收两年同比'],
            #对应数据库返回字段
            'dbCol':['season','code','name','净利率','debt_rate','PE2S',
                     '净利环比','扣非环比','y_nphb','y_kfhb','np_2y_tb','in_2y_tb'],
            #查询的定制页面
            # 'page':

        },
    }

QUERY_CONFIG = QUERY_CONFIG()



