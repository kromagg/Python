# Python 3 code to demonstrate the
# working of MD5 (string - hexadecimal)

import hashlib

# initializing string
str2hash = "password"

# hashed string using MD5 is 32 strings long, hex:
# 1234567890
# ----------
# 5f4dcc3b5a
# a765d61d83
# 27deb882cf
# 99

# encoding string using encode()
# then sending to md5()
result = hashlib.md5(str2hash.encode())

# printing the equivalent hexadecimal value.
print("The hexadecimal equivalent of hash is : ", end ="")
print(result.hexdigest())
