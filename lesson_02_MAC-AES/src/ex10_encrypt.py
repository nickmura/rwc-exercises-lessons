from Crypto.Random import get_random_bytes
from Crypto.Cipher import AES
from Crypto.Protocol.KDF import scrypt

BUFFER_SIZE = 1024 * 1024  # The size in bytes that we read, encrypt and write to at once


password = "password"  # Get this from somewhere else like input()

input_filename = 'aes-gcm-input/input.txt'  # Any file extension will work
output_filename = input_filename + '.encrypted'  # You can name this anything, I'm just putting .encrypted on the end

# Open files
file_in = open(input_filename, 'rb')  # rb = read bytes. Required to read non-text files
file_out = open(output_filename, 'wb')  # wb = write bytes. Required to write the encrypted data

salt = get_random_bytes(32)  # Generate salt
generatekey = scrypt(password, salt, key_len=32, N=2**17, r=8, p=1)
key = b'\xb5\xed\xc3#\xdc@[\xcf>\xb6\xed\xa0\x927\r\x8az\xb4\xa3[\xb3 \xb5CuR\xd0\xc0O\x95y\xc9'  # Generate a key using the password and salt
print(key)
file_out.write(salt)  # Write the salt to the top of the output file

cipher = AES.new(key, AES.MODE_GCM)  # Create a cipher object to encrypt data
file_out.write(cipher.nonce)  # Write out the nonce to the output file under the salt

# Read, encrypt and write the data
data = file_in.read(BUFFER_SIZE)  # Read in some of the file
while len(data) != 0:  # Check if we need to encrypt anymore data
    encrypted_data = cipher.encrypt(data)  # Encrypt the data we read
    file_out.write(encrypted_data)  # Write the encrypted data to the output file
    data = file_in.read(BUFFER_SIZE)  # Read some more of the file to see if there is any more left

# Get and write the tag for decryption verification
tag = cipher.digest()  # Signal to the cipher that we are done and get the tag
file_out.write(tag)

# Close both files
file_in.close()
file_out.close()