# =========================== #
# -*- coding: utf-8 -*-       #
# @Time : 22/2/1 22:13     #
# @Author : 毕磊              #
# @Site : ---                 #
# @File : global_data.py          #
# @Software: PyCharm  #
#
# =========================== #

from datetime import date

import py.db.dao.common_data_access as common_data


class Site_global_data():
    def __init__(self):
        self.trade_day = common_data.get_trade_day_thisyear()

    def is_trade_day(self, day: date = None) -> bool:
        # log.debug(type(day))
        if day == None: day = date.today()
        day = day.strftime('%Y-%m-%d')
        # log.debug(day)
        return day in self.trade_day['trade_day'].values


if __name__ == '__main__':
    global_data = Site_global_data()
    today = date(2022, 2, 9)
    print(today)
    print(global_data.is_trade_day(today))
