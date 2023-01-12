import hashlib

fixed_hash = hashlib.md5()
def preimage():
    p= b'Hello world'
    counter = 0
    fixed_hash = hashlib.md5(p).hexdigest()[:5]
    while True:
        variable_hash = hashlib.md5(bytes(counter)).hexdigest()[:5]
        if fixed_hash == variable_hash:
            print(counter, fixed_hash, variable_hash)
            break
        counter += 1
preimage()