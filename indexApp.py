from flask import Flask, session
import sqlite3

def index():
    if('username' in session):
        conn = sqlite3.connect('database.db')
        c = conn.cursor()

        following = c.execute('SELECT * FROM following WHERE user1 = ?',(session['username'],)).fetchall()

        ret = ""
        for i in following:
            user = i[1]
            posts = c.execute('SELECT * FROM posts WHERE user1 = ?',(user,)).fetchall()
            for post in posts:
                ret+=str(user)+ " wrote "+str(post[1])
                ret+="<br>"
        
        return ret
    else:
        return "Main"