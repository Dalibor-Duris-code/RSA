import sympy
import random
import unidecode
from sympy.core.evalf import N
import re

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
    kluce = {}
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

    kluce = {'d': d, 'e': e, 'n': n}
    return kluce

def rozdelenie(vstup, pocet):
    part = []
    for i in range(0,len(vstup),pocet):
        part.append(vstup[i:i + pocet])
    return part

def sifruj(e,n, vstupText):
    vstupText = unidecode.unidecode(vstupText)
    
    text = rozdelenie(vstupText,5)
    
    sifrovanyText = ''
    bpart = ''
    chars = []
    bchars = []

    for part in text:   
        for char in part:
            chars.append(ord(char))
        for bchar in chars:
            bchars.append(bin(bchar).replace("0b","").zfill(12))
        bpart = ''.join(bchars)
        number = int(bpart,2)
        sifra = pow(number, e,n)
        sifrovanyText = sifrovanyText + str(sifra)
        sifrovanyText = sifrovanyText + ' '
        bchars.clear()
        chars.clear()
    
    # print(text)
    # print(chars)
    # print(bchars)
    # print(number)
    # print(str(sifrovanyText))
    return sifrovanyText
    
    
def desifruj(d,n, sifrovanyText):
    blockLen = 5 * 12
    binaryLen = 12
    blocks = sifrovanyText.split()

    plainText = ''
    for block in blocks:
        decrypt = pow(int(block), d, n)
        binaryBlock = format(decrypt, 'b').zfill(blockLen)
        binaryChars = []
        for i in range(0, len(binaryBlock), binaryLen):
            binaryChars.append(binaryBlock[i: i + binaryLen])
        chars = []
        for bchar in binaryChars:
            if int(bchar, 2) != 0:
                chars.append(int(bchar, 2))
        for char in chars:
            plainText += chr(char)

    return plainText