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


# 股东变化
def getShareHolder(global_data):
    # 回头改为自动更新,按月或按周
    codes = ['20211231']
    holders.getShareHolder_onseason(codes)


if __name__ == '__main__':
    quit(0)
