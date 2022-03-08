# =========================== #
# -*- coding: utf-8 -*-       #
# @Time : 22/3/7 21:03     #
# @Author : 毕磊              #
# @Site : ---                 #
# @File : sche_weekly_manager.py          #
# @Software: PyCharm  #
#
# =========================== #
import mypy.ppi_data.ppi_dzb_week as dzb
import mypy.tools.soundTool as sound

def run_weekly_task():
    sound.say("获取大宗榜")
    dzb.get_ppi_dzb_weekly()
    sound.wellDone()


if __name__ == '__main__':
    quit(0)
