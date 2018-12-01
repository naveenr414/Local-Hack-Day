from flask import Flask, session,request, render_template, redirect, url_for
import sqlite3


def write():

    if(request.method == 'POST'):
        conn = sqlite3.connect('database.db')
        c = conn.cursor()
        post = request.form['post']
        username = session['username']
        c.execute('INSERT INTO posts(user1,posttext) VALUES(?,?)',(username,post,))
        conn.commit()
        return redirect(url_for('index'))

    if('username' in session):
        return render_template("write.html")
    else:
        return 'You must be logged in to write a post'
