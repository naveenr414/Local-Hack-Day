from flask import Flask, session, redirect, url_for, request, render_template,session
import sqlite3

def editclub():
    if(request.method == 'POST'):
        conn = sqlite3.connect('database.db')
        c = conn.cursor()
        description = request.form['description']
        c.execute("UPDATE clubs SET description=? where clubname=?",(description,session['username'],))
        conn.commit()
        return redirect(url_for("index"))

    if('username' in session):
        conn = sqlite3.connect("database.db")
        c = conn.cursor()
        able = c.execute('SELECT * FROM users WHERE username=?',(session['username'],)).fetchone()[3]
        if(able == "True"):
            description = c.execute('SELECT * FROM clubs where clubname=?',(session['username'],)).fetchone()
            
            if(description):
                description = description[1]
            else:
                description = ""

            print(description)
            
            return render_template("edit.html",description=description)

    return redirect(url_for("index"))
