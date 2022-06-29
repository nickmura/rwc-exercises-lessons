Exercise / assignments for Chapter 2 of Real World Cryptography,
hash functions.

# exercises lesson-1 

## ex-01
> MD5 is said to be ‘insecure/broken’. Which security properties are vulnerable? Prove it.

MD5 has a fixed digest size / value of 128 bit. Unlike other hash functions such as SHA3 which have arbitrary large digest sizes, this
allows attackers to exploit the high probability of finding a collision. Since the digest is 128 bit, we can deduce we have a probability >50% of finding a collision once we compute over 2^64 operations to find a collision or the original input. Today a reasonable digest size is at least 256 bit, because it would require 2^128 operations to be computed, to find an exploitation, which is not reasonable to exploit.

## ex-02
> Calculate the total theoretical number of attempts it would take to brute force various hashes digests (MD5, SHA-1, SHA256).

As mentioned in the previous exercise, the probability to be greater than 50% of finding a collision, or the input for a hash function is 1/2 of the digest size. So...

- MD5 has a fixed digest size of 128 bits, so >2^64 guesses would provide a high probability of finding an exploit.
- SHA-1 has a fixed digest size of 160 bits, so >2^80 guesses would provide a
high probability of finding an exploit.
- SHA-256 has a fixed digest size of 256 bits, so >2^128 guesses would provide a high probability of finding an exploit.

## ex-03
>Find a digest collision of the first 4/6 bits of any two input string MD5 hash digests.

I have an demonstration of a collision in which 3-6 of the leading bits of the hash are identical... however with larger collisions time complexity is worse. hash is an input of only characters, and hash2 is an input of only numbers (an increment of counter). The example is for 4 characters. I guarantee there's a much more efficient way to get a collision than my algorithm :( _(exercise3.py)_
```python
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
```

```
Output: 34848 b'xib'...+34842 characters 26d9 26d9
```




## ex-04
>Explain and demonstrate how to calculates the Hamming Distance between two strings.

The hamming distance is a comparison of the position or indexes of two strings or vectors are different. So for example, 0110 and 0000 have different positions at index 1 and 2 (index starting at 0.) I have a
demonstration in python using the scipy library. As you can see, there is only one discrepancy in the last character of the two strings. _(see exercise4.py)_

```python
# import modules
from scipy.spatial.distance import hamming

# define strings
a = 'testing 120'
b = 'testing 123'

#calculate Hamming distance between the two strings
result = hamming(a,b)

#print the Hamming distance between the two strings
print('Hamming distance between a & b strings:',result)
```

```
Output: Hamming distance between a & b strings: 1.0
``` 


## ex-05
> What is the Hamming Distance between any bytestring hashes where i1 (unmodified) and i2 has 1 bit flipped.

I have added to the previous demonstration and converted equivalent strings to bytestring and then converted to binary.
One index of the bytestrings bytes being changed results in the same hamming distance, however I decided to convert to
binary to change the bits.

```python
# import modules
from scipy.spatial.distance import hamming

# define strings
a = 'testing 123'
b = 'testing 123'

# converting strings to bytestrings, then converting to binary (to flip bits)
a_b = bytes(a, 'UTF-8')
b_b = bytes(b, 'UTF-8')
bytestring_a = []
bytestring_b = []
bitstring_a = []
bitstring_b = []

for bytes in a_b:
    bytestring_a.append(bin(bytes)[2:])
bytestring_a = ''.join(bytestring_a)
print(bytestring_a)

for bytes in b_b:
    bytestring_b.append(bin(bytes)[2:])
# flipping the bit of index 2 of bytestring_2 (probably inefficient)
bytestring_b = ''.join(bytestring_b)
bytestring_b = list(bytestring_b)
bytestring_b[2] = '0'
bytestring_b = ''.join(bytestring_b)
print(bytestring_b)

#calculate Hamming distance between the two bytestrings
result = hamming(bytestring_a, bytestring_b)

#print the Hamming distance between the two bytestrings
print('Hamming distance between a & b bytestrings:',result)
```

```
Output:
1110100110010111100111110100110100111011101100111100000110001110010110011
1100100110010111100111110100110100111011101100111100000110001110010110011
Hamming distance between a & b bytestrings: 1.0
```
Because the the strings were identical, the hamming distance prior to the bitflip was zero. There is only one discrepancy because we changed the second index from 1 to 0.

## ex-06
> Explain and demonstrate the difference b/w Second Pre-Image Resistance and Collision Resistence.

On page 29, chapter 2 of Real World Cryptography, figure 2.4 and 2.5 show a diagram presenting a great abstraction of what the difference between them. Because they are similar, I think this greatly demonstrates
their difference! They are mistaken for one another, people think of collision attacks when really are thinking of the former (second pre image). I am also guilty of that problem.

![image](https://user-images.githubusercontent.com/92566574/176204302-0044fc7c-16b2-4ac7-9086-e2ea9ea14d03.png)

![image](https://user-images.githubusercontent.com/92566574/176204386-2f33cefb-8117-4ef8-abbe-adfb092f25c3.png)

The first diagram shows that _second pre image resistance_ or a _secoond pre image attack_ is when given X, find Y such that, H(x) = H(y).
The second diagram shows that _collision resistance or a _collision attack_ is find x and y such that, H(x) = H(y).

Second pre image attacks, counter-intuitvely are much more difficult to accomplish. Let's use
the example of the birthday problem or paradox. As mentioned in the next question, it's the
probability that a pair of two people will share the same birthday, which is a collision attack! _(Find x and y such that B(x) = B(y))_ 

But if we were to say... Given x, find y that has the same birthday as X... The probability would be much, much less. Because we are discriminately finding a B(y) also equal to a predetermined B(x). Collision attacks are indiscriminate! Any x and y that have equal hashes will do. 

I have an algorithm for a second pre-image attack in which the first 5 characters of the digest are identical. As far as I know, there isn't a feasible pre-image attack for an entire MD5 hash. More characters, worse time complexity. _(exercise6.py)_
```python
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
```

```
Output:
254351 3e259 3e259
```


For collision resistance, there is a demonstration in _[(exercise1.py)](https://github.com/nickmura/realworld-cryptography-studygroup/blob/main/code/01_Hash_Functions/e0101.py)_ (provided by zk-community) that finds two inputs of images casted as bytestring, that provide a collision of the same hash. When executed or ran, it provides a collision of two inputs:
```
Output:
>>> Collision detected! <<< md5:
253dd04e87492e4fc3471de5e776bc3d
-----

Binary File Collision Detection
 OK  sha256

 OK  md5
```


## ex-07
> Explain and demonstrate the calculation of 'The Birthday Bound' Paradox.

The birthday paradox is a probability theory problem, that asks for the probability in a set of n randomly chosen people at least two will share
a birthday. Contrary to what you would believe, the probability of a shared
birthday exceeds 50% in a group of only 23 people! How is this the case?

Well, the probability of any two people not having the same birthday is _(364/365)_. In a group containing n people, there are n choose 2 (nC2) pairs of people. or (n * (n - 1) / 2)
The probability of no two people of n sharing the same birthday can be approximated as multiplying the probability of any two people not having the same birthday multiplied by the probability of all other pairs of n. In other words, combining the two formulas of probability together provides us the probability of any pair of n NOT sharing a birthday. This approximation assumes all birthdays are
independent, as n is chosen randomly.

(364/365)^(23 * (23 - 1) / 2) = 0.49952284596

_(23 * (23 - 1) / 2) = 253_

So the approximate probability of two people NOT sharing a birthday when n is 23 is 49.952284596%, w. Which means, the probability
for someone sharing a birthday exceeds the probability of NOT sharing a birthday!

1 - 0.49952284596 = 0.50047715404

_(exceeds 50% !)_

## ex-08
> Find an input string which results in a SHA256 hash with 1/2/X 0's (zero).

Here is a simple algorithm that results in a SHA256 with 4 leading zeroes. _(exercise8.py)_
```python
import secrets
import hashlib

while(True):
    p=secrets.token_bytes(64)
    h=hashlib.sha256(p).hexdigest()
    if (h[0:4]=='0000'): break
print(f'input to get 4 leading zeroes: {p.hex()}')
print(f'hash with 4 leading zeroes: {h}')
```

```
Output:
input to get 4 leading zeroes: d33cdcf04734e2776a2a443a2bc3f66296b907b55712444ad8aa6c5822af7182c9a9bd95dca7ebec659d0e5e1adf10d5dff61fabe3758bef23f0c9ec73cd9398
hash with 4 leading zeroes: 0000e8706579f94fdf28be2ad73573b0db71d81b074a97009e9806c9c620021e
```



## ex-09
> Find X (look up, don't over think it): md5(X).digest() > d41d8cd98f00b204e9800998ecf8427e

Using this [code](https://gist.github.com/miodeqqq/8e064f14d446348914f0e45818234a2e?permalink_comment_id=4002462#gistcomment-4002462) I found here
for decrypting a MD5 hash, with the change below I made to it's result _(exercise9.py)_:

```python
print(f"The input for this hash or reversal is: '{decryptMD5(sys.argv[1])}'")
```
Executing/running this file with the provided hash returns me this output, an empty string as the input for the hash:
```Output:
[*] Decrypting hash!
decryptMD5 Time: 0.000 s
The input for this hash or reversal is: ''
[+] Hash decrypted! :)
```

[Other resource cites this hash reversal as an empty string aswell.](https://md5.gromweb.com/?md5=d41d8cd98f00b204e9800998ecf8427e)

## ex-10
> Prepare an exercise related to XOR bitwise operations (compress/uncompress)



 _Given only the output of a XOR operation, why can we uncompress or derive a definitive input?_


 Given z (output), find x (input 1) and y (input 2) is simply not enough information to derive a discriminate or definitive input that would hold true
 for all intents and purposes. (as far as I know) (pre-image attack is!). Take a look at the diagram from Real World Cryptography.
 

 &nbsp;
 
 ![image](https://user-images.githubusercontent.com/92566574/176490877-2d147b36-b447-4115-99ba-e586170bb589.png)

&nbsp;

As you can see, the logic can compute the same output for different combination of inputs. This means we can output the same thing with many different inputs, there we cannot evidently find the definitive input(s) that created this output! We can only get some inputs that
are equivalent to the input, or a collision. We cannot say these are
the specific inputs we are looking for, so it's not useful. x and y
could be anything If we were given x (an input) and z, to find y (another input), it would be much easier to come to
a definitive input (pre image attack)

&nbsp;

![image](https://user-images.githubusercontent.com/92566574/176491254-61da23a8-9f36-47d7-a97f-b14e3ea433bc.png)
 


## ex-11
> Prepare an exercise related to serialization / deserialization

_What does serialization and deserialization mean?_
&nbsp;

Serialization is the idea of encoding or converting an object to a stream of bytes to store the object or transmit/transfer the object in a integral form that mitigates side effects, when performing actions or data exchange.

Deserialization is the reversal of the aforementioned. Transforming the bytes stream back to it's original form and executing its intended purpose, (typically in the form of communicating or transfering). A usecase for serialization can simply be data storage, and deserialization when data needs to be accessed.


## ex-12
> Explain and demonstrate the difference between cryptographic hash functions and checksum functions (CRC32)

A hash function is a one way function that takes a input of data and produces a unique string of bytes in return. The hash function is precedented and is present in all faucets of cryptography, and the internet. Construction of hash functions are rarely used alone, as they are a rudimentary building block of cryptography. As demonstrated in previous exercises such as _exercise4.py, exercise6.py, and exercise8.py_ the implications of constructing a hash function are intuitive.

A checksum is a mathematical value typically assigned to a piece of data to verify its validity, such as that it has not been changed. In the case of CRC32, it returns or computes a 32 bit integer value from a byte data type. Demonstrated below _(exercise12.py)_
```python
import zlib
s = b'Hello world'

crc = zlib.crc32(s)
print(crc)
```

```
Output: 2346098258
```


