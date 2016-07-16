from flask import Flask, request, render_template, Response, json
from flaskext.mysql import MySQL
import recommendation
import os

APP_ROOT = os.path.dirname(os.path.abspath(__file__))
DATA_FOLDER = os.path.join(APP_ROOT, 'recommend_data/')

mysql = MySQL()
app = Flask(__name__)

# MySQL configurations
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = ''
app.config['MYSQL_DATABASE_DB'] = 'start_for_x'

app.config['UPLOAD_FOLDER'] = DATA_FOLDER

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
            cursor.execute('''INSERT INTO startup_tag (startup_name, tag) VALUES (%s, %s)''',
                           (data['startup_name'], tag))
            conn.commit()

        js = json.dumps({'status': 'OK'})
        resp = Response(js, status=200, mimetype="application/jsonp")
        resp.headers.add('Access-Control-Allow-Origin', '*')
        return resp


@app.route('/api/finances/<name>', methods=['GET'])
def get_finances(name):
    if request.method == 'GET':
        tags = get_company_tags(name)
        companies = recommendation.Recommendation().get_recommendations(DATA_FOLDER, tags)

        conn = mysql.connect()
        cursor = conn.cursor()

        res = []
        for company in companies:
            # Get evaluation
            cursor.execute('''SELECT current_valuation FROM startup_evaluation WHERE startup_name = %s''', (company,))
            conn.commit()
            # evaluations is a tuple of tuple
            evaluations = cursor.fetchall()
            evaluation = ""
            if evaluations is not None and len(evaluations) != 0:
                evaluation = evaluations[0][0]

            # Get fundings
            cursor.execute('''SELECT funding_date, event, amount_raised, investors FROM startup_funding
                              WHERE startup_name = %s''', (company,))
            conn.commit()
            fundings = cursor.fetchall()
            # Parse fundings data
            funding_list = []
            for funding in fundings:
                funding_list.append({'funding_date': funding[0], 'event': funding[1], 'amount_raised': funding[2],
                                     'investors': funding[3].split(',')})

            sub_res = {company: funding_list, 'current_valuation': evaluation}
            res.append(sub_res)

        js = json.dumps(res)
        print js
        resp = Response(js, status=200, mimetype="application/jsonp")
        resp.headers.add('Access-Control-Allow-Origin', '*')
        return resp


@app.route('/api/news/<name>', methods=['GET'])
def get_news(name):
    if request.method == 'GET':
        tags = get_company_tags(name)
        companies = recommendation.Recommendation().get_recommendations(DATA_FOLDER, tags)

        conn = mysql.connect()
        cursor = conn.cursor()

        res = []
        for company in companies:
            cursor.execute('''SELECT link FROM startup_news WHERE startup_name = %s''', (company,))
            conn.commit()
            links = cursor.fetchall()

            # convert list of tuples to list of strings
            link_list = []
            for link in links:
                link_list.append(link[0])

            sub_res = {company: link_list}
            res.append(sub_res)

        js = json.dumps(res)
        print js
        resp = Response(js, status=200, mimetype="application/jsonp")
        resp.headers.add('Access-Control-Allow-Origin', '*')
        return resp


@app.route('/api/workplace/<name>', methods=['GET'])
def get_workplace(name):
    if request.method == 'GET':
        tags = get_company_tags(name)
        companies = recommendation.Recommendation().get_recommendations(DATA_FOLDER, tags)

        conn = mysql.connect()
        cursor = conn.cursor()

        res = []
        for company in companies:
            cursor.execute('''SELECT founder_name, profile, photo FROM founder WHERE startup_name = %s''',
                           (company,))
            conn.commit()
            founders = cursor.fetchall()

            cursor.execute('''SELECT employee_name, profile, photo FROM employee WHERE startup_name = %s''',
                           (company,))
            conn.commit()
            employees = cursor.fetchall()

            # convert data
            employee_list = []
            for founder in founders:
                employee_list.append({'name': founder[0], 'profile': founder[1], 'photo': founder[2]})

            for employee in employees:
                employee_list.append({'name': employee[0], 'profile': employee[1], 'photo': employee[2]})

            sub_res = {company: employee_list}
            res.append(sub_res)

        js = json.dumps(res)
        print js
        resp = Response(js, status=200, mimetype="application/jsonp")
        resp.headers.add('Access-Control-Allow-Origin', '*')
        return resp


def get_company_tags(startup_name):
    return ["University Students", "Mobile", "Recruting", "Educational Games", "Big Data"]
    # conn = mysql.connect()
    # cursor = conn.cursor()
    # cursor.execute('''SELECT tag FROM startup_tag WHERE startup_name = %s''', (startup_name,))
    # conn.commit()
    #
    # tags = cursor.fetchall()
    #
    # return tags


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=9000)
