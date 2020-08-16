# -*- coding: utf-8 -*-
"""
Created on Sat Aug 15 15:13:29 2020

@author: ryanf
"""
import sqlite3 

def create_connection(db_file):
    conn = None 
    try:
        conn =sqlite3.connect(db_file)
        return conn
    except Exception as e:
        print(e)
    return conn

def create_table(conn, create_table):
    try:
        c= conn.cursor()
        c.execute(create_table)
    except Exception as e:
        print(e)
        
def main():
    database = r"C:\sqlite\db\user.db"
    
    usersTable = """ CREATE TABLE IF NOT EXISTS users (
    profileID integer PRIMARY KEY,
    fullName text NOT NULL,
    campus text NOT NULL, 
    year text NOT NULL,
    major text NOT NULL,
    clubs text,
    canHelp blob, 
    needHelp blob,
    interests text
    FOREIGN KEY (clubs) REFERENCES studentClubsTable (clubName)
    FOREIGN KEY (canHelp) REFERENCES studentTutorTable (canHelp)
    FOREIGN KEY (needHelp) REFERENCES studentTutor2Table (needHelp)
    FOREIGN KEY (interests) REFERENECES userInterestTable (interests)
    ); """
    
    studentClubsTable = """CREATE TABLE IF NOT EXISTS studentClubs(
    profileID integer NOT NULL,
    clubName text PRIMARY KEY
    );"""
    
    studentTutorTable = """ CREATE TABLE IF NOT EXISTS studentCanHelp(
    profileID integer NOT NULL,
    canHelp text PRIMARY KEY
    );"""
    
    studentTutor2Table = """CREATE TABLE IF NOT EXISTS studentNeedHelp(
    profileID integer NOT NULL,
    needHelp text PRIMARY KEY
    );"""
    
    userInterestTable = """CREATE TABLE IF NOT EXISTS userInterestTable(
    profileID integer NOT NULL,
    interests text PRIMARY KEY
    );"""
    
    conn = create_connection(database)
    
    if conn is not None:
        create_table(conn, usersTable)
        create_table(conn, studentClubsTable)
        create_table(conn, studentTutorTable)
        create_table(conn, studentTutor2Table)
        create_table(conn, userInterestTable)
    else:
        print("error: cannot establish connection")
    if __name__ == '__main__':
        main()