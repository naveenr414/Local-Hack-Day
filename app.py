from flask import Flask
import loginApp

app = Flask(__name__)

@app.route('/')
def main():
    return "Main"

@app.route('/login')
def login():
    return loginApp.login()

app.run(host='127.0.5.1', port= 8081)
