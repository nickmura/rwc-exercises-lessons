import zlib
s = b'Hello world'

crc = zlib.crc32(s)
print(crc)
