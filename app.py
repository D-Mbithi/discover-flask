from flask import (
        Flask, render_template, redirect, url_for, request, session, flash
        )
from functools import wraps


# create the application and set some configurations
app = Flask(__name__)
app.secret_key = 'klasndlnqenio32ea/dmmkawd2nqeks[[qeslkwqelk'


# login required decorator
def login_required(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        if 'logged_in' in session:
            return f(*args, **kwargs)
        else:
            flash('You need to log in')
            return redirect(url_for('login'))
    return wrap

# funtion route for home page
@app.route('/')
@login_required
def home():
    return render_template('index.html')


# Fountion route for welcome page
@app.route('/welcome')
def welcome():
    return render_template("welcome.html")


# login page routing
@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != 'admin' or \
                request.form['password'] != 'admin':
                    error = 'Invalid login cridentials, please try again'
        else:
            session['logged_in'] = True
            flash('you have been loggen in!')
            return redirect(url_for('home'))
    return render_template('login.html', error=error)


# Logout page routing
@app.route('/logout')
@login_required
def logout():
    session.pop('logged_in', None)
    flash('you have been loggen out!')
    return redirect(url_for('welcome'))


if __name__ == "__manin__":
    app.run(debug=True)
