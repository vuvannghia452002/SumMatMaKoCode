# -*- coding: utf-8 -*-
"""
Created on Thu May 27 22:05:13 2021

@author: PC
"""

from Crypto.Hash import SHA256
from Crypto.Random import random
from Crypto.Util.number import bytes_to_long
from Crypto.Util.number import long_to_bytes
from Crypto.Util.number import getPrime
from sympy.ntheory import is_primitive_root 

def generate_key():
    p = getPrime(512) 
    g = getPrime(128)
    x = random.randint(1, p-1)
    h = pow(g, x, p)

    return p, g, x, h

def encrypt(msg: bytes, g, p, x, h: int):
    y = random.randint(1, p-1)

    s = pow(h, y, p)
    c1 = pow(g, y, p)
    c2 = bytes_to_long(msg) * s

    return long_to_bytes(c1), long_to_bytes(c2)

def decrypt(c1, c2: bytes, x, p: int) -> bytes:
    temp1 = bytes_to_long(c1)
    temp2 = bytes_to_long(c2)
    s = pow(temp1, x, p)
    dm = (temp2 * pow(s, -1, p)) % p
    
    return long_to_bytes(dm)

def main():
    inp = input("Input the string you want to encrypt: ")
    p, g, x, h = generate_key()
    c1, c2 = encrypt(inp.encode(), g, p, x, h)

    print(f"g: {g}")
    print(f"x: {x}")
    print(f"p: {p}")
    print(f"c1: {c1}")
    print(f"c2: {c2}")

    d1 = decrypt(c1, c2, x, p)
    assert(d1 == inp.encode())

if __name__ == "__main__":
    main()