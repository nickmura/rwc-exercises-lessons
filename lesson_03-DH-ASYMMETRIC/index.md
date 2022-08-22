Exercise / assignments for Chapter 5 & 6 of Real World Cryptography, Key exchanges & Asymmetric encryption and hybrid encryption.


# exercises lesson-3

## ex-01
> What is a MITM attack in the context of key exchanges? And why is it significant?


A man in the middle attack is when an attacker takes advantage of a poorly authenticated, or unauthenticated key exchange. There are many ways an attacker can intercept a connection for a key exchange. Ultimately the goal is for the attacker to impersonate the reciever or initiator for a shared secret, or host the communication line, basically having control of the entire 'secure' connection, in most cases.

Take for instance, a SSL certiicate. A certificate authority, is an entity that stores signs and issues digitcal certificates. It validates the secure connection of websites on the browser. So information is not written in plaintext. If someone was to intercept the private key of the certificate authority, all the traffic coming to and from the connection could be monitored, potentially sensitive information in plaintext. Regardless of whether or not it's a passive or active MITM attack, a user has intercepted the communication line and is altering/eavesdropping communications.

## ex-02
> What is the difference between an active MITM, and a passive MITM?

An active MITM attack is when an attacker is impersonating the reciever or initatior and the goal is to delete, or change the data or system resources of the communication, or even potentially damage the system resources. the victim can easily detect the attack. 

A passive is when the attacker is solely eavesdropping. The system resources are not changed, rather the goal is to recieve data of either parties and use it to the attacker advantage. It is difficult for the victim to detect the attack.


## ex-03

> Outline or describe the group Diffie Hellman uses. (what kind of set of elements it uses, etc)?


Diffie Hellman strictly uses a prime integer set of elements.

The binary operation for the group, or the type of group is multiplicative.

## ex-04
> What is the significance of the discrete logarithm problem, specific to Diffie Hellman?

The discrete logarithm problem basically says given an integer N, generator G, power x, and mod y find G^x mod y = N. On page 95, figure 5.2.2 explains this.

*Imagine that I take a generator, let’s say 3, and give you a random element among the ones it can generate, let’s say 2 = 3x
 mod 5 for some x unknown to you. Asking you “what is x?” is the same as asking you to find the discrete logarithm of 2 in base 3. Thus, the discrete logarithm problem in our group is about finding out how many times we multiplied the generator with itself in order to produce a given group element*

 It then further explains in the next paragraph how this is how this can be very difficult when provided large numbers and Diffie Hellman relies on this property for it's cryptographic robustness.

 *In our example group, you can quickly find that 3 is the answer (indeed, 33
 = 2
mod 5). But if we picked a much larger prime number than 5, things get much more
complicated: it becomes hard to solve. This is the secret sauce behind Diffie-Hellman.
You now know enough to understand how to generate a key pair in DH:*

So diffie hellman uses the discrete lograithm to compute private keys.

## ex-05
> Why are many standards of Diffie Hellman considered deprecated? What makes one of them useful?

Diffie Hellman has been around for a while (since 1979) and there has been many libraries and standards made over the past 40 years. It explains on page 97 that over the course of the past decade a few notable deemed secure protocols have been broken due to their modified DH groups and additional math that can leak or expose key leakage, large inefficency or exposure to cryptoanalysis. At this point, the standards can be a bit arbitrary.

*In the past, many libraries and software often generated and hardcoded their own
parameters. Unfortunately, they were sometimes found to be either weak or, worse,
completely broken. In 2016, someone found out that Socat, a popular command-line
tool, had modified their default DH group with a broken one a year prior, raising the
question whether this had been a mistake or an intentional backdoor. Using standardized DH groups might seem like a better idea, but DH is one of the unfortunate counterexamples. Only a few months after the Socat issue, Antonio Sanso, while reading
RFC 5114, found that the standard had specified broken DH groups as well.*

It then elaborates that the main implemented and generally accepted DH standard is ECDH as of today, or (less accepted) RFC 7919


*Due to all of these issues, newer protocols and libraries have converged towards
either deprecating DH in favor of Elliptic Curve Diffie-Hellman (ECDH) or using the
groups defined in the better standard, RFC 7919 (https://www.rfc-editor.org/info/rfc7919). For this reason, best practice nowadays is to use RFC 7919, which defines
several groups of different sizes and security. For example, ffdhe2048 is the group
defined by the 2,048-bit prime modulus...*

## ex-06
> Why do the other standards of Diffie Hellman have best practice 2048 bit prime number security while ECDH is 256 bit?




## ex-07
> Explain the goal of asymmetric encryption and provide a real world example of what it's used for.

Asymmetric encryption is to ensure and validate that for the sender only the recipient can decrypt the data/communication it was sent, given that they own the private key that derived the public key.

Asymmetric encryption is used in email security, digital signature applications, and the most essential cryptographic application online - TLS, which is a protocol that authenticates the server and preferrably the client as well - and negotiates a shared encryption key, then encrypts normal traffic aswell for only the sender and reciever to recieve (server(s) and/or client).

## ex-08
> Using the same shared secret with everyone would be very bad, can you see why?

Having a universal shared secret would entail using it to decrypt or encrypt any message that isn't intended for your recipient. A recipient for one message could use the same secret for another message intended for another reciepient.

## ex-09
> Explain the limitation(s) of asymmetric encryption and why it occurs.
- It's a slow process compared to symmetric cryptography due to what is called a "slow hardness assumption", which is the reliance on an inherently inefficient primitive such as a discrete logarithm or integer factorization, which causes the problem of asymmetric cryptography not being appropriate for large messages, since decrypting it is not nessecarily in polynomial time.



## ex-10
> What is key encapsulation and why is it important?

Key encapsulation is the mechanism that secures symmetric key
material using asymmetric cryptorgraphy. Long message / large data sets are really difficult to send in asymmetric systems, therefore we used what is called an hybrid encryption / cryptosystem, which allows us to send large data as the symmetric data is much smaller than the raw data itself, as I elaborated in the previous exercise.


## ex-11
> Explain the million message attack. What is the most common implementation of RSA today?

In 1998 someone named Daniel Bleichenbacher wrote a paper titled "Chosen ciphertext attacks against protocols based on the RSA encryption standard PKCS #1" which demonstrated cryptanalysis through bruteforce. Basically, a an attacker can submit arbitrary RSA encrypted messages to itself, observe how influenced the decryption (if it at all was corresponding to the real ciphertext of the attacked encrypted message) and continue the attack based on previous observations of the arbitrary messages, which typically requires a million messages.

## ex-12
> Explain the three mathematic algorithm problems that these cryptographic primitives rely on page 121, Figure 6.13.


Diffie Hellman relies on the *discrete logarithm problem*, which is one of the three hardness assumptions that asymmetric cryptography relies on. Here is a demonstration
I've made that outlines the different aspects of the algorithm. 
In more simpler terms of this diagram, to compute the algorithm to get A, it's relatively easy. But to reverse and solve for `a`, and the `mod p` for the generator, it's inherently a very difficult problem.
It's analagous to a one way function but in a formal mathematical sense.
![image](https://user-images.githubusercontent.com/92566574/185941130-1ae0d73d-a15b-42ad-9401-8d1833d201d7.png)


Elliptic Curve Diffie Hellman relies on the *elliptic curve logarithm problem* which is simply the algorithm we mentioned above but specific to the elliptic curve group that is different than the Galois group other standards of DH rely on.


RSA relies on the factoring problem of prime numbers
Multiplying two large prime numbers results in a product that is extremely difficult to compute for either. The only person who can decrypt the message
is the individual who knows the prime numbers.


![image](https://user-images.githubusercontent.com/92566574/185953439-5e5d166e-8ab9-4b9e-bde4-48f66f012448.png)
