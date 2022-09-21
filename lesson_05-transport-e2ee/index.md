Exercise / assignments for Chapter 5 & 6 of Real World Cryptography, Secure transport & End 2 end encryption.

## exercise-01

> What is referred to as 'Secure transport protocols'?

A 'secure transport' protocol is designed to provide secure communications over a network. This is a abstract term for a lack of, as they can be constructed with a multitude of different cryptographic primitives and have many different uses. They include protocols such as TCP, HTTP, SSH, WPA, IPSEC, Noise, SSL or TLS, etc. The most mature and standardized 'secure transport' protocol is TLS.


## exercise-02

> Why do we need something such as TLS?

It's essential to HTTPS, which is the widely used protocol for the internet and viewing sites. Without TLS, HTTP wouldn't exist.

As a whole, 'secure transport' protocols is explanatory in the unofficial term - securely transport data, whether it be communication or files, it's a general application of cryptography and security that the entire internet is dependant on in one way or another.

## exercise-03

> What is the difference between SSL and TLS?

SSL is a deprecated term as this was what it was first developed in 1995, then in 1999 of Janurary it was defined as TLS 1.0 in [RFC-2246](https://datatracker.ietf.org/doc/html/rfc2246)

## exercise-04

> Is version control a problem with these protocols? Why?

A lot of TLS implementations on servers are severely outdated due to legacy clients and servers many libraries and applications support older versions of the protocol. This is a problem because the amount of vulnerabilities found in these versions is vast; and the implementations to mitigate these exploits are hard to implement. Section 9.3 (page 194 and 195) states this.

## exercise-05

> Are 'secure transport' protocols considered symmetric or asymmetric? Why?

When you connect to a secure transport it's a exchange of private and public keys between the client and the server. Asymmetric exchanges / cryptosystems have notably low maxmimum amounts of data exchanges. You can only send so much data with an asymmetric system. There is an exchange of public keys and symmetric private keys, so it is a hybrid cryptosystem.

## exercise-06

> Why are key exchanges ephermal for these 'secure transport' protocols?

Imagine if the server had the same key exchange (private key) for every handshake with a client. That would leave a lot of vulnerability! We need to throw out the key exchange for every handshake.

## exercise-07

> Describe the handshake phase.

A handshake protocol uses a hybrid encryption system. In Figure 9.4, the process of the handshake for TLS is demonstrated. First the key exchange occurs of the secure transport protocol between the server and the client, as that is the most problematic or involved process.

![image](https://user-images.githubusercontent.com/92566574/191391181-6e59870f-36f0-4d1a-8763-feecc138fca2.png)

If the server parameters or version of TLS doesn't match the client, then the connection or handshake is halted.  


## exercise-08

> What is the Noise protocol?

## exercise-09

> What is the difference between end-to-end encryption and 'secure transport protocols'?

E2EE is not a protocol by itself, rather, it's multiple cryptography primitives used together to create secure communicaton in the environment of adversaries.
You can construct a E2EE protocol many different ways using different primtiives, while secure transport protocols have standards and utilities for specific applications.

For example, TLS is a protocol for securing communication only for central servers and a client or its users, allowing the server to see everything. TLS is nessescary for a server/application to function properly on the internet.

## exercise-10

> What did the initative of encrypted email create?

Email is an unencrypted protocol. This led an individual to create PGP, a hybrid encryption system for secure communication. It is still used extensively today as it is quite accesible. It's a bit uninittuive however. 
