# -*- coding: utf-8 -*-
"""
Created on Tue May 17 20:05:41 2022

@author: MD MOSSADEK TOUHID
"""

import math

message = 95

p = 73
q = 89

e = 6

n = p*q
phi = (p-1)*(q-1)

while True:
    if math.gcd(e,phi) == 1:
        break
    else:
        e = e+1
 
print("Original Message: ", message)
e_text = math.pow(message,e)
cipher = int(e_text % n)
print("Encrypted Message: ", cipher)



d_key = 2


while True:
    temp = message ** (d_key*e)
    temp = temp % n
    if temp == message:
        print("decrypt key d: ", d_key)
        print("Original Message: ", temp)
        break
    d_key += 1