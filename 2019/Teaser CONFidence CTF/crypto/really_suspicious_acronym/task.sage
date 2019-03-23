def bytes_to_long(data):
    return int(data.encode("hex"),16)

def rsa(msg,e,n):
    return pow(bytes_to_long(msg),e,n)

flag = open('flag.txt','r').read()
tmp = randint(2**1023, 2**1024)
e = 65537
p = next_prime(57005*tmp+randint(2, 2**500))
q = next_prime(48879*tmp+randint(2, 2**500))
N =  p*q
print('msg1 = '+str(rsa("You can't factor the modulus",e,N)))
print('msg2 = '+str(rsa("If you don't know the modulus!",e,N)))
print('flag = '+str(rsa(flag,e,N)))
p4{S3cur1ty_th0ru9h_0b5cur1ty_4t_i7s_fin3s7}