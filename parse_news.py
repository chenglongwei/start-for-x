from flask import Flask, json
from flaskext.mysql import MySQL

mysql = MySQL()
app = Flask(__name__)

# MySQL configurations
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = ''
app.config['MYSQL_DATABASE_DB'] = 'start_for_x'

mysql.init_app(app)

# Insert into table
conn = mysql.connect()
cursor = conn.cursor()

data = json.loads(open('news.json').read())

for line in data:
    startup_name = line['company']
    news = line['news']
    for new in news:
        try:
            cursor.execute('''INSERT INTO startup_news (link, title, startup_name) VALUES (%s, %s, %s)''',
                   (new['link'], new['title'], startup_name))
            conn.commit()
        except:
            print new['link']


