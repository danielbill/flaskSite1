# =========================== #
# -*- coding: utf-8 -*-       #
# @Time : 22/2/2 10:24     #
# @Author : 毕磊              #
# @Site : ---                 #
# @File : sche_before_trade_daily.py          #
# @Software: PyCharm  #
# 开盘前的定时任务
# =========================== #
import log
import py.akshare_data.as_getMarketInfo as market
import py.akshare_data.as_iwc_hotrank as hotrank
import py.data_process.processor_manager as processors
import py.web_worm.em_web_worm.em_stock_popular_rank as em_rank


# 开盘前的数据更新
def update_before_marketOpen_daily(global_data):
    if global_data.is_trade_day() == False: return
    # 更新个股热度 更新速度快
    hotrank.get_today_rank()
    log.info('爱问财热度更新成功')
    # 更新需要十分钟,东财的热度是逐个股票更新的
    emrank_fetcher = em_rank.em_popular_rank_fetcher()
    emrank_fetcher.allProcess()
    log.info('东财人气更新成功')
    # 获取市场统计情况,主要是成交额,平均市盈率
    market.getMarketInfo()
    log.info('市场大致情况获取成功')
    log.info('..............')
    log.info('数据处理中....')
    after_update(global_data)
    log.info('早盘前处理全部完成!')

# 在日收盘后的数据处理程序
def after_update(global_data):
    processors.process_before_marketOpen()
    log.info("开盘前,数据处理结束!")

if __name__ == '__main__':
    quit(0)
