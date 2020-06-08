from flask import Flask, render_template, g, session, request, redirect, url_for, flash
#from data import Article
from flask_sqlalchemy import SQLAlchemy
from passlib.hash import sha256_crypt
app = Flask(__name__)

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql://sql7346420:PYDlIdzWtEm@sql7.freemysqlhosting.net/sql7346420"
db = SQLAlchemy(app)  


@app.route('/')
def accueil():
    return render_template('accueil.html')
 
@app.route('/about')
def about ():
    return render_template('about.html')

@app.route('/support')
def support ():
    return render_template('support.html')

@app.route('/rules')
def rules ():
    return render_template('rules.html')

@app.route('/profile')
def profilel():
    return render_template('profile.html')

@app.route('/register', methods=["GET","POST"])
def register():
    if request.method == "POST":
        username = request.form.get("username")
        email = request.form.get("email")
        password = request.form.get("password")
        confirm = request.form.get("confirm")
        secure_password = sha256_crypt.encrypt(str(password))

        if password == confirm:
            db.execute("INSTERT INTO users(username, email, passord) VALUE(:username,:email,:password)",
                                            {"username":username,"email":email,"password":secure_password})
            db.commit()
            return redirect(url_for('login'))
        else:
            return render_template('register.html')

    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != 'admin' or request.form['password'] != 'admin':
            error = 'Invalid Username or Password. Please try again.'
        else:
            return redirect(url_for('accueil'))
    return render_template('_login.html', error=error)

if __name__ == '__main__':
    app.run(debug=True)