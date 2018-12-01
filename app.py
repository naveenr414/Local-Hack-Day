from flask import Flask
import loginApp

app = Flask(__name__)

@app.route('/hello')
def helloIndex():
    return 'Hello World from Python Flask!'

@app.route('/login')
def login():
    return loginApp.login()

@app.route('/fakelogin')
def fakeLogin()

app.run(host='127.0.5.1', port= 8081)
