# -*- coding: utf-8 -*-
"""
Created on Mon Jun  7 21:24:05 2021

@author: PC
"""

from Crypto.PublicKey import DSA
from Crypto.Signature import DSS
from Crypto.Hash import SHA256
from Crypto.Util.number import bytes_to_long
from Crypto.Random import random


def generate_key(bits: int):
    key = DSA.generate(bits)
    q = key.q
    p = key.p
    
    h = random.randint(2, p-2)
    g = pow(h, (p-1)//q, p)

    return (p, q, g)


def sign(msg: bytes, p, q, g, x: int):    #-> tuple[int, int]:
    Hm = bytes_to_long(SHA256.new(msg).digest())
    k = random.randint(1, q-1) 
    
    r = pow(g, k, p) % q
    s = (pow(k, -1, q) * (Hm + x * r)) % q
    
    return (r, s)

 
def verify(msg: bytes, p, q, g, y, r, s: int) -> bool:
    Hm = bytes_to_long(SHA256.new(msg).digest())
    if not (r > 0 and r < q):
        return False

    if not(s > 0 and s < q):
        return False
    
    w = pow(s, -1, q)
    u1 = (Hm * w) % q
    u2 = (r * w) % q
    v = ((pow(g, u1, p) * pow(y, u2, p)) % p) % q

    if v == r:
        return True
    
    return False

def main():
    p, q, g = generate_key(1024) 
    assert(((p-1) % q) == 0)
    x = random.randint(1, q-1)
    y = pow(g, x, p) 
    
    file_name = input("Please input file name: ")
    try:
       f = open(file_name, 'rb')
       data = f.read()
       f.close()

       r, s = sign(data, p, q, g, x)

       if verify(data, p, q, g, y, r, s) != True:
           print("data not equal")
           return
       
       print("The parameter output: ")
       print(f"p: {p}")
       print(f"q: {q}")
       print(f"g: {g}")
       print(f"x: {x}")
       print(f"y: {y}")
       
       print("The signature output: ")
       print(f"r: {r}")
       print(f"s: {s}")
    except FileNotFoundError:
        print("File not found")


if __name__ == "__main__":
    main()
