# =========================== #
# -*- coding: utf-8 -*-       #
# @Time : 22/2/20 9:45     #
# @Author : 毕磊              #
# @Site : ---                 #
# @File : view_data_manager.mypy          #
# @Software: PyCharm  #
# 视图所需的数据和提供的参数,集中管理在此处
# =========================== #
import mypy.db.dao.sql_query_in_stock as sqls
#页面查询的入参/处理/出参定义
VIEW_CONF ={
    #dir.view_key
    'stock.company_detail':{
        'param':['code','codeOrName'],
        'query':{
            'yubao':sqls.QUERY_SQLS.get('my_yubao_and_pe_bycode'),
            'report':sqls.QUERY_SQLS.get('my_report_and_pe_bycode'),
            #8季 单季度营收净利扣非 走势图
            'ink_trend':"""select season,code,s营收,s净利,s扣非 from my_yubao
                        where code={code} and season in
                        (select max(season) from my_yubao)
                        union
                        select season,code,s营收,s净利,s扣非 from my_season_report
                        where code={code}
                        order by season desc limit 12""",
            #8季度 净利率 负债率走势图
            'ndrate_trend':"""select r.season,r.code,r.净利率,r.资产负债率,i.ROA,i.ROEA,i.npMARgin npr
                        from my_season_report r, u_earn_indicator i
                        where r.code={code} and i.code=r.code and i.season=r.season
                        order by r.season desc limit 12""",
            #季度股东人数\持股变化图
            'holder_change':sqls.QUERY_SQLS.get('holder_detail_bycode'),
        }
    }
}

if __name__ == '__main__':
     s = 'xxxxxx{v1}xxxx{v2}'
     s1 = 'xxxxxx{v1}xxxx{v4}'
     param ={
         'v1':123,
         'v2':'ccc',
         'v4':'mmmm'
     }
     print(s.format(**param))
     print(s1.format(**param))
