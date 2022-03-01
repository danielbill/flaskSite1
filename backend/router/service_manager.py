# =========================== #
# -*- coding: utf-8 -*-       #
# @Time : 22/2/22 20:26     #
# @Author : 毕磊              #
# @Site : ---                 #
# @File : service_manager.mypy          #
# @Software: PyCharm  #
#
# =========================== #
import mypy.biz.mystock.my_stock_service as mss
import global_data as gd
#ajax调用的服务配置
SVC_CONF ={
    'mystock.add':{
        'param':['code'],
        'svc':lambda code: mss.add_stock(code),
        'reload':'my_stock'
    },
    'mystock.del':{
        'param':['code'],
        'svc':lambda code: mss.del_stock(code),
        'reload':'my_stock'
    }
}
def do_service(svc_id,param):
    svcc = SVC_CONF.get(svc_id)
    if svcc is None : return
    param_key = svcc.get('param')
    svc_params = {}
    for key in param_key:
        svc_params[key]=param.get(key)
    svc = svcc.get('svc')
    data =  svc(**svc_params)
    reload = svcc.get('reload')
    if reload is not None:
        gd.SGD.reload(type=reload)
    return data




if __name__ == '__main__':
    do_service('mystock.del',{'code':'000960'})
