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

Noise protocol is a cryptography framework/library based on Diffie Hellman key exchanges. Noise can be implemented for simple communication or a secure transport. The reason why it's significant or relevant to us is because it consists of two parties exchanging a handshake, which there are many different handshakes the noise protocol can rely on for a protocol.

Noise is a **protocol framework**. Meaning it is not a singular protocol, rather it's a framework for building many different protocols.

## exercise-09

> What is the difference between end-to-end encryption and 'secure transport protocols'?

E2EE is not a protocol by itself, rather, it's multiple cryptography primitives used together to create secure communicaton in the environment of adversaries.
You can construct a E2EE protocol many different ways using different primtiives, while secure transport protocols have standards and utilities for specific applications.

For example, TLS is a protocol for securing communication only for central servers and a client or its users, allowing the server to see everything. TLS is nessescary for a server/application to function properly on the internet.

## exercise-10

> What did the initative of encrypted email create?

Email is an unencrypted protocol. This led an individual to create PGP, a hybrid encryption system for secure communication. It is still used extensively today as it is quite accesible, you can generate PGP keys on a multitude of sites online. It's a bit uninitutive however. 

## exercise-11

> What are some of the problems with GPG?

As mentioned in the last question, it's unintuitive. It's main reason for being conceived was to encrypt a standardized unencrypted application (email, which is still unencrypted) but requires overhead and is quite technically involved for a hybrid encryption system. It is not cryptographically vulnerable; meaning you can't crack a PGP key however there are significant reasons as to why you shouldn't use it, such as signing messages is redundant (you can send pgp messages without signing the message). Encryption is not authenticated.

## exercise-12

> How are E2E (end-2-end encryption) protocols typically constructed?

E2EE protocols are typically hybrid cryptosystems. asymmetric cryptography albeit more practical and less overhead, they have severala constraints such as speed and size being low.

Symmetric cryptography doesn't have these constraints, albeit more involved, and less practical in of itself. So we use such primtives together to get the best of both worlds.  E2EE probably has other specific primitives per use, although generally if not every E2EE consists of a hybrid cryptosystem.


## exercise-13

> What is a 'diffie hellman ratchet' and what purpose does it serve?


On the [signal](https://signal.org/docs/specifications/doubleratchet/) specifications, it states the diffie hellman ratchet is used to generate ephemeral keys between two parties. It shares these keys intuitively between the parties, per message. Everytime a message is sent, a new key is sent with the message to the recipient. Who then sends their key to the previous sender (now recipient) when they send a message. This acts a 'ping pong' mechanism.

*"If an attacker steals one party's sending and receiving chain keys, the attacker can compute all future message keys and decrypt all future messages. To prevent this, the Double Ratchet combines the symmetric-key ratchet with a DH ratchet which updates chain keys based on Diffie-Hellman outputs.*

*To implement the DH ratchet, each party generates a DH key pair (a Diffie-Hellman public key and private key) which becomes their current ratchet key pair. Every message from either party begins with a header which contains the sender's current ratchet public key. When a new ratchet public key is received from the remote party, a DH ratchet step is performed which replaces the local party's current ratchet key pair with a new key pair.*

*This results in a "ping-pong" behavior as the parties take turns replacing ratchet key pairs. An eavesdropper who briefly compromises one of the parties might learn the value of a current ratchet private key, but that private key will eventually be replaced with an uncompromised one. At that point, the Diffie-Hellman calculation between ratchet key pairs will define a DH output unknown to the attacker."*


## exercise-14

> Why does Signal use X3DH, or three types of ephemeral keys?

I actually am incorrect, and apologize for misinterpreting the protocol. X3DH does not consist of three ephemeral keys.

![image](https://user-images.githubusercontent.com/92566574/192324420-420a8dd1-bba2-4d47-9da7-a906913dbca0.png)

X3DH consists of an identity key, a signed public key to verify the identity of the identity key, and a bundle of signed 'prekeys'. The identity key is not ephemeral, meaning it is generated at the conception of the user. The prekeys however, are indeed ephemeral. They are generated and provided to a fellow user on a basis of communication


![image](https://user-images.githubusercontent.com/92566574/192324475-2e21c4fa-5730-42da-a7d2-c6e30343d05c.png)

The prekeys and idenitty keys are stored on a trusted server, although these keys do not create vulnerability. A key is signed with the private key (on a device of a user) and only provides forward secrecy. Once the session or message between a recipient is sent, the ratchet occurs (last exercise) and another prekey is used to establish a secure communication.

The reason for X3DH even while it may be a bit complicated under the hood is due to offline constraints of such a system. ECDH excahnge requires both parties to be offline to actually exchange keys, so X3DH and the ratchet provides the practical use for offline messaging and forward secrecy.







## exercise-15

> What is the difference between the Signal protocol and the Matrix protocol?

Signal is a properitary protocol that only select applications use such as Messenger, Skype, Whatsapp, Facebook, Skype, and Signal messenger. 

Matrix is a open protocol that anyone can implement / interoperate with. It intends to standardize federated protocols for end-to-end encrypted messaging.
