from flask import Flask, session, redirect, url_for
import loginApp, indexApp, writeApp, followApp

app = Flask(__name__)
app.secret_key = 'super secret key'
app.config['SESSION_TYPE'] = 'filesystem'
app.config['UPLOAD_FOLDER'] = 'uploads'

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
    return writeApp.write(app)

@app.route('/follow',methods=['GET','POST'])
def follow():
    return followApp.follow()

app.run(host='127.0.5.1', port= 8081)
