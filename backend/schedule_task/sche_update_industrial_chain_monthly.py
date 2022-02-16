# =========================== #
# -*- coding: utf-8 -*-       #
# @Time : 22/2/9 7:59     #
# @Author : 毕磊              #
# @Site : ---                 #
# @File : sche_update_industrial_chain_monthly.py          #
# @Software: PyCharm  #
#
# =========================== #

import py.akshare_data.bulk_commodity.ak_industrial_chain as ic

def update():
    fetcher = ic.Fetcher()
    fetcher.allProcess()

if __name__ == '__main__':
    quit(0)
