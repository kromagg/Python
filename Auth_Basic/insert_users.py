#!/usr/bin/python

import sqlite3

conn = sqlite3.connect('test.db')
print("Opened database successfully");

conn.execute("INSERT INTO USER (user_id, user_name, user_password, account_status, failed_login_attempts, created_date, locked_out_date)  \
    VALUES (1, 'lcustodio', 'migraine12345', 1, 0, '2022.01.01 00:00:01', null)");

conn.execute("INSERT INTO USER (user_id, user_name, user_password, account_status, failed_login_attempts, created_date, locked_out_date)  \
    VALUES (2, 'hcustodio', 'gym123', 1, 0, '2022.02.01 00:00:02', null)");

conn.execute("INSERT INTO USER (user_id, user_name, user_password, account_status, failed_login_attempts, created_date, locked_out_date)  \
    VALUES (3, 'tcustodio', 'willy123', 1, 0, '2022.03.01 00:00:03', null)");

conn.execute("INSERT INTO USER (user_id, user_name, user_password, account_status, failed_login_attempts, created_date, locked_out_date)  \
    VALUES (4, 'jfart', 'abc123', -1, 0, '2022.03.01 00:00:03', null)");

conn.execute("INSERT INTO USER (user_id, user_name, user_password, account_status, failed_login_attempts, created_date, locked_out_date)  \
    VALUES (5, 'kfart', 'abc123', 0, 3, '2022.03.01 00:00:03', '2021.12.31 23:00:03')");


conn.commit()
print("Records created successfully");
conn.close()