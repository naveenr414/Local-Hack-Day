from flask import Flask, session, redirect, url_for,render_template
import sqlite3

def club(clubname):
    con = sqlite3.connect("database.db")
    c = con.cursor()
    clubInfo = c.execute("SELECT * FROM clubs WHERE clubname=?",(clubname,)).fetchone()
    print(clubname,clubInfo)
    if(clubInfo):
        description = clubInfo[1]
        followers = c.execute("SELECT * FROM following WHERE user2=?",(clubname,))
        followers = [i[0] for i in followers]
        reviews = c.execute("SELECT * from reviews WHERE clubname=?",(clubname,))
        d = []
        for i in reviews:
            l = {}
            l["reviewer"] = i[0]
            l["time"] = i[2]
            l["review"] = i[1]
            d.append(l)
        return render_template("club.html",description=description,followers=followers,reviews=d,username=session["username"])
    else:
        return redirect(url_for("index"))

def clubList():
    con = sqlite3.connect("database.db")
    c = con.cursor()
    clubInfo = c.execute("SELECT * FROM clubs").fetchall()
    clubInfo = [i[0] for i in clubInfo]

    print(clubInfo)

    # return ""
    return render_template("clubList.html",clubInfo=clubInfo,username=session['username'])
