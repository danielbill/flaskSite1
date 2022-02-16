# =========================== #
# -*- coding: utf-8 -*-       #
# @Time : 22/2/2 11:32     #
# @Author : 毕磊              #
# @Site : ---                 #
# @File : sche_stock_holders.py          #
# @Software: PyCharm  #
# 股东情况更新任务
# =========================== #
import py.akshare_data.as_getCnInfo_shareholder as holders
import py.tools.financial_report_tool as frt

# 股东变化
def getShareHolder(global_data):
    # 回头改为自动更新,按月或按周
    codes = []
    lat_season = frt.get_season_code_with_day(frt.get_latest_report_season())
    codes.append(lat_season)
    for code in codes:
        holders.getShareHolder_onseason(code)


if __name__ == '__main__':
    getShareHolder(None)
