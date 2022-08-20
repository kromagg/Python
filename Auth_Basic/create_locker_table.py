#!/usr/bin/python

import sqlite3

conn = sqlite3.connect('test.db')
print("Opened database successfully");

conn.execute('''CREATE TABLE LockerAssignment
         (

        locker_assignment_id INT PRIMARY KEY     NOT NULL,
        user_id INT  NOT NULL,
         locker_number     INT NOT NULL
        );''')
print("Table created successfully");

conn.close()