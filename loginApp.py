from flask import Flask, session, redirect, url_for, render_template, request
import hashlib
import sqlite3

def login():
    
    """Log in a registered user by adding the user id to the session."""
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        h = hashlib.md5()
        h.update(password.encode())
        password = h.hexdigest()

        conn = sqlite3.connect('database.db')
        c = conn.cursor()
        
        error = None
        user = c.execute(
            'SELECT * FROM users WHERE username = ?', (username,)
        ).fetchone()

        d = {}

        if user is not None:
            d = {'name':user[0],'username':user[1],'password':user[2]}

        if user is None:
            error = 'Incorrect username.'
        elif d['password'] !=  password:
            error = 'Incorrect password.'
        if error is None:
            # store the user id in a new session and return to the index
            session.clear()
            session['username'] = d['username']
            print([session['username']])
            return redirect(url_for('index'))

        return render_template("login.html",error=error)

    return render_template('login.html',error="")
