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

Currently not completed.

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

```Output: Hamming distance between a & b strings: 1.0``` 


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

Currently not completed.

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

Currently not completed.




