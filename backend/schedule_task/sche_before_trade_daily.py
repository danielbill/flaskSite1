# =========================== #
# -*- coding: utf-8 -*-       #
# @Time : 22/2/2 10:24     #
# @Author : 毕磊              #
# @Site : ---                 #
# @File : sche_before_trade_daily.py          #
# @Software: PyCharm  #
# 开盘前的定时任务
# =========================== #
import py.akshare_data.as_iwc_hotrank as hotrank
import py.web_worm.em_web_worm.em_stock_popular_rank as em_rank


# 开盘前的数据更新
def update_before_marketOpen_daily(global_data):
    if global_data.is_trade_day() == False: return
    # 更新个股热度 更新速度快
    hotrank.get_today_rank()
    # 更新需要十分钟,东财的热度是逐个股票更新的
    emrank_fetcher = em_rank.em_popular_rank_fetcher()
    emrank_fetcher.allProcess()


if __name__ == '__main__':
    quit(0)
