# =========================== #
# -*- coding: utf-8 -*-       #
# @Time : 22/3/3 8:50     #
# @Author : 毕磊              #
# @Site : ---                 #
# @File : sche_atnight_daily.py          #
# @Software: PyCharm  #
# 深夜收盘作业
# =========================== #
import mypy.akshare_data.as_sina_finaIndic2 as sfi2
import mypy.tools.financial_report_tool as frt
import log
import backend.schedule_task.sche_stock_holders as ssh
import mypy.tools.soundTool as sound

#更新东财季报
def do_jobs_atnight(global_data):
    sound.say('更新财务指标和股东人数')
    #更新财务指标
    _update_sina_fi()
    #更新股东人数
    ssh.getShareHolder()
    sound.wellDone()


def _update_sina_fi():
    if frt.is_fina_report_time() == False:
        log.info("不是发布快报的时段,pass")
        return
    #更新财务指标表,同比扣非给my_season_report,并更新扣非相关计算值
    sfi2.get_sina_financial_indicator()


if __name__ == '__main__':
    sound.say('更新财务指标和股东人数')
