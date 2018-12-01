from flask import Flask, session, redirect, url_for
import sqlite3

def club(clubname):
    con = sqlite3.connect("database.db")
    c = con.cursor()
    clubInfo = c.execute("SELECT * FROM clubs WHERE clubname=?",(clubname,)).fetchone()
    if(clubInfo):
        return clubInfo[1]
    else:
        return redirect(url_for("index"))
