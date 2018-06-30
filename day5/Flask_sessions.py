

from flask import Flask, session, redirect, url_for, render_template, request

import os

app = Flask (__name__)

app.secret_key = os.urandom(24)

@app.route('/')
def index ():
    if request.method == "POST":
        session.pop("user", None)

        if request.form['password'] == ['password']:
            session['user'] == request.form ['username']
            return redirect (url_for('register.html'))
    return render_template ('login.html')

@app.route ('/login', methods = ["GET", "POST"])
def login():
     return render_template ('login.html')

@app.route('/register')
def register ():
    return render_template ('register.html')

@app.route('/comments')
def comments ():
    return render_template ('login.html')

app.route('/logout')
def logout ():
    return render_template ('login.html')

    if __name__=='__main__':
        app.run (debug = True)
