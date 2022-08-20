#!/usr/bin/python

import sqlite3

conn = sqlite3.connect('test.db')
print("Opened database successfully");

cursor = conn.execute("SELECT user_id, user_name, user_password, user_password_md5, account_status, failed_login_attempts, created_date, locked_out_date FROM USER;")
for row in cursor:
    print("Id:", row[0], ", U:", row[1], ", P:", row[2], "PMD5:", row[3], ", status:", row[4], ", fail:", row[5], ", created:", row[6], ", locked:", row[7])

print("Operation done successfully");
conn.close()