# =========================== #
# -*- coding: utf-8 -*-       #
# @Time : 22/2/2 11:32     #
# @Author : 毕磊              #
# @Site : ---                 #
# @File : sche_stock_holders.py          #
# @Software: PyCharm  #
# 股东情况更新任务
# =========================== #
import py.akshare_data.as_shareholder as holders
import py.tools.financial_report_tool as frt

# 股东变化
def getShareHolder(global_data):
    seasons = []
    lat_season = frt.get_season_code_with_day(frt.get_latest_report_season())
    seasons.append(lat_season)
    for season in seasons:
        #更新频率一般般,按季度批量更新所有个股,每周执行一次比较合适
        holders.getEmShareHolder(season)

    #东财按照个股更新的股东变动情况,更新频率高
    holders.get_all_holder_detail()


if __name__ == '__main__':
    getShareHolder(None)
