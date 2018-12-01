from flask import Flask, session,request, render_template, redirect, url_for
import sqlite3
from werkzeug.utils import secure_filename
import os
from datetime import datetime

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ['.png','.jpg','.jpeg','gif']

def write():
    if(request.method == 'POST'):
        conn = sqlite3.connect('database.db')
        c = conn.cursor()
        post = request.form['post']

        time = datetime.now().strftime("%B %d, %Y %I:%M%p")

        file = ""
        if('file' in request.files):
            f = request.files['file']
            if(allowed_file(f.filename)):
               file = f.filename
               f.save(os.path.join(app.config['UPLOAD_FOLDER'],secure_file(file)))
        
        username = session['username']
        c.execute('INSERT INTO posts(user1,posttext,time,image) VALUES(?,?)',(username,post,time,file,))
        conn.commit()
        return redirect(url_for('index'))

    if('username' in session):
        return render_template("write.html")
    else:
        return 'You must be logged in to write a post'
