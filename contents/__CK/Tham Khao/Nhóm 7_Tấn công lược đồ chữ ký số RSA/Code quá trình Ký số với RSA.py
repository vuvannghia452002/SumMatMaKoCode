
import random
import time
import math
from hashlib import sha256


def coprime(a, b):
    while b != 0:
        a, b = b, a % b
    return a
    
    
def extended_gcd(a, b):
    if a == 0 :  
        return b, 0, 1
             
    gcd,x1,y1 = extended_gcd(b%a, a) 
     
    x = y1 - (b//a) * x1 
    y = x1 
     
    return gcd,x,y

#Thuật toán Euclid mở rộng  
def modinv(a, m):
	g, x, y = extended_gcd(a, m)
	if g != 1:
		raise Exception('Nghịch đảo mod không tồn tại')
	return x % m    

        
def is_prime(num):
    if num == 2:
        return True
    if num < 2 or num % 2 == 0:
        return False
    for n in range(3, int(num**0.5)+2, 2):
        if num % n == 0:
            return False
    return True
    
def hashFunction(message):
  hashed = sha256(message.encode("UTF-8")).hexdigest()
  return hashed

def generate_keypair(p, q):
    if not (is_prime(p) and is_prime(q)):
        raise ValueError('Cả 2 số p và q đều phải là số nguyên tố.')
    elif p == q:
        raise ValueError('2 số p và q phải khác nhau')

    N = p * q
    phi = (p-1) * (q-1)

    #Chọn số nguyên e sao cho e and phi(n) là 2 số nguyên tố cùng nhau
    e = random.randrange(1, phi)
    g = coprime(e, phi)
    while g != 1:
        e = random.randrange(1, phi)
        g = coprime(e, phi)
    #Sử dụng thuật toán Euclid mở rộng tìm d để tạo khóa Private
    d = modinv(e, phi)
    #Return khóa public và khóa Private
    return ((N, e), (N, d))

p = int(input("Hãy nhập một số nguyên tố (17, 19, 23, v.vv...): "))
q = int(input("Hãy nhập một số nguyên tố khác (Không phải số đầu tiên): "))   

print()
print("Bắt đầu tạo khóa Public và Private . . .")

public, private = generate_keypair(p, q)
print("Khóa Public là: ", public ,"\nKhóa Private là: ", private)

def encrypt(privatek, mabam_h):
    N, key = privatek

    #Chuyển đổi từng chữ cái trong bản rõ thành các số dựa trên bảng mã Unicode
    #và mã hóa bằng công thức s =  h ^ d mod N
            
    numberRepr = [ord(char) for char in mabam_h]
    print("Biểu diễn số của tin nhắn đã băm qua bản mã Unicode trước khi mã hóa: ")
    print(numberRepr)
    chukyso_s = [pow(ord(char),key,N) for char in mabam_h]
    
    #Return the array of bytes
    return chukyso_s

message = 'Lớp Toán tin K63'
print("Tin nhắn cần gửi: ", message)
print()
print("Bắt đầu mã hóa tin nhắn với khóa bí mật ", private ," . . .")
mabam_h = hashFunction(message)
print("Tin nhắn sau được băm:", mabam_h)
chukyso_s = encrypt(private, mabam_h)
print("Chữ ký số sau khi đã được mã hóa bằng công thức s =  h ^ {} mod {}:".format(private[1], private[0]))
print(chukyso_s)

def decrypt(publick, received_sign):
    n, key = publick
       
    #sinh ra mã băm dựa trên chũ ký số 
    numberRepr = [pow(char, key, n) for char in received_sign]
    mabam_h = [chr(pow(char, key, n)) for char in received_sign]

    print("Biểu diễn số của mã băm được giải mã từ chữ ký số s được gửi tới: ")
    print(numberRepr)
    
    return ''.join(mabam_h)
  
def verify(receivedHashed, receivedmessage):
  ourHashed = hashFunction(receivedmessage)
  print("Mã băm của tin nhắn nhận được: ", ourHashed)
  if receivedHashed == ourHashed:
      print("Xác thực thành công: ", )
      print(receivedHashed, " = ", ourHashed)
  else:
      
      print("Xác thực thất bại: ")
      print(receivedHashed, " != ", ourHashed)
      
receivedmessage = 'Lớp Toán tin K64'
received_sign = chukyso_s
print("Tin nhắn nhận được là: ", receivedmessage)
print("Chữ/ kí số nhận được là: ")
print(received_sign)
print()
receivedHashed = decrypt(public, received_sign)
print("Mã băm xong khi giải mã chữ ký số: ", receivedHashed)
print()
print("Bắt đầu xác thực . . .")
verify(receivedHashed, receivedmessage)