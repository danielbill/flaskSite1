# =========================== #
# -*- coding: utf-8 -*-       #
# @Time : 22/1/25 20:33     #
# @Author : 毕磊              #
# @Site : ---                 #
# @File : scheduleManager.py          #
# @Software: PyCharm  #
# =========================== #
from flask_apscheduler import APScheduler  # 引入APScheduler
import time
import py.db.mysql_db_manager as mydb
import py.akshare_data.as_getEmYugao as yugao
import py.akshare_data.as_getEmLatestPrice as priceTool
import py.akshare_data.as_getEmStockAbcInfo as stockInfoTool
import py.core_value_computing.yubao_calculator as yubao_cal
import py.akshare_data.as_getCnInfo_shareholder as holders
import py.akshare_data.as_getMarketInfo as market
import log




# 任务配置类
class SchedulerConfig(object):
    JOBS = [
        {
            'id': '东财预告定时抓取任务',  #
            'func': 'scheduleManager:get_yubao',  # 任务执行程序
            'args': None,  # 执行程序参数
            'trigger': 'interval',  # 任务执行类型，定时器
            'minutes': 30  # 任务执行时间，单位秒
        },
        {
            'id': '每日收盘股价更新任务',  #
            'func': 'scheduleManager:get_latestPrice',  # 任务执行程序
            'args': None,  # 执行程序参数
            'trigger': 'cron',
            'day_of_week': '0-4',  # 每周1至周516点执行
            'hour': 16,
            'minute': 1
        },
        {
            'id': '预报计算任务',  #
            'func': 'scheduleManager:cal_yubao_value',  # 任务执行程序,并不应当定时任务，而是应当由更新触发
            'args': None,  # 执行程序参数
            'trigger': 'interval',  # 任务执行类型，定时器
            'minutes': 60  # 任务执行时间，单位秒
        },
        {
            'id': '更新股票基础信息',  #
            'func': 'scheduleManager:update_stack_abc_info',  # 任务执行程序
            'trigger': 'cron',
            'day_of_week': '0-4',  # 每周1至周516点执行
            'hour': 16,
            'minute': 10
        },
        {
            'id': '获取市场总体情况',  #
            'func': 'scheduleManager:getMarketInfo',  # 任务执行程序
            'trigger': 'cron',
            'day_of_week': '0-4',  # 每周1至周516点执行
            'hour': 16,
            'minute': 2
        },
        {
            'id': '获取股东变化情况',  #
            'func': 'scheduleManager:getShareHolder',  # 任务执行程序
            'trigger': 'cron',
            'day_of_week': 'sat',  # 每周1至周516点执行
            'hour': 18,
            'minute': 2
        }
    ]
    SCHEDULER_API_ENABLED = True


# 定义任务执行程序
def get_yubao():
    yugao.run()
    log.info('东财预告抓取')

#取得市场运行中的股票代码
def get_latestPrice():
    priceTool.getLatestPrice()
    log.info('收盘股价抓取时间')

#在价格之后更新，主要更新股本数据
def update_stack_abc_info():
    stockInfoTool.run()
    log.info('收盘股价抓取时间')


#计算预报价值前，上一季度的季报必须先计算完成
def cal_yubao_value():
    yubao_cal.calculate_yb_value()
    log.info('预报计算时间')


# 获取市场情况
def getMarketInfo():
    market.getMarketInfo()
    log.info('市场大致情况获取时间')


#股东变化
def getShareHolder():
    #回头改为自动更新
    codes = [ '20211231']
    holders.getShareHolder_onseason(codes)


if __name__ == '__main__' :
    get_latestPrice()
    get_yubao()



