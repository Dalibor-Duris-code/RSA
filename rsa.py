import sympy
import random
import math
import unidecode
import re

from sympy.core.evalf import N

g_blockLen = 5
g_binaryLen = 8

def genPrimeNum():
    return sympy.randprime(1*(10**12), (1*10**13))

def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def modInverse(a, m):
    j = m
    x = 1
    y = 0 
    if (m == 1): 
        return 0

    while (a > 1):
        q = a // m
        t = m
        m = a % m
        a = t
        t = y
        y = x - q * y
        x = t
        
    if (x < 0):
        x += j
    return x

def generateKey():
    
    p = genPrimeNum()
    q = genPrimeNum()

    n = p * q

    phi = (p-1) * (q-1)

    e = 0
    index = 0
    while index != 1:
        e = random.randrange(1, phi)
        index = gcd(e, phi)
    d = modInverse(e, phi)

    key = {}
    key = { 'e':e, 'd':d, 'n':n }
    return key


# def encryption(e, n, plainText):
#     plainText = unidecode.unidecode(plainText)
#     blockLen = g_blockLen
#     binaryLen = g_binaryLen
#     blocks = []
#     for i in range(0, len(plainText), blockLen):
#         blocks.append(plainText[i: i + blockLen])

#     ciphertext = ''
#     for block in blocks:
#         chars = []
#         for char in block:
#             chars.append(ord(char))
#         binaryChars = []
#         for char in chars:
#             binaryChars.append(format(char, 'b').zfill(binaryLen))
#         binaryBlock = int(''.join(binaryChars), 2)
#         encrypt = pow(binaryBlock, e, n)
#         ciphertext += str(encrypt) + ' '

#     return ciphertext

# def decryption(d, n, cipherText):
#     cipherText = re.sub(r'[^0-9 ]', '', cipherText)
#     blockLen = g_blockLen * g_binaryLen
#     binaryLen = g_binaryLen
#     blocks = cipherText.split()

#     plainText = ''
#     for block in blocks:
#         decrypt = pow(int(block), d, n)
#         binaryBlock = format(decrypt, 'b').zfill(blockLen)
#         binaryChars = []
#         for i in range(0, len(binaryBlock), binaryLen):
#             binaryChars.append(binaryBlock[i: i + binaryLen])
#         chars = []
#         for bchar in binaryChars:
#             if int(bchar, 2) != 0:
#                 chars.append(int(bchar, 2))
#         for char in chars:
#             plainText += chr(char)

#     return plainText

# #print(generateKey())
# keys = generateKey()
# #print(keys)
# kokotina = encryption(keys['e'],keys['n'],'kokot jebnuty')
# print(kokotina)
# pica = decryption(keys['d'], keys['n'],kokotina)
# print(pica)