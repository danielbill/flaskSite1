# =========================== #
# -*- coding: utf-8 -*-       #
# @Time : 22/2/14 10:43     #
# @Author : 毕磊              #
# @Site : ---                 #
# @File : QUERY_CONFIG.mypy          #
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
        #自选股查询配置
        'mystock' : {
            'sql':"""select s.code,s.name,s.industry,r.成长性,r.成长排名,r.盈利能力,r.盈利排名,
                           pe4s,pe2s,pe4s_y,pe2s_y,pekf2s_y,pekf2s_y,pop.`rank`,
                           lp.最新价 最新,lp.成交额 金额,lp.换手率 换手,lp.总市值,lp.涨跌幅
                    from my_stock s,my_score r,estimate_pe p,em_stock_popular_rank pop,em_latestprice lp
                    where s.code =r.code and s.code=p.code and s.code=pop.scode and lp.代码=s.code""",
            #order by
            'order':'code',
            #查询页名称
            'search_title':'自选股',
            #是否显示查询面板
            'show_search':False,
            #数据表格的表头
            'tableCol':['代码','名称','行业','人气','最新','涨跌幅','换手','市值','成长性','成长排名','盈利能力','盈利排名',
                        'pe4s','pe4s_y','pe2s_y','pekf2s_y'],
            #对应数据库返回字段
            'dbCol':['code','name','industry','rank','最新','涨跌幅','换手','总市值','成长性','成长排名','盈利能力','盈利排名',
                     'pe4s','pe4s_y','pe2s_y','pekf2s_y'],
            #数据表格的高度
            'tableHeight':500,
            #查询的定制页面
            # 'page':
            'extra': {
                'codeToDetail':0#点击数据表格的code列,打开个股详情页面,1代表第二列
            }

        },
        #自选股查询配置
        'ms_mkt' : {
            'sql':"""select ms.code,ms.name,lp.涨跌幅,lp.成交额,lp.换手率,r.`rank`,
                       lp.ae,lp.ae-mp.avg20_ae ae_chg,lp.rank_ae,lp.rank_amount,
                      mp.avg20_ae,mp.avg20_excg,mp.avg20_amount
                from my_stock ms, my_stock_price mp,em_stock_popular_rank r,em_latestprice lp
                where ms.code=mp.code and ms.code=r.scode and ms.code=lp.代码
                and mp.日期 = (select max(日期) from my_stock_price)
                order by rank_ae""",
            #数据表格的表头
            'tableCol':['代码','名称','涨幅','换手','金额','东财','活跃排名','活跃度','活跃-20',
                        '金额排名','活跃a20','金额a20','换手a20'],
            #对应数据库返回字段
            'dbCol':['code','name','涨跌幅','换手率','成交额','rank','rank_ae','ae','ae_chg',
                     'rank_amount','avg20_ae','avg20_amount','avg20_excg'],
            #数据表格的高度
            'tableHeight':480,
            #查询的定制页面
            'page':'query/mystock.html',
            'extra': {
                'codeToDetail':0#点击数据表格的code列,打开个股详情页面,1代表第二列
            }
        },
        #自选股查询配置
        'ms_est' : {
            'sql':"""select ms.code,ms.name,season, 
                    PE4S, PE2S, PEkf4S, PEkf2S, PE2S_Y, PE4S_Y, PEkf2S_Y, PEkf4S_Y, season_y
                    from my_stock ms, estimate_pe pe
                    where ms.code=pe.code
                    order by pe4s""",
            #数据表格的表头
            'tableCol':['代码','名称','季度','PE4S','PE2S','PEkf4S','PEkf2S','预报季','PE2S_Y',
                        'PE4S_Y','PEkf4S_Y','PEkf2S_Y'],
            #对应数据库返回字段
            'dbCol':['code','name','season','PE4S','PE2S','PEkf4S','PEkf2S','season_y','PE2S_Y',
                     'PE4S_Y','PEkf4S_Y','PEkf2S_Y'],
            #数据表格的高度
            'tableHeight':480,
            #查询的定制页面
            'page':'query/mystock.html',
            'extra': {
                'codeToDetail':0#点击数据表格的code列,打开个股详情页面,1代表第二列
            }

        },
        #排名表查询配置
        'rank' : {
            'sql':"""select * from my_score                     
                    where 成长排名 is not null and 盈利排名 is not null 
                    {where}                    
                    order by 成长排名 limit 100""",
            #查询参数
            'param':['grow_rank','earn_rank'],
            #where参数, 查询参数转数据库条件参数
            'where':['成长排名<','盈利排名<'],
            #form中查询标签
            'label':['成长排名<','盈利排名<'],
            #input 默认值
            'def_val':[200,500],
            #order by
            'order':'成长排名',
            #查询页名称
            'search_title':'排名',
            #是否显示查询面板
            'show_search':True,
            #数据表格的表头
            'tableCol':['代码','名称','g_season','成长排名','成长性','e_season','盈利排名','盈利能力'],
            #对应数据库返回字段
            'dbCol':['code','name','g_season','成长排名','成长性','e_season','盈利排名','盈利能力'],
            #查询的定制页面
            # 'page':
            #通用定制项
            'extra': {
                'codeToDetail':0#点击数据表格的code列,打开个股详情页面,1代表第二列
            }
        },
        #预报暴增
        'strategy.yrglp' : { #预告暴增低PE
            'sql':"""select yrg.*,y.净利环比,y.扣非环比,y.营收环比,y.净利同比,y.扣非同比,y.营收同比,
                       PE4S, PE2S, PEkf4S, PEkf2S, PE2S_Y, PE4S_Y, PEkf2S_Y, PEkf4S_Y,
                       r.`rank`
                from my_choice yrg, my_yubao y,estimate_pe p,em_stock_popular_rank r
                where yrg.code = y.code and y.code = p.code and r.scode = p.code
                  and yrg.type='yrglp'
                  and yrg.season = y.season and y.season = p.season_y
                 {where}
                order by PE2S_Y""",
            #查询参数
            'param':['season'],
            #where参数, 查询参数转数据库条件参数
            'where':['yrg.season='],
            #数据表格的表头
            'tableCol':['季度','代码','名称','人气','PE2S_Y','PEkf2S_Y','净利环比','扣非环比','营收环比'],
            #对应数据库返回字段
            'dbCol':['season','code','name','rank','PE2S_Y','PEkf2S_Y','净利环比','扣非环比','营收环比'],
            #查询的定制页面
            'page':'strategy/strategy_tmpt.html',
            #通用定制项
            'extra': {
                'codeToDetail':1#点击数据表格的code列,打开个股详情页面,1代表第二列
            }
        },
        #预报高增
        'strategy.yhglp' : { #预告暴增低PE
            'sql':"""select yrg.*,y.净利环比,y.扣非环比,y.营收环比,y.净利同比,y.扣非同比,y.营收同比,
                       PE4S, PE2S, PEkf4S, PEkf2S, PE2S_Y, PE4S_Y, PEkf2S_Y, PEkf4S_Y,
                       r.`rank`
                from my_choice yrg, my_yubao y,estimate_pe p,em_stock_popular_rank r
                where yrg.code = y.code and y.code = p.code and r.scode = p.code
                  and yrg.type='yhglp'
                  and yrg.season = y.season and y.season = p.season_y
                  {where}
                order by PE2S_Y""",
            #查询参数
            'param':['season'],
            #where参数, 查询参数转数据库条件参数
            'where':['yrg.season='],
            #数据表格的表头
            'tableCol':['季度','代码','名称','人气','PE2S_Y','PEkf2S_Y','净利环比','扣非环比','营收环比'],
            #对应数据库返回字段
            'dbCol':['season','code','name','rank','PE2S_Y','PEkf2S_Y','净利环比','扣非环比','营收环比'],
            #查询的定制页面
            'page':'strategy/strategy_tmpt.html',
            #通用定制项
            'extra': {
                'codeToDetail':1#点击数据表格的code列,打开个股详情页面,1代表第二列
            }
        },
        #预报高增
        'strategy.hmse' : { #5高利润稳增长 high margin steady expand
            'sql':"""select hm.*,rk.`rank`,p.rank_ae,pe.PE4S,pe.PE2S_Y,
                           pe.debt_rate,r.营收同比,r.净利同比,r.扣非同比
                    from precho_2y_highmargin hm, estimate_pe pe ,my_choice c,
                         my_season_report r ,em_stock_popular_rank rk,em_latestprice p
                    where hm.code=pe.code and hm.code=r.code and hm.code=rk.scode
                      and p.代码=hm.code and hm.season = r.season and c.code=hm.code
                      and c.type='hmse'
                    order by hm.peg""",
            #数据表格的表头
            'tableCol':['代码','名称','季度','PEG','净利同比','营收同比','人气','活跃排名','score_2y','PE4S','PE2S_Y','roa_y3','roe_y3','净利率_y3'],
            #对应数据库返回字段
            'dbCol':['code','name','season','peg','净利同比','营收同比','rank','rank_ae','score_2y','PE4S','PE2S_Y','roa_y3','roe_y3','净利率_y3'],
            #查询的定制页面
            'page':'strategy/strategy_tmpt.html',
            #通用定制项
            'extra': {
                'codeToDetail':0#点击数据表格的code列,打开个股详情页面,1代表第二列
            }
        },
        #预报扭亏为盈
        'strategy.yd2e' : {
            'sql':"""select y.*,pe.PEkf2S_Y,pe.PE2S_Y,pe.PEkf4S_Y,pe.PE4S_Y,r.`rank`,p.总市值,p.最新价
                    from my_yubao y , estimate_pe pe, em_latestprice p,em_stock_popular_rank r
                    where y.code=pe.code and y.code=p.代码 and y.season = pe.season_y and y.code=r.scode
                       {where}
                       and 预报类型='扭亏' and s净利>0 and s扣非>0 and 净利环比>0 and 扣非环比>0 and 净利同比>10
                    and r.`rank`<2000
                    order by 总市值""",
            #查询参数
            'param':['season'],
            #where参数, 查询参数转数据库条件参数
            'where':['y.season='],
            #数据表格的表头
            'tableCol':['季度','代码','名称','人气','PE4S_Y','PEkf4S_Y','总市值','最新价'],
            #对应数据库返回字段
            'dbCol':['season','code','name','rank','PE4S_Y','PEkf4S_Y','总市值','最新价'],
            #查询的定制页面
            'page':'strategy/strategy_tmpt.html',
            #通用定制项
            'extra': {
                'codeToDetail':1#点击数据表格的code列,打开个股详情页面,1代表第二列
            }
        },
        #预报减亏
        'strategy.ysrd' : {
            'sql':"""select y.*,pe.PEkf2S_Y,pe.PE2S_Y,pe.PEkf4S_Y,pe.PE4S_Y,r.`rank`,p.总市值,p.最新价
                    from my_yubao y , estimate_pe pe, em_latestprice p,em_stock_popular_rank r
                    where y.code=pe.code and y.code=p.代码 and y.season = pe.season_y and y.code=r.scode
                      {where}
                      and 预报类型='减亏' and s净利>0 and s扣非>0 and 净利环比>0 and 扣非环比>0
                    order by 总市值""",
            #查询参数
            'param':['season'],
            #where参数, 查询参数转数据库条件参数
            'where':['y.season='],
            #数据表格的表头
            'tableCol':['季度','代码','名称','人气','PE4S_Y','PEkf4S_Y','总市值','最新价'],
            #对应数据库返回字段
            'dbCol':['season','code','name','rank','PE4S_Y','PEkf4S_Y','总市值','最新价'],
            #查询的定制页面
            'page':'strategy/strategy_tmpt.html',
            #通用定制项
            'extra': {
                'codeToDetail':1#点击数据表格的code列,打开个股详情页面,1代表第二列
            }
        },
        #连续三年扩张
        'strategy.hse' : {
            'sql':"""select h.code,h.name,h.season,pe.PE4S,pe.PE2S,
                           pe.PE4S_Y,pe.PE2S_Y,rk.`rank`,r.ROE,r.净利率,
                           h.三年净利同比,h.三年营收同比,h.三年扣非同比,
                           h.两年净利同比,h.两年营收同比,h.两年扣非同比,
                           h.净利同比,h.营收同比,h.扣非同比,r.资产负债率
                    from my_choice_hse h, estimate_pe pe ,em_stock_popular_rank rk,my_season_report r
                    where h.code = pe.code and h.code=rk.scode and h.code=r.code
                    and r.season = (select max(season) from my_season_report where code=h.code)
                    order by pe4s""",
            #数据表格的表头
            'tableCol':['代码','名称','季度','人气','PE4S','PE2S','PE2S_Y',
                        '三年净利同比','三年营收同比','三年扣非同比',
                        '净利同比','营收同比','扣非同比','ROE','净利率','资产负债率',
                        '两年净利同比','两年营收同比','两年扣非同比'],
            #对应数据库返回字段
            'dbCol':['code','name','season','rank','PE4S','PE2S','PE2S_Y',
                     '三年净利同比','三年营收同比','三年扣非同比',
                     '净利同比','营收同比','扣非同比','ROE','净利率','资产负债率',
                     '两年净利同比','两年营收同比','两年扣非同比'],
            #查询的定制页面
            'page':'strategy/strategy_tmpt.html',
            #通用定制项
            'extra': {
                'codeToDetail':0#点击数据表格的code列,打开个股详情页面,1代表第二列
            }
        },
        #市场成交活跃200
        'strategy.mp' : {
            'sql':"""select p.代码 code, p.名称 name, p.涨跌幅, p.换手率,round(p.成交额/100000000,2) as amount,p.rank_ae,r.`rank`,i.行业
                    from em_latestprice p, em_stock_popular_rank r, em_stockabcinfo i
                    where r.scode = p.代码 and p.代码=i.股票代码
                    order by rank_ae limit 200""",
            #数据表格的表头
            'tableCol':['代码','名称','涨幅','换手','金额','活跃排名','东财人气','行业'],
            #对应数据库返回字段
            'dbCol':['code','name','涨跌幅','换手率','amount','rank_ae','rank','行业'],
            #查询的定制页面
            'page':'strategy/strategy_tmpt.html',
            #通用定制项
            'extra': {
                'codeToDetail':0#点击数据表格的code列,打开个股详情页面,1代表第二列
            }
        },
    }

QUERY_CONFIG = QUERY_CONFIG()



