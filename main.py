import config
from flask import render_template, redirect, url_for, request, session
app = config.app
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
    return render_template('main_view.html', error=error)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if 'username' not in session:  
        error = None
        return render_template('login_view2.html', error=error)
    else:
        return redirect(url_for('add_user'))

@app.route('/validate_login/', methods=['GET', 'POST'])
def validate_login():
    print(request.get_json())
    values = request.get_json()
    if request.method == 'POST':
        if values['username'] == 'admin' or values['password'] == 'admin':
            session['username']=values['username'] 
            return 'success'
        else:
            return 'Hwew!'
    else:
            return 'Hello, World!'    

@app.route('/users', methods=['GET', 'POST'])
def users():
    users = imports.users.Users()
    return users.sample()

@app.route('/logout', methods=['GET', 'POST'])
def logout():
    if 'username' in session:  
        session.pop('username',None)  
        return redirect(url_for('login'))
    else:
        return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True, port=8080)