from flask import Flask, render_template, redirect, url_for, request
from flask_mysqldb import MySQL
import json
app = Flask(__name__)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'flask'
mysql = MySQL(app)

@app.route('/')
def hello_world():
    return 'Hello, World!'

# Route for handling the login page logic
@app.route('/add_user', methods=['GET', 'POST'])
def add_user():
    error = None
    values = request.get_json()
    if request.method == 'POST':
        if values['username'] != 'admin' or values['password'] != 'admin':
            cur = mysql.connection.cursor()
            username = values["username"]
            password = values["password"]
            cur.execute("INSERT INTO users(username, password) VALUES (%s, %s)", (username, password))
            mysql.connection.commit()
            cur.close()
            return "success"
        else:
            return 'Hello, World!'
    return render_template('add_user.html', error=error)

@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    return render_template('login_view.html', error=error)

@app.route('/validate_login/', methods=['GET', 'POST'])
def validate_login():
    print(request.get_json())
    values = request.get_json()
    if request.method == 'POST':
        if values['username'] != '' or values['password'] != '':
            return 'Invalid Credentials. Please try again.'
        else:
            return 'Hwew!'
    else:
            return 'Hello, World!'    

if __name__ == '__main__':
    app.run(debug=True, port=8080)