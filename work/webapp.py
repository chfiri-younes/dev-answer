from flask import Flask, render_template, g, session, request, redirect, url_for

import os

app = Flask(__name__)

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

@app.route('/register')
def register():
    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != 'admin' or request.form['password'] != 'admin':
            error = 'Invalid Username of Password. Please try again.'
        else:
            return redirect(url_for('accueil'))
    return render_template('_login.html', error=error)

if __name__ == '__main__':
    app.run(debug=True)