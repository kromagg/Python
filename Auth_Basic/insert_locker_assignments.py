#!/usr/bin/python

import sqlite3

conn = sqlite3.connect('test.db')
print("Opened database successfully");

conn.execute("INSERT INTO LockerAssignment (locker_assignment_id, user_id, locker_number) VALUES (343, 1, 71)");

conn.execute("INSERT INTO LockerAssignment (locker_assignment_id, user_id, locker_number) VALUES (344, 2, 92)");

conn.execute("INSERT INTO LockerAssignment (locker_assignment_id, user_id, locker_number) VALUES (345, 3, 93)");

conn.execute("INSERT INTO LockerAssignment (locker_assignment_id, user_id, locker_number) VALUES (346, 4, 84)");

conn.execute("INSERT INTO LockerAssignment (locker_assignment_id, user_id, locker_number) VALUES (347, 5, 15)");


conn.commit()
print("Records created successfully");
conn.close()