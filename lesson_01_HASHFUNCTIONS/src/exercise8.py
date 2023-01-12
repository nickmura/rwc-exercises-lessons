import secrets
import hashlib

while(True):
    p=secrets.token_bytes(64)
    h=hashlib.sha256(p).hexdigest()
    if (h[0:4]=='0000'): break
print(f'input to get 4 leading zeroes: {p.hex()}')
print(f'hash with 4 leading zeroes: {h}')