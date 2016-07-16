from flask import Flask, request, render_template, Response, json
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
    return render_template('home.html', message="Hello World")


@app.route('/api/create_startup', methods=['POST'])
def create_startup():
    if request.method == 'POST':
        data = request.get_json()
        # print data
        print data

        # Insert into table
        conn = mysql.connect()
        cursor = conn.cursor()

        for tag in data['tags']:
            cursor.execute('''INSERT INTO startup_tag (startup_name, tag) VALUES (%s, %s)''', (data['startup_name'], tag))
            conn.commit()

        js = json.dumps({'status': 'OK'})
        resp = Response(js, status=200, mimetype="application/jsonp")
        resp.headers.add('Access-Control-Allow-Origin', '*')
        return resp


@app.route('/api/finances/<name>', methods=['GET'])
def get_finances(name):
    print name
    return "OK"


@app.route('/api/news/<name>', methods=['GET'])
def get_news(name):
    return "OK"


@app.route('/api/workplace/<name>', methods=['GET'])
def get_workplace(name):
    return "OK"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=9000)
