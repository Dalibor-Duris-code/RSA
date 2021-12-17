import sympy
import random
import math

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

    keys = {'e': e, 'd': d, 'n': n}
    return keys


print(generateKey())