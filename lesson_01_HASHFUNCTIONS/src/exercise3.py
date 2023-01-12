import hashlib
import random
fixed_hash = hashlib.md5()
def collision():
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    p = bytes('b'.encode())
    counter = 2
    while True:
        hash1 = hashlib.md5(bytes(p)).hexdigest()[:4]
        hash2 = hashlib.md5(bytes(counter)).hexdigest()[:4]
        
        if hash1 == hash2:
            print(counter, f'{p[:5]}...+{len(p[5:])} characters', hash1, hash2)
            break
        counter += 1 
        p += bytes(random.choice(alphabet).encode())
collision()