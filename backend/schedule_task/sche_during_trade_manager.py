# =========================== #
# -*- coding: utf-8 -*-       #
# @Time : 22/2/18 12:38     #
# @Author : 毕磊              #
# @Site : ---                 #
# @File : sche_during_trade_manager.py          #
# @Software: PyCharm  #
#
# =========================== #
import py.akshare_data.as_getEmLatestPrice as p

#交易盘中任务
def on_trading_task(global_data):
    if global_data.is_trade_day() == False:return
    #更新价格
    p.getLatestPrice()


if __name__ == '__main__':
    quit(0)
