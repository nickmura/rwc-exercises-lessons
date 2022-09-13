Exercise / assignments for Chapter 5 & 6 of Real World Cryptography, Signatures and zero knowledge proofs & Randomness and secrets

## exercise-01

> Define a digital signature. What are some real world examples of where they would be implemented

A digital signature is a cryptographic system to verifiy the authenticity of data, typically with the 
signature of a private key. A valid digital signature gives the recipient that the data was created by
a known sender, and that the message was not altered in transit.

A real world example of a digital signature would be creating and sending a transaction on Ethereum, which uses ECDSA to create transactions on their network. The United States Government Printing Office publishes electronic versions of the budget, public and private laws, and congressional laws with digital signatures, to verify the authenticity.


## exercise-02 
> What is the difference between MACs and digital signatures?

A MAC is a symmetric cryptography primitive while a digital signature is a asymmetric cryptography primitive. Anyone can sign a digital signature, regardless if it's invalid or not. Only if it's valid will it have merit.

## exercise-03

> As you saw in chapter 3, authnetication tags produced by MACs must be verified in constant time to avoid timing attacks. Do you think we need to do the same for verifiying signatures?


No, because the signature gets verified by the private key that derived the public key it was sent to. Whenever the signature is signed by the public key's private key, it is verfiied and the signature is valid. Therefore, constant time is not reliant.

## exercise-04

> Provide a demonstration in a programming language of your choice for a digital signature.

*ex04_0.py*

```python
from ecdsa import SigningKey
private_key = SigningKey.generate() # uses NIST192p
signature = private_key.sign(b"Sign this message")
print(signature)
```
```Output: b'\xc7.n\xe0\x13\xd44\xa5i\x90\x08\x81\r}\xa0\x8b\xeb9i\xf9\xa1\xd4w\xe2\xf2[^\x8a\xb3}0E7\xd71a/\x07\x0b\xcb\x87n\xb1\x1b\xb6\xcb\x89\xc6'```


*ex04_1.py*

```python


```

## exercise-05

> How do digital signatures create secure communication for authenticated key exchanges, or public key infrastructures for sites?

Participants can setup a communication channel with a key exchange, then create a signature with a signing key, then send the key exhchange public key along with the signature to the other participant. If the signature is associated with the valid key he was expecting, he can knows it's a **valid authenticated key exchange**. If the signature is invalid, meaning the signing key is not the same as the private key, or vice versa, then it's been MITM attacked.

A public key infrastructure is trusting an authority to sign the public keys of various domain names. In other words, the authority validates the domain's relation with the public key provided by the user. If the signature does match the expected signing key, then a MITM attack has occured. A good example of this would be the **web public key infrastructure** on our browsers.

## exercise-06

> Why are zero knowledge proofs so difficult to construct mathematically? Explain the goal.


The fundamental goal of a zero knowledge proof is to construct an algorithm that shows the acknowledgment of a value without actually revealing it. So if our goal is to share the value x to a recipient without actually revealing the value of x, there needs to be a rigorous algebraic algorithm constructed for it to work feasibly.

A zero knowledge proof is quite rigourous to achieve and wasn't really available in
applied cryptography 

## exercise-07
> What did the Fiat shamir heuristic protocol eventually lead up to?

I made a mistake in this question by prefacing schnorr identification protocol as
fiat shamir heuristic.

The schnorr identification protocol is one of the first primitive zero knowledge protocols, specifically a interactive zero knowledge protocol. Schnorr's identifcation uses what is called a Sigma protocol which has three-movement pattern (Commitment, challenge, proof) meaning a user makes a commitment of a random value, then the recipient of the commitment sends a challenge relative to the commitment, and then it proves it original sender knows a witness of x, which matches the challenge, and commitmement. This is demonstrated in Figure 7.6. it also mentioned, that this has large overhead, as it is interactive. It requires mulitple messages so applied cryptography rarely uses it. This lead to the conception of the Fiat shamir hueristic. It is also insecure if the witness is dishonest, which non-interactive proofs fix.



Fiat shamir heuristic / 'transformation' is a technique for non-interactive proofs of knowledge and creating a digital signature from it. This can have implications of proving information without revealing the underlying information.  They are still used to this day.

This lead to the conception of Schnorr signatures, which implemented Fiat shamir heuristic with a schnorr identification protocol, which is one of the or thee first discrete logarithm based security primtiive.




## exercise-08
> Why is using/implementing RSA signatures generally a bad idea?


The same reason why RSA is kind of frowned upon other asymmetric encryption or cryptography systems. There are many different variations of RSA, and some of them could be vulnerable, and the space of RSA is always changing. The groups and mathematical properties of such vary.

## exercise-09

> Provide a couple real world examples of ECDSA (Elliptic Curve Digital Signature Algorithm) in practice.

- As mentioned, Ethereum and Bitcoin uses ECDSA to sign transactions and messages.

- SSL uses ECDSA to derive its certificates and authenticate a valid certificate. Although, most certificates use RSA to derive public keys and authenticate, for legacy reasons.

- 
  


## exercise-10

> What is the difference between a determinsitic and predictable process?

A predicatable process whose value outcome is knowable at a prior time. A deterministic in which no randomness is involved with the outcome of the process. A determinstic process will always produce the same output from the same input.



## exercise-11

> What could a PRNG be useful?

## exercise-12

> What is one of the most common sources of entropy?

HRNG is a device that generates random sequences of binary input, from noise signals of phenomena in our environment such as thermal noise, photoelectric effect, and other shochastic processes. A hardware generator consists of a transducer to convert the physical phenomena to an electrical signal, then an amplifier to increase the flucuations to a measurable level, then some type of analog to digital converter to convert the output to a binary digit(s). By repeatedly sampling the varying signal, a sequence of random binary is obtained. 

This has very large implications for cryptography, where they are used to generate random keys, and non-determinstic computation from your CPU. This is the most random process we have aside from quantum entropy, which is the ability to find entropy from the nuances of particles moving around on a quantum level.

## exercise-13

> Explain the difference between private and public randomness.

Private randomness is to ensure privacy or security - for example the determinstic process of creating a private key, or a KDF

Public randomness is to provide or produce randomness for others, or a multiple parties, for exmaple, producing a random number on google, or rolling a dice online, or any trivial purpose of randomness that doesn't require robustness.

## exercise-14

> Why would a KDF be useful? Provide an example of a primitive and how it would be implemented.

An KDF is a function that derives secret keys from a secret value such as a password, passphrase, etc. For example, mnemonic seedphrases in [BIP-39](https://github.com/bitcoin/bips/blob/master/bip-0039.mediawiki) (Bitcoin Improvement Proposal 39) that are generated for Bitcoin and Ethereum wallets, use multiple KDFs in the generation of a mnemonic seedphrase (private key). 

First a mnemonic of 12 or 24 words is generated, and then we use PBKDF2 with the mnemonic generated essentially as a passphrase. Then, all of which used with HMAC-SHA512 (HMAC is the most implemented or conventional primitive of a KDF) to generate the seed or private key.

## Bonus questions!

## exercise-15
> How can a digital signature be considered a ZKP?


## exercise-16
> What is the goal of zero knowledge proofs?

## exercise-17
> What is a significant real world example of a zero knowledge proof?


## exercise-18
> What's the difference between interactive and non-interactive proofs?  
