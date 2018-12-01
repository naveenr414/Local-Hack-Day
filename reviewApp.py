from flask import Flask, session,request, render_template, redirect, url_for
import sqlite3
from datetime import datetime

def review(clubname):
    if(request.method == 'POST'):
        conn = sqlite3.connect('database.db')
        c = conn.cursor()
        review = request.form['review']

        time = datetime.now().strftime("%B %d, %Y %I:%M%p")
        
        username = session['username']
        c.execute('INSERT INTO reviews(username,review,time,clubname) VALUES(?,?,?,?)',(username,review,time,clubname))
        conn.commit()
        return redirect(url_for('index'))

    if('username' in session):
        conn = sqlite3.connect("database.db")
        c = conn.cursor()
        able = c.execute('SELECT * FROM users WHERE username=?',(session['username'],)).fetchone()[3]
        if(able == "False"):
            return render_template("blog/review.html",username=session["username"])
        else:
            return redirect(url_for("index"))
    else:
        return redirect(url_for("index"))

