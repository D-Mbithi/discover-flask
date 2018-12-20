from flask import Flask, render_template, redirect, url_for, request
app = Flask(__name__)


# funtion route for home page
@app.route('/')
def home():
    return render_template('index.html')


# Fountion route for welcome page
@app.route('/welcome')
def welcome():
    return render_template("welcome.html")


# Function page for login page
@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != 'admin' or \
                request.form['password'] != 'admin':
                    error = 'Invalid login cridentials, please try again'
        else:
            return redirect(url_for('home'))
    return render_template('login.html', error=error)


if __name__ == "__manin__":
    app.run(debug=True)
