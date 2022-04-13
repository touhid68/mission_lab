import math

p = 656692050181897513638241554199181923922955921760928836766304161790553989228223793461834703506872747071705167995972707253940099469869516422893633357693
q = 204616454475328391399619135615615385636808455963116802820729927402260635621645177248364272093977747839601125961863785073671961509749189348777945177811
e = 7
message = 3472930211
print("Original Message: ", message)

n = p*q
phi_n = (p-1)*(q-1)
print("Size of n: ",len(str(n)))

#encryption key
while True:
    if math.gcd(e,phi_n) == 1:
        break
    else:
        e = e+1
        print(e)

Cipher = pow(message,e,n)
print("Encrypted Message: ", Cipher)



#decryption key
dd=pow(e,-1)
d=math.fmod(dd,phi_n)


Decrypted = pow(Cipher,d)
Decrypted=math.fmod(Decrypted,n)
#print("Decrypted Message: ", Decrypted)

print("Decrypted Message: " , math.ceil(Decrypted))