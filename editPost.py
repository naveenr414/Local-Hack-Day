from flask import Flask, session, redirect, url_for, request, render_template
import sqlite3
from datetime import datetime

def delete(postnum):
    conn = sqlite3.connect("database.db")
    c = conn.cursor()
    c.execute("DELETE FROM posts where id=?",(postnum, ))
    conn.commit()
    return redirect(url_for("index"))

def update(postnum):
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
           f.save(os.path.join(app.config['UPLOAD_FOLDER'],secure_filename(file)))
        
        username = session['username']
        c.execute('UPDATE posts set post=?, time=?, image=?  WHERE id=?',(post,time,file,postnum))
        conn.commit()
        return redirect(url_for('index'))

    if('username' in session):
        conn = sqlite3.connect("database.db")
        c = conn.cursor()
        able = c.execute('SELECT * FROM users WHERE username=?',(session['username'],)).fetchone()[3]
        if(able == "True"):
            currentPost = c.execute("SELECT * FROM posts where id=?", (postnum)).fetchone()[1]
            print(currentPost)
            return render_template("blog/update.html",post=currentPost)
        else:
            return redirect(url_for("index"))
    else:
        return redirect(url_for("index"))
