# =========================== #
# -*- coding: utf-8 -*-       #
# @Time : 22/2/21 19:58     #
# @Author : 毕磊              #
# @Site : ---                 #
# @File : stock_holder_reloader.mypy          #
# @Software: PyCharm  #
#
# =========================== #
import mypy.akshare_data.as_shareholder as sh

#重载指定个股的股东变动详情
def reload(param):
    code = param.get('code')
    if code is None:return
    sh.one_stock_holder_detail(code)

if __name__ == '__main__':
    quit(0)
