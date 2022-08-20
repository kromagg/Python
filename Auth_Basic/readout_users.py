#!/usr/bin/python

import sqlite3

conn = sqlite3.connect('test.db')
print("Opened database successfully");

cursor = conn.execute("SELECT user_id, user_name, user_password, account_status, failed_login_attempts, created_date, locked_out_date FROM USER;")
for row in cursor:
    print("ID:", row[0], ", U:", row[1], ", P:", row[2], ", status:", row[3], ", fail:", row[4], ", created:", row[5], ", locked:", row[6])

print("Operation done successfully");
conn.close()