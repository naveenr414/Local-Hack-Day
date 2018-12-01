from flask import Flask, session

def login():
    if('username' in session):
        return "Logged in"
    else:
        return "Not Logged in"
