from flask import Flask, session, redirect, url_for, render_template, request
import sqlite3

def follow():
    if request.method == 'POST':
        conn = sqlite3.connect("database.db")
        c = conn.cursor()
        username = session['username']
        following = c.execute("SELECT * FROM following where user1=?",(username,)).fetchall()
        following = [i[1] for i in following]
        
        newFollows = list(request.form.getlist('checkbox'))

        print(newFollows)
        print(following)

        for i in newFollows:
            if i not in following:
                c.execute('INSERT INTO following(user1,user2) VALUES(?,?)',(username,i))

                print("Inserting",i)

        for i in following:
            if i not in newFollows:
                c.execute("DELETE FROM following WHERE user1=? AND user2=?",(username,i))

        conn.commit()
        
        return redirect(url_for("index"))
    
    if('username' in session):
        username = session['username']
        conn = sqlite3.connect("database.db")
        c = conn.cursor()
        allUsers = c.execute('SELECT * FROM users').fetchall()
        allUsers = [i[1] for i in allUsers]
        following = c.execute("SELECT * FROM following where user1=?",(username,)).fetchall()
        following = [i[1].replace(" ","") for i in following]

        print("Currently following",following)
        print("All users",allUsers)
        print("Username",username)
        
        allUsers.remove(username)
        return render_template("follow.html",allUsers=allUsers,following=following)
    else:
        return "Need to login!"
