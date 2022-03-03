from flask import Flask ,render_template
app = Flask(__name__)

from backend.router import bp_query,bp_selection,bp_dazong,bp_trend,bp_martket,bp_ajax_api,bp_common
#增加router
app.register_blueprint(bp_query.bp)
app.register_blueprint(bp_martket.bp)
app.register_blueprint(bp_trend.bp)
app.register_blueprint(bp_ajax_api.bp)
app.register_blueprint(bp_dazong.bp)
app.register_blueprint(bp_selection.bp)
app.register_blueprint(bp_common.bp)

from global_data import *
#设置站点级全局变量
#配置参数
app.config.from_pyfile('settings.py')
app.config['global_data'] = SGD
import mypy.choice.choice_strategy as cho_stgy
app.config['CHOICE_STRATEGY'] = cho_stgy.CHOICE_STRATEGY



from flask_apscheduler import APScheduler
from scheduleManager import *
#配置定时任务
with app.app_context():
    app.config.from_object(SchedulerConfig())
    scheduler = APScheduler()  # 实例化 APScheduler
    scheduler.init_app(app)  # 把任务列表放入 flask
    scheduler.start()  # 启动任务列表

@app.route('/')
def index():
    return render_template('/home_iframe.html')

@app.route('/test')
def test():
    return render_template('base/test.html')

@app.route('/<dir>/<page>')
def page(dir,page):
    return render_template(f'{dir}/{page}.html')


if __name__ == '__main__':
    app.run()

