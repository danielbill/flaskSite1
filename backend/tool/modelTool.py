# =========================== #
# -*- coding: utf-8 -*-       #
# @Time : 22/2/12 14:22     #
# @Author : 毕磊              #
# @Site : ---                 #
# @File : modelTool.py          #
# @Software: PyCharm  #
# 将数据层转化为视图层的工具
# =========================== #
import py.tools.dataFrameTool as dfTool

#将后台数据库df转义成layui的数据表所需的对象
def df_to_layui_table_data(df)->dict:
    data = {
        'code': 0,
        'msg': 'ok',
        'data': []
    }
    # 转为record,但不是json
    json_like_dict = dfTool.df_to_records(df)
    data['count'] = len(df)
    data['data'] = json_like_dict
    return data

#将后台数据库df转义成w2ui的数据表所需的对象
def df_to_w2ui_table_data(df)->dict:
    data = {
        'total': 0,
        'status': 'success',
        'records': []
    }
    # 转为record,但不是json
    json_like_dict = dfTool.df_to_records_with_index(df,'recid')
    data['total'] = len(df)
    data['records'] = json_like_dict
    return data

#ajax传输时,无法转换na和null,导致加载失败
def fill_Na_and_Null(df):
    if df.empty : return
    return df.fillna(0)


if __name__ == '__main__':
    quit(0)
