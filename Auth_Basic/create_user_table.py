#!/usr/bin/python

import sqlite3

conn = sqlite3.connect('test.db')
print("Opened database successfully");

conn.execute('''CREATE TABLE User
         (user_id INT PRIMARY KEY     NOT NULL,
         user_name           VARCHAR(128)    NOT NULL,
         user_password            VARCHAR(128)     NOT NULL,
         account_status     INT NOT NULL,
         failed_login_attempts INT,
         created_date        DATETIME NOT NULL,
         locked_out_date    DATETIME);''')
print("Table created successfully");

conn.close()