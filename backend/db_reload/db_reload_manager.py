# =========================== #
# -*- coding: utf-8 -*-       #
# @Time : 22/2/21 19:57     #
# @Author : 毕磊              #
# @Site : ---                 #
# @File : db_reload_manager.mypy          #
# @Software: PyCharm  #
#
# =========================== #
import backend.db_reload.stock_holder_reloader as hr

DB_RELOAD_CONF ={
    'stock.company_detail':hr
}

def reload_db(reload_id,param):
    reloader = DB_RELOAD_CONF.get(reload_id)
    if reloader is None : return
    reloader.reload(param)


if __name__ == '__main__':
    quit(0)
