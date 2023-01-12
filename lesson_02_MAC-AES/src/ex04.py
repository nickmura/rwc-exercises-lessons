import hashlib
import secrets
import hmac

# my and key as per question
my = secrets.token_hex(64)
key = secrets.token_hex(16)

# encoding as per other answers
byte_key = bytes(key, 'UTF-8')  # key.encode() would also work in this case
message = my.encode()

# now use the hmac.new function and the hexdigest method
h = hmac.new(byte_key, message, hashlib.sha256).hexdigest()

# print the output
print(h)
print(message)