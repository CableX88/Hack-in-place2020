# -*- coding: utf-8 -*-
"""
Created on Sat Aug 15 18:28:30 2020

@author: ryanf
"""
import sqlite3 as sql
from flask import Flask
from flask import render_template 
from flask import request
import models as dbHandler 

usersTable = """ CREATE TABLE IF NOT EXISTS login (
     profileID integer PRIMARY KEY AUTOINCREMENT,
     email text NOT NULL,
     password text NOT NULL, 
     ); """
def insertUsername(username, password):
 con = sql.connect("database.db")
 cur = con.cursor()
 cur.execute("INSERT INTO usersTable (username, password) VALUES (?,?)", (username, password))
 con.commit()
 con.close()
 
def retrieveUsers():
 con = sql.connect("database.db")   
 cur = con.cursor()
 cur.execute("SELECT username, password FROM users")
 users = cur.fetchall()
 con.close()
 return users

app = Flask(__name__)
@app.route('/', methods = ['POST', 'GET'])
def home():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        dbHandler.insertUser(username, password)
        users = dbHandler.retrieveUsers()
        return render_template('test.html')
    else:
        return render_template('test.html')
if __name__ == 'main':
    app.run(debug = False, host='0.0.0.0')

