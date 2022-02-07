# =========================== #
# -*- coding: utf-8 -*-       #
# @Time : 22/2/2 11:13     #
# @Author : 毕磊              #
# @Site : ---                 #
# @File : sche_yubao.py          #
# @Software: PyCharm  #
# 一年四次的预报处理任务
# 包括获取或后计算两层任务
# =========================== #
import log
import py.akshare_data.as_getEmYugao as yugao
import py.core_value_computing.yubao_calculator as yubao_cal
import py.tools.financial_report_tool as frt


# 取预报,在每年的四个指定时段,目前还未优化到指定时段运行
def get_yubao(global_data):
    if frt.is_yubao_time() == False : return
    yugao.run()
    log.info('东财预告抓取完毕.')
    log.info('执行预报价值计算,请确保上季度季报价值计算已完成...')
    cal_yubao_value()
    log.info('预报价值计算完毕***')


# 计算预报价值前，上一季度的季报必须先计算完成
def cal_yubao_value():
    yubao_cal.calculate_yb_value()


if __name__ == '__main__':
    quit(0)
