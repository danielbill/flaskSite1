# =========================== #
# -*- coding: utf-8 -*-       #
# @Time : 22/2/2 11:02     #
# @Author : 毕磊              #
# @Site : ---                 #
# @File : sche_after_trade_daily.mypy          #
# @Software: PyCharm  #
# 收盘后的日常工作
# =========================== #
import global_data as gd
import log
import mypy.akshare_data.ak_em_mystock_price as msp
import mypy.akshare_data.ak_em_stock_strong as stockStrong
import mypy.akshare_data.ak_em_ztb as emztb
import mypy.akshare_data.ak_lg_market_activity as marketActivity
import mypy.akshare_data.ak_ths_cxd as cxd
import mypy.akshare_data.ak_ths_cxg as cxg
import mypy.akshare_data.as_getEmLatestPrice as priceTool
import mypy.akshare_data.as_getEmStockAbcInfo as stockInfoTool
import mypy.akshare_data.as_getMarketInfo as market
import mypy.akshare_data.bulk_commodity.ak_future_price as fuPrice
import mypy.akshare_data.bulk_commodity.ak_future_storage as fuStorage

import mypy.web_worm.em_web_worm.em_stock_popular_rank as em_rank
import mypy.akshare_data.ak_ths_moneyflow as tmf
import mypy.data_process.processor_manager as processors
import mypy.tools.soundTool as sound

# 收盘更新日常
def update_after_market_close(global_data):
    if global_data is None:
        global_data = gd.Site_global_data()
    if global_data.is_trade_day() == False: return
    # sound.say('开始复盘')
    # 1,更新个股最新价格
    priceTool.getLatestPrice()
    log.info('收盘股价抓取成功')
    # 更新涨停板情况
    update_ztb = emztb.get_ztb()
    update_ztb.allProcess()
    log.info('当日涨停板情况获取成功')
    # 更新强势股情况
    update_strong = stockStrong.get_stock_strong()
    update_strong.allProcess()
    log.info('当日强势股情况获取成功')
    # 更新创新高情况
    update_cxg = cxg.get_cxg()
    update_cxg.allProcess()
    log.info('当日创新高情况获取成功')
    # 更新创新低情况
    update_cxd = cxd.get_cxd()
    update_cxd.allProcess()
    log.info('当日创新低情况获取成功')
    # 更新市场活跃性
    update_market_activity = marketActivity.market_activity()
    update_market_activity.allProcess()
    log.info('当日市场活跃度获取成功')
    # 更新个股热度
    # hotrank.get_today_rank()
    # log.info('当日问财活跃度获取成功')
    # 更新需要十分钟,东财的热度是逐个股票更新的
    emrank_fetcher = em_rank.em_popular_rank_fetcher()
    emrank_fetcher.allProcess()
    log.info('当日收盘东财人气榜获取成功')
    # 在价格之后更新，主要更新股本数据,有依赖关系,以价格表的code为索引进行更新
    # 因为股票过多,所以也需要每日更新
    stockInfoTool.run()
    log.info('股票股本数据更新成功')
    #期货价格数据
    fuPrice_fetcher = fuPrice.Fetcher()
    fuPrice_fetcher.allProcess()
    log.info('期货价格数据更新成功')
    #期货库存数据
    fuStorage_fetcher = fuStorage.Fetcher()
    fuStorage_fetcher.allProcess()
    log.info('期货库存数据更新成功')
    # 获取市场统计情况,主要是成交额,平均市盈率
    market.getMarketInfo()
    log.info('市场大致情况获取成功')
    msp.get_mystock_history_price()
    log.info('自选股价格更新完毕')
    tmf.get_moneyflow()
    log.info('同花顺资金流向更新完毕')

    # -----------------------------------------------------
    log.info('当日收盘结束!')
    sound.wellDone()
    log.info("启动后处理...")
    # -----------------------------------------------------
    # 数据后处理
    after_update_after_marketClose_daily(global_data)
    sound.wellDone()


# 在日收盘后的数据处理程序
def after_update_after_marketClose_daily(global_data):
    processors.process_after_updated_tradedata()
    log.info("数据后处理结束!")


if __name__ == '__main__':
    update_after_market_close(None)
