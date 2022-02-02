# =========================== #
# -*- coding: utf-8 -*-       #
# @Time : 22/1/25 20:33     #
# @Author : 毕磊              #
# @Site : ---                 #
# @File : scheduleManager.py          #
# @Software: PyCharm  #
# =========================== #

from flask import current_app

import log


# 任务配置类
class SchedulerConfig(object):
    def __init__(self):
        log.debug('in SchedulerConfig init %s ' % current_app.name)
        self.app = current_app
        self.global_data = self.app.config['global_data']
        self.JOBS = [
            {
                'id': '东财预告定时抓取任务',  #
                'func': 'backend.schedule_task.sche_yubao:get_yubao',
                'args': [self.global_data],  # 执行程序参数
                'trigger': 'interval',  # 任务执行类型，定时器
                'minutes': 30  # 任务执行时间，单位秒
            },
            {
                'id': '每日收盘更新任务',  #
                'func': 'backend.schedule_task.sche_after_trade_daily:update_after_marketClose_daily',
                'args': [self.global_data],  # 执行程序参数
                'trigger': 'cron',
                'day_of_week': '0-4',  # 每周1至周5 16点执行
                'hour': 16,
                'minute': 1
            },
            {
                'id': '获取股东变化情况',  #
                'func': 'backend.schedule_task.sche_stock_holders:getShareHolder',  # 任务执行程序
                'args': [self.global_data],  # 执行程序参数
                'trigger': 'cron',
                'day_of_week': 'sat',  # 每周1至周516点执行
                'hour': 18,
                'minute': 2
            },
            {
                'id': '每日盘前更新任务',  #
                'func': 'backend.schedule_task.sche_before_trade_daily:update_before_marketOpen_daily',
                'args': [self.global_data],  # 执行程序参数
                'trigger': 'cron',
                'day_of_week': '0-4',  # 每周1至周5 16点执行
                'hour': 8,
                'minute': 30
            },
            {
                'id': 'test',  #
                'func': 'scheduleManager:test',
                # 'func': 'backend.schedule_task.sche_yubao:get_yubao',
                'args': [self.global_data],  # 执行程序参数
                'trigger': 'interval',  # 任务执行类型，定时器
                'seconds': 999999920  # 任务执行时间，单位秒
            }
        ]
    SCHEDULER_TIMEZONE = 'Asia/Shanghai'
    SCHEDULER_API_ENABLED = True


def test(global_data):
    log.debug("this is test")


