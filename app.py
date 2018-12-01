from flask import Flask, session, redirect, url_for
import loginApp
import indexApp
import writeApp

app = Flask(__name__)
app.secret_key = 'super secret key'
app.config['SESSION_TYPE'] = 'filesystem'

@app.route('/')
def index():
    return indexApp.index()

@app.route('/login', methods=['GET', 'POST'])
def login():
    return loginApp.login()

@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('index'))

@app.route('/write',methods=['GET', 'POST'])
def write():
    return writeApp.write()

app.run(host='127.0.5.1', port= 8081)
