#!/usr/bin/python

import sqlite3

username = ''
password = ''

print('Enter your name: ', end="")
username = input()

print('Enter your password: ', end="")
password = input()

conn = sqlite3.connect('test.db')

cursor = conn.execute("SELECT user_id, user_name, user_password, account_status, failed_login_attempts, created_date, locked_out_date FROM [User] WHERE user_name = \'" + username + "\'")

user_found = False

for row in cursor:
    user_found = True

    if (password == str(row[2])):
        # match
        print("Credential matches")

        # -1 = disabled, 0 = locked out, 1 = active 
        if (row[3] == -1):
            print("User's account is disabled")
        elif (row[3] == 0):
            print("User's account is locked out, since " + str(row[6]))
        elif (row[3] == 1):
            print("User may proceed")

    else:
        # incorrect password
        print("Incorrect password")

if not user_found:
    print("User was not found")



conn.close()



