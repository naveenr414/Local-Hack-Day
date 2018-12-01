from flask import Flask, session, redirect, url_for, g
import loginApp, indexApp, writeApp, followApp, clubApp, editApp, reviewApp, editPost

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

@app.route('/clubs/<clubname>')
def club(clubname):
    return clubApp.club(clubname)

@app.route('/editclub',methods=['GET','POST'])
def editclub():
    return editApp.editclub()

@app.route('/clubs/<clubname>/review',methods=['GET','POST'])
def review(clubname):
    return reviewApp.review(clubname)

@app.route('/delete/<postnum>')
def delete(postnum):
    return editPost.delete(postnum)

@app.route('/update/<postnum>', methods=['GET', 'POST'])
def update(postnum):
    return editPost.update(postnum)

app.run(host='127.0.5.1', port= 8081)
