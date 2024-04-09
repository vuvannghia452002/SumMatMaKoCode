from Crypto.PublicKey import ElGamal
from Crypto import Random
import Crypto.Random.random

#thiet lap cac gia tri nguyen to
def kronecker(x,p):
    q = (p-1)/2
    return pow(x,q,p)

def findQNR(p):
    r = Crypto.Random.random.randrange(2,p-1)
    while kronecker(r,p) == 1:
        r = Crypto.Random.random.randrange(2,p-1)
    return r

def findQR(p):
    r = Crypto.Random.random.randrange(2,p-1) 
    return pow(r,2,p)

#su dung so nguyen to 512 bit
key = ElGamal.generate(512, Random.new().read)

wrong = 0
runs = 1000
#phuong phap vet can
for i in xrange(runs):

    plaintexts = dict()
    plaintexts[0] = findQNR(key.p)
    plaintexts[1] = findQR(key.p)

    challenge_bit = Crypto.Random.random.randrange(0,2)
    r =  Crypto.Random.random.randrange(1,key.p-1) 
    challenge = key.encrypt(plaintexts[challenge_bit], r)

    output = -1
    if (kronecker(key.y, key.p) == 1) or (kronecker(challenge[0], key.p) == 1):
        if kronecker(challenge[1], key.p) == 1:
            output = 1
        else:
            output = 0
    else:
        if kronecker(challenge[1], key.p) == 1:
            output = 0
        else:
            output = 1

    if output != challenge_bit:
        wrong = wrong + 1

print("so laln thu:", wrong)
print("khoa bi mat:",key.p)
