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
            if(allowed_file(f.filename)):
               file = f.filename.split(".")[0]+str(time).replace(" ","_")+"."+f.filename.split(".")[1]
               f.save(os.path.join(app.config['UPLOAD_FOLDER'],secure_filename(file)))
        
        username = session['username']
        c.execute('INSERT INTO posts(user1,posttext,time,image) VALUES(?,?,?,?)',(username,post,time,file,))
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
