# =========================== #
# -*- coding: utf-8 -*-       #
# @Time : 22/2/9 8:01     #
# @Author : 毕磊              #
# @Site : ---                 #
# @File : sche_monthly_manager.py          #
# @Software: PyCharm  #
#
# =========================== #
import backend.schedule_task.sche_update_industrial_chain_monthly as ic
import log

#所有月更新任务在此处注册
def run_monthly_task():
    #东财产业链内容月更新 -- 橡塑无法更新
    ic.update()
    log.info("产业链更新成功")

if __name__ == '__main__':
    quit(0)
