Exercise / assignments for Chapter 2 of Real World Cryptography, hash functions.

# exercises lesson-2

## ex-01

> Provide an general abstract definition, and an example of a MAC in use. (Provide a simple definition for a message authentication code).

A message authentication code is a set of data or information used to authenticate and ensure the data integrity of a message. The information/data the MAC provides is dependant on the raw data of the message, and any specific change (e.x where the data originated) to the raw data will change the data set the MAC provides, and therefore is detected. A couple real world use cases are servers authenticating the cookies they recieve from browser clients on websites, implementation within encryption systems such as AEAD, (which provides encryption for a lot of the internet) and the HMAC is used to derive key material in a protocol such as TLS.


## ex-02

> What is the relationship between MAC and a hash function?


As mentioned before in the last lesson, we used hash functions also to provide and ensure integrity and authentication for data. Any change to the raw data of a practical hash function will produce a different hash. 

On page 57 of RWC, David Wong writes, "Message authentication codes are often designed to produce bytes that look random (like hash functions)..." So it's more of a convention to use a hash function with a MAC, (called HMAC) because there's already a conventional general purpose function to authenticate data. We use both simultaenously because a hash is conventionally more appropriate to discern or detect a change in integrity. 

## ex-03

> Not all MACs are PRFs. Can you see why?

The security goal of a psuedorandom function (PRF) that it guarantees that all of its outputs appear random and are indistinguishable, regardless of how the corresponding inputs were chosen, and that it's a deterministic function.

The security goal of a message authentication code that it guarantees the data integrity and authenticates that it's
a valid message from where it originated and the recipient, and that it's a deterministic function (todo: validate that it needs to be
detrministic )

So, these two security goals can overlap, however they are not dependant on each other until you use say, a HMAC. Not nessescarily all authentication is psuedorandom.

## ex-04

>  Provide a demonstration of a HMAC in a programming language of your choice.

```python
    import hashlib
    import secrets
    import hmac

    # my and key as per question
    my = 'Hello, this is my message' # The message I am authenticating and hashing
    key = secrets.token_hex(16)

    # encoding as per other answers
    byte_key = bytes(key, 'UTF-8')  # key.encode() would also work in this case
    message = my.encode()

    # now use the hmac.new function and the hexdigest method
    h = hmac.new(byte_key, message, hashlib.sha256).hexdigest()

    # print the output
    print(my, h)
```

Here a user has a message and a key is inputted to the user. Then the key is encoded in bytes, and the message is encoded in a utf-8 bytes string. Then we use the hmac function with the key, message, and a SHA256 hash function, and we return it the output in a hex digest. 



## ex-05

>  Why can some 128 bit cryptographic algorithms have collision attacks while other algorithms are resistant?

A lot of emphasis was made on the last lesson that exploits / attacks on cryptography standards are due to their digest size. This is misleading, because a lot of the cryptoanalytic attacks on specific standards (such as MD5) take advantage of security properties specific to the standard.


## ex-06

> What is advanced encryption used for, compared to something such as a hash function?

A hash function, is a general purpose tool for providing data integrity of a given input and are often used in combination with other cryptographic tools or applications. They can be used for encryption purposes, but not on it's own. 

Advanced encryption, such as AES, is solely for the purpose of encoding information/communication, creating security for authorized parties.



## ex-07

> What is the fundamental problem demonstrated with AES-ECB? (Provide an example or demonstration).
> 
Creating an intuitive demonstration for ECB is a bit difficult because the crypto libraries providing potential demonstrations for this standard are a bit difficult to work with, since ECB has quite insecure security properties.

On *page 71, Figure 4.7*, There exists a diagram showing a well known example, outlining the fundamental insecure security property of ECB.

![image](https://user-images.githubusercontent.com/92566574/182693904-8a5067e5-d887-4b0c-a174-59c65f0364d6.png)

It is mentioned prior, that AES is a block cipher and one of the constraints, is that a block cipher can only encrypt a block by itself. Meaning if you have a message or data set that is larger than 128 bits (16 bytes), padding and a mode of operation is used, to divide the data into 16 bytes or factors less than 16 bytes.

However, the mapping used (electronic codebook) for deciding what value of plaintext for ciphertext is encrypted, is reused per block. So that is why patterns of ciphertext can be deduced, because the ciphertext is predictable.

## ex-08

> In AES-CBC, how can we prevent the ciphertext as well as the IV from being modified by an attacker?

AES-CBC attempts to solves the issue that AES has with AES-ECB, revealing information about the plaintext because there are patterns of the 1:1 operation (plaintext to ciphered) in the ciphertext that can be deduced when the plaintext/data to be encrypted is larger than 16 bytes, due to the limitations of block ciphers.

AES-CBC uses something called cipher block chaining (CBC), it takes an additional value called an initialization vector, which is randomized and unpredictable, and changes the value and 1:1 operation for each block of 16 bytes.
Therefore, the encryption for the entire plaintext does not reveal any information or pattern of the plaintext.

However, the problem with this mechanism (aswell as ECB) is that there is no integrity mechanism. An
attacker can flip bits, or rather modify the the IV or ciphertext, causing the plaintext to change. This is demonstrated on *page 73, Figure 4.10*.

![image](https://user-images.githubusercontent.com/92566574/182949236-f1298397-996a-4a15-b8df-2f2943aeda57.png)


So we are able to combat this by implementing the HMAC, which provides an inherent integrity mechanism and invalidates any changes made to the cipher or IV, once the encryption has been made for the message. It is mentioned, that we use the MAC after padding the plaintext, and encrypting it over both the ciphertext and the IV,
so in other words, after all encryption properties have been made to the plaintext, we apply the HMAC over it, like
an indestructible piece of armor!

