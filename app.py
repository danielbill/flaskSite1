from flask import Flask
from flask import request



app = Flask(__name__)


@app.route('/hello')
def hello_world():
    return 'Hello1 World!'

@app.route('/index')
def index():
    user_agent = request.headers.get('User-Agent')
    return '<p>Your browser is %s</p>' % user_agent

if __name__ == '__main__':
    app.run()
