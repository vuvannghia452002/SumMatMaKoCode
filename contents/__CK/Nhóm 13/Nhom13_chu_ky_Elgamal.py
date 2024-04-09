import random
from math import pow


a=random.randint(2,10)
#ham tim uoc chung lon nhat cua 2 so
def gcd(a,b):
    if a<b:
        return gcd(b,a)
    elif a%b==0:
        return b
    else:
        return gcd(b,a%b)


#sinh khoa
def gen_key(r):
    key= random.randint(pow(10,20),r)
    while gcd(r,key)!=1:
        key=random.randint(pow(10,20),r)
    return key


#tinh a^b mob c
def power(a,b,c):
    x=1
    y=a
    while b>0:
        if b%2==0:
            x=(x*y)%c;
        y=(y*y)%c
        b=int(b/2)
    return x%c


#Ky so
def sign(msg,q,g):
    ct=[]
    k=gen_key(q)
    s=power(k,q-3,q-1)
    p=power(g,k,q)
    for i in range(0,len(msg)):
        ct.append(msg[i])

    for i in range(0,len(ct)):
        ct[i]=q-1 - (((ord(ct[i])-q)*s)%(q-1))
    return ct,p



msg=input("Nhap thong diep:")
q=random.randint(pow(10,20),pow(10,50))
g=random.randint(2,q)
key=gen_key(q)
h=power(g,key,q)
ct,p=sign(msg,q,g)
print("Khoa bi mat=",g)
print("Khoa cong khai=",h)
print("Chu ky= (a, b)")
print("a=",p)
print("b=",ct)