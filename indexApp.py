from flask import Flask, session, render_template
import sqlite3

def index():
    if('username' in session):
        conn = sqlite3.connect('database.db')
        c = conn.cursor()

        following = c.execute('SELECT * FROM following WHERE user1 = ?',(session['username'],)).fetchall()
        following = [i[1].replace(" ","") for i in following]
        following.append(session['username'])

        ret = ""
        ret+="My name is "+str(session['username'])+"<br>"

        print("My following",following)

        allPosts = []

        for i in following:
            user = i
            posts = c.execute('SELECT * FROM posts WHERE user1 = ?',(user,)).fetchall()
            # posts = dict(posts)

            allPosts.append(posts)
            print(posts,user)
        
        print(ret)
        print(allPosts)
        return render_template('blog/index.html', allPosts = allPosts)

    else:
        return redirect(url_for('login'))
