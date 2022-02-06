from flask import Flask
from flask_apscheduler import APScheduler

import router.bp_ajax_api as ajax_api
import router.bp_martket as bp_market
import router.bp_trend as bp_trend
from global_data import *
from scheduleManager import *

app = Flask(__name__)
#配置参数
app.config.from_pyfile('settings.py')

#设置站点级全局变量
global_data = Site_global_data()
app.config['global_data'] = global_data

#增加router
app.register_blueprint(bp_market.bp)
app.register_blueprint(bp_trend.bp)
app.register_blueprint(ajax_api.bp)

#配置定时任务
with app.app_context():
    app.config.from_object(SchedulerConfig())
    scheduler = APScheduler()  # 实例化 APScheduler
    scheduler.init_app(app)  # 把任务列表放入 flask
    scheduler.start()  # 启动任务列表

# @app.route('/')
# def index():
#     return render_template('/index1.html')




