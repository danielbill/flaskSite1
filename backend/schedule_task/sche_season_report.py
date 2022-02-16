# =========================== #
# -*- coding: utf-8 -*-       #
# @Time : 22/2/7 16:32     #
# @Author : 毕磊              #
# @Site : ---                 #
# @File : sche_season_report.py          #
# @Software: PyCharm  #
#
# =========================== #
import log
import py.akshare_data.as_em_yjbb_kb as bb_kb

import py.tools.financial_report_tool as frt


def get_allreport(global_data):
    if frt.is_fina_report_time() == False:
        log.info("不是发布快报的时段,pass")
        return
    get_em_seasonreport()

#更新东财财务快报,这会变更财务报表更新的逻辑
def get_em_seasonreport():


    fetcher = bb_kb.Fetcher()
    fetcher.allProcess()


if __name__ == '__main__':
    quit(0)
