Exercise / assignments 11 & 12 of Real World Cryptography, User authentication & Crypto as in cryptocurrency?


## exercise-01

> What is the goal of user authentication?

Allow services and applications to identify users based on unique parameters. For example, allowing a user to log in to a service and have personalization or permissions specific to their identity.

Another form of user authentication would be connecting to a SSH session with a webserver, to perform FTP. Only certain users can perform such an action to a server, which is why we need user authentication!

## exercise-02

> What is the difference between user authentication and data authentication?


User authentication is to ensure the integrity of a given user being
valid which a wide range of cryptography and networking primitives can provide, where as, data authentication is to ensure the integrity of a given set of data being  valid and expected. Hash functions, MACs, etc.


## exercise-03

> what is the most common form of general user-authentication?

Username and password, password stored in database. Single-sign-on authentication is becoming more conventional by the day however user authentication for those applications (Google, Apple, Facebook, etc) are created with username and passwords

## exercise-04

> Name a few fundamental problems with passwords.

- Passwords can be brute-forced and cracked, which requires more robust or verbose password requirements for services

- The more verbose the requirements have to be for a password, the less intuitive it is to authenticate a user, which potentially sacrafices the entire point of a password - to authenticate a user (if the user doesn't remem ber their password since it was so robust)
## exercise-05

> Could you think of a real world example of a Single-sign on?

The problem with 'single sign on' applications is that they have to reach a wide scale of adoption for them to be precedented or adopted by a mass user-base. So, services such as Google, Twitter, Facebook, Apple, etc can use a single sign on with much ease use, because well there has already been an assimilation and adoption for their service(s) by the general user-base.

Also, single-sign-on as mentioned above is typically an alternative to a conventional 'username and password' user authentication experience. An unprecedented application/protocol, in recent years is an application called Metamask, which acts as a web authentication wallet for signing messages, transactions and exchanging funds for the larger portion of Web3, which isn't an alternative; its the standard for user authentication for web3 applications. There is no need for users to assimilate as there was nothing to assimiliate for these type of applications in the first place!


## exercise-06

> What is an 'oblivious psuedorandom function'?



## exercise-07

> Why is cryptography significant to cryptocurrency or vice-versa?


Cryptocurrency is built of cryptography systems and is the forefront of cryptography research as the entire environment is adversarial, which is perfect for cryptography, and the intended purpose for cryptography. Cryptocurrencies are significant to cryptography because as mentioned they provide an excellent and involved ecosystem for research and development as crypto solutions will always 


## exercise-08

> Why are cryptographic gurantees so nessescary for blockchain & cryptocurrency applications?

Cryptocurrencies, in general, exist and were concieved for an environment where ALL participiants are assumed to be adversarial. The reason we need strong cryptographic gurantees as it's the dependant techniques to ensure the integrity of the system. Cryptography, as a general definition, is 
'..the practice or study of techniques for secure communication in the presence of adversarial behavior'. So comunicating, and transacting with adversarial participants in an economic system, probably requires cryptography, aswell as all of the applications built for these participants. 

## exercise-09

> Give a few reasons why cryptography development and research has been centered around cryptocurrencies in the last few years.

Cryptography has been a bit of a niche field of research - cryptocurrencies and blockchain development has created a new demand for cryptography research as the environment is maximally adversial so applied cryptographic security gurantees are nessescary, and will recieve the most recongition amd research. Cryptography research and applications will still be researched outside of cryptocurrencies and blockchains.

## exercise-10

> What is a merkle tree?

A merkle tree is a hash tree in which every leaf is labelled with a hash of a data block, and every node that is not a leaf. A child node, allows efficient and secure verification of the contents of a large data structure.

## exercise-11 

> Name a few implementations of ECDSA in blockchains.

ECDSA is used for ethereum digital signatures.
ECDSA is also used for constructing public keys, and addresses.
ECDSA is also used for bitcoin digital signatures


## exercise-12

> What are layer 2 protocols?
