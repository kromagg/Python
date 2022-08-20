#!/usr/bin/python

import sqlite3

conn = sqlite3.connect('test.db')
print("Opened database successfully");

conn.execute("DELETE FROM LockerAssignment");

conn.execute("DELETE FROM User");

conn.commit()
print("Records created successfully");
conn.close()