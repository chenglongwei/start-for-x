from flask import Flask, request, render_template
from flaskext.mysql import MySQL

mysql = MySQL()
app = Flask(__name__)

# MySQL configurations
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = ''
app.config['MYSQL_DATABASE_DB'] = 'start_for_x'

mysql.init_app(app)


@app.route('/')
def hello_world():
    return render_template('home.html')


@app.route('/api/create_startup', methods=['POST'])
def create_startup():
    return "OK"


@app.route('/api/finances/', methods=['GET'])
def get_finances():
    return "OK"


@app.route('/api/news/', methods=['GET'])
def get_news():
    return "OK"


@app.route('/api/workplace/', methods=['GET'])
def get_workplace():
    return "OK"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=9000)
