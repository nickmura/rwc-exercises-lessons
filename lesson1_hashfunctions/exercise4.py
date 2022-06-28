# import modules
from scipy.spatial.distance import hamming

# define strings
a = 'testing 120'
b = 'testing 123'


#calculate Hamming distance between the two strings
result = hamming(a,b)

#print the Hamming distance between the two strings
print('Hamming distance between a & b bytestrings:', result)


