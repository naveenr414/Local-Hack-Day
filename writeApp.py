from flask import Flask, session,request, render_template, redirect, url_for
import sqlite3
from werkzeug.utils import secure_filename
import os
from datetime import datetime

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ['png','jpg','jpeg','gif']

def write(app):
    if(request.method == 'POST'):
        conn = sqlite3.connect('database.db')
        c = conn.cursor()
        post = request.form['post']

        time = datetime.now().strftime("%B %d, %Y %I:%M%p")

        file = ""
        print(request.files)
        if('file' in request.files):
            f = request.files['file']
            file = f.filename.split(".")[0]+str(time).replace(" ","_")+"."+f.filename.split(".")[1]
            file = file.replace(":","_")
            print(file)
            filePath = os.path.dirname(os.path.abspath(__file__)).replace("\\","/")+url_for("static",filename="cronTab.png").replace("cronTab.png","")
            f.save(filePath+file)
            print(type(f))
        
        username = session['username']
        maxID = c.execute("SELECT MAX(id) FROM posts").fetchone()[0]
        if maxID == None:
            maxID=0
        c.execute('INSERT INTO posts(username,post,time,image,id) VALUES(?,?,?,?,?)',(username,post,time,file,maxID+1))
        conn.commit()
        return redirect(url_for('index'))

    if('username' in session):
        conn = sqlite3.connect("database.db")
        c = conn.cursor()
        able = c.execute('SELECT * FROM users WHERE username=?',(session['username'],)).fetchone()[3]
        if(able == "True"):
            return render_template("blog/write.html")
        else:
            return redirect(url_for("index"))
    else:
        return redirect(url_for("index"))
