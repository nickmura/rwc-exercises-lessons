import os

from Crypto.Cipher import AES
from Crypto.Protocol.KDF import scrypt

BUFFER_SIZE = 1024 * 1024  # The size in bytes that we read, encrypt and write to at once


password = "password"  # Get this from somewhere else like input()

input_filename = 'aes-gcm-input/input.txt.encrypted'  # The encrypted file
output_filename = 'aes-gcm-input/decrypted.txt'  # The decrypted file

# Open files
file_in = open(input_filename, 'rb')
file_out = open(output_filename, 'wb')

# Read salt and generate key
salt = file_in.read(32)  # The salt we generated was 32 bits long
key = b'\xb5\xed\xc3#\xdc@[\xcf>\xb6\xed\xa0\x927\r\x8az\xb4\xa3[\xb3 \xb5CuR\xd0\xc0O\x95y\xc9'  # Generate a key using the password and salt again
# Read nonce and create cipher
nonce = file_in.read(16)  # The nonce is 16 bytes long
cipher = AES.new(key, AES.MODE_GCM, nonce=nonce)

# Identify how many bytes of encrypted there is
# We know that the salt (32) + the nonce (16) + the data (?) + the tag (16) is in the file
# So some basic algebra can tell us how much data we need to read to decrypt
file_in_size = os.path.getsize(input_filename)
encrypted_data_size = file_in_size - 32 - 16 - 16  # Total - salt - nonce - tag = encrypted data

# Read, decrypt and write the data
for _ in range(int(encrypted_data_size / BUFFER_SIZE)):  # Identify how many loops of full buffer reads we need to do
    data = file_in.read(BUFFER_SIZE)  # Read in some data from the encrypted file
    decrypted_data = cipher.decrypt(data)  # Decrypt the data
    file_out.write(decrypted_data)  # Write the decrypted data to the output file
data = file_in.read(int(encrypted_data_size % BUFFER_SIZE))  # Read whatever we have calculated to be left of encrypted data
decrypted_data = cipher.decrypt(data)  # Decrypt the data
file_out.write(decrypted_data)  # Write the decrypted data to the output file

# Verify encrypted file was not tampered with
tag = file_in.read(16)
try:
    cipher.verify(tag)
except ValueError as e:
    # If we get a ValueError, there was an error when decrypting so delete the file we created
    file_in.close()
    file_out.close()
    os.remove(output_filename)
    raise e

# If everything was ok, close the files
file_in.close()
file_out.close()