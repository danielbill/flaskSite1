# =========================== #
# -*- coding: utf-8 -*-       #
# @Time : 22/2/4 11:23     #
# @Author : 毕磊              #
# @Site : ---                 #
# @File : flask_request_tool.mypy          #
# @Software: PyCharm  #
# flask获取参数方式：
#
# request.form.get("key", type=str, default=None) 获取表单数据
#
# request.args.get("key") 获取get请求参数
#
# request.values.get("key") 获取所有参数
#
# 作者：码农的happy_life
# 链接：https://www.jianshu.com/p/ecd97b1c21c1
# 来源：简书
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
# =========================== #
import log

#flask request 
def getRequestPostParam(request):
    params ={}
    if request.method == 'POST':
        keys = request.form.keys()
    for key in keys:
        params[key]=request.form.get(key)
    log.debug('post params is %s' %params)


if __name__ == '__main__':
    quit(0)
