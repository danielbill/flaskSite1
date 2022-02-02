from flask import Flask, render_template
from flask_apscheduler import APScheduler

import py.db.mysql_db_manager as mydb
import router.blueprint_main as bp_main
from global_data import *
from scheduleManager import *

app = Flask(__name__)
app.config.from_pyfile('settings.py')

app.register_blueprint(bp_main.bp)
# handler = logging.FileHandler("site.log")
# app.logger.addHandler(handler)
# app.logger.setLevel(logging.DEBUG)
global_data = Site_global_data()
app.config['global_data'] = global_data

with app.app_context():
    app.config.from_object(SchedulerConfig())
    scheduler = APScheduler()  # 实例化 APScheduler
    scheduler.init_app(app)  # 把任务列表放入 flask
    scheduler.start()  # 启动任务列表


@app.route('/hello')
def hello():
    sql = " select * from em_yugao_plain"
    return render_template('yubao.html', data=mydb.queryToDataframe(sql))


@app.route('/')
def index():
    return render_template('/value/高增长.html')

@app.route('/api/data/highIncrease')
def highIncrease():
    json_data = {
        'code':0,
        'msg':'ok',
        'data':[]
    }
    sql = 'select * from yubao_value where netprofit_hb>15 and netprofit_tb>50'
    df = mydb.queryToDataframe(sql)
    data = df.to_json(orient = "records", force_ascii=False)
    json_data['count'] = len(df)
    json_data['data'] = data
    return data





