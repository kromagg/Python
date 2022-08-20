#!/usr/bin/python

import sqlite3

conn = sqlite3.connect('test.db')
print("Opened database successfully");

cursor = conn.execute("SELECT locker_assignment_id, user_id, locker_number FROM LockerAssignment;")
for row in cursor:
    print("Id:", row[0], ", user_id:", row[1], ", locker_number:", row[2])

print("Operation done successfully");
conn.close()