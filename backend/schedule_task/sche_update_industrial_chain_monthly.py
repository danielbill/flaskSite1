# =========================== #
# -*- coding: utf-8 -*-       #
# @Time : 22/2/9 7:59     #
# @Author : 毕磊              #
# @Site : ---                 #
# @File : sche_update_industrial_chain_monthly.mypy          #
# @Software: PyCharm  #
#
# =========================== #

import mypy.akshare_data.bulk_commodity.ak_industrial_chain as ic
import log

def update():
    fetcher = ic.Fetcher()
    fetcher.allProcess()
    log.info("产业链数据更新完毕")

if __name__ == '__main__':
    quit(0)
