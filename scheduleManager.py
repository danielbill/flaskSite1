# =========================== #
# -*- coding: utf-8 -*-       #
# @Time : 22/1/25 20:33     #
# @Author : 毕磊              #
# @Site : ---                 #
# @File : scheduleManager.mypy          #
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
                'id': '东财业绩快报\财报定时抓取任务',  #
                'func': 'backend.schedule_task.sche_season_report:get_allreport',
                'args': [self.global_data],  # 执行程序参数
                'trigger': 'interval',  # 任务执行类型，定时器
                'hours': 1  # 任务执行时间
            },
            {
                'id': '东财预告定时抓取任务',  #
                'func': 'backend.schedule_task.sche_yubao:get_yubao',
                'args': [self.global_data],  # 执行程序参数
                'trigger': 'interval',  # 任务执行类型，定时器
                'minutes': 30  # 任务执行时间
            },
            {
                'id': '每日收盘更新任务',  #
                'func': 'backend.schedule_task.sche_after_trade_daily:update_after_marketClose_daily',
                'args': [self.global_data],  # 执行程序参数
                'trigger': 'cron',
                'day_of_week': '0-4',  # 每周1至周5 16点执行
                'hour': 17,
                'minute': 50
            },
            {
                'id': '获取股东变化情况',  #
                'func': 'backend.schedule_task.sche_stock_holders:getShareHolder',  # 任务执行程序
                'args': [self.global_data],  # 执行程序参数
                'trigger': 'cron',
                'day_of_week': 'mon-sun',  # 每周1至周7
                'hour': 19,
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
                'id': '每月底更新任务',  #
                'func': 'backend.schedule_task.sche_monthly_manager:run_monthly_task',
                'args': None,  # 执行程序参数
                'trigger': 'cron',
                'year': '*',
                'month': '*',
                'day': 'last',
                'hour':18,
                'minute':0
            },
            {
                'id': '交易日盘中更新任务',  #
                'func': 'backend.schedule_task.sche_during_trade_manager:on_trading_task',
                'args':  [self.global_data],
                'trigger': 'cron',
                'year': '*',
                'month': '*',
                'day_of_week': "mon-fri",  # 周一到周五
                "hour": "9-15",  # 9点到15点
                "minute": "29,59",
            },
            {
                'id': 'test',  #
                'func': 'scheduleManager:test',
                # 'func': 'backend.schedule_task.sche_yubao:get_yubao',
                'args': [self.global_data],  # 执行程序参数
                'trigger': 'interval',  # 任务执行类型，定时器
                'seconds': 9999999920  # 任务执行时间，单位秒
            }
        ]
    SCHEDULER_TIMEZONE = 'Asia/Shanghai'
    SCHEDULER_API_ENABLED = True


def test(global_data):
    log.debug("this is test")


