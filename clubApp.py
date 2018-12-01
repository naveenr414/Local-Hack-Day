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
        return render_template("club.html",description=description,followers=followers)
    else:
        return redirect(url_for("index"))