# =========================== #
# -*- coding: utf-8 -*-       #
# @Time : 22/2/1 22:13     #
# @Author : 毕磊              #
# @Site : ---                 #
# @File : global_data.mypy          #
# @Software: PyCharm  #
#
# =========================== #

from datetime import date

import mypy.db.dao.common_data_access as common_data
import mypy.biz.mystock.my_stock_service as mss


class Site_global_data():
    def __init__(self):
        self.trade_day = common_data.get_trade_day_thisyear()
        self.my_stock = mss.get_mystocks()
        self.params ={
            'yb_s2':None
        }
        self._init_params()

    def is_trade_day(self, day: date = None) -> bool:
        # log.debug(type(day))
        if day == None: day = date.today()
        day = day.strftime('%Y-%m-%d')
        # log.debug(day)
        return day in self.trade_day['trade_day'].values

    def _reload_trade_day(self):
        self.trade_day = common_data.get_trade_day_thisyear()

    def _reload_my_stock(self):
        self.my_stock=mss.get_mystocks()

    def get_mystock(self):
        return self.my_stock

    def _init_params(self):
        for key in self.params.keys():
            self.params[key] = common_data.get_global_data(key)

    def reload_param(self,paramKey):
        self.params[paramKey] = common_data.get_global_data(paramKey)

    def getParam(self,paramKey):
        return self.params.get(paramKey)

    def reload(self,type):
        # print(f'reload is {type}')
        reloads  ={
            'trade_day': self._reload_trade_day(),
            'my_stock': self._reload_my_stock()
        }
        return reloads.get(type,None)

SGD = Site_global_data()

if __name__ == '__main__':
    df  = SGD.get_mystock()
    row = df[df.code=='600362']
    print(row)
    print(row['grp'].values[0])
