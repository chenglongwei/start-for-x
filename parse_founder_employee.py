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

data = json.loads(open('founders.json').read())

for line in data:
    startup_name = line['company']
    founders = line['founders']
    for founder in founders:
        cursor.execute('''INSERT INTO founder (founder_name, profile, photo, startup_name) VALUES (%s, %s, %s, %s)''',
                   (founder['name'], founder['profile'], founder['photos'], startup_name))
        conn.commit()


data = json.loads(open('employees.json').read())
for line in data:
    startup_name = line['company']
    members = line['members']
    for member in members:
        cursor.execute('''INSERT INTO employee (employee_name, profile, photo, startup_name) VALUES (%s, %s, %s, %s)''',
                   (member['name'], member['profile'], member['photos'], startup_name))
        conn.commit()


