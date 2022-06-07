# -*- coding: utf-8 -*-
"""
Created on Tue Jun  7 21:53:35 2022

@author: MD MOSSADEK TOUHID
"""

import random
a = random.randint(3,7543)
print(a)
alpha = 2
p = 733331
beta  = pow(alpha,a,p)


x  =  234

y1  =pow(alpha,11,p)
y2 = (x*pow(beta,11,p))%p



dec = (y2*(pow(y1,-a,p)))%p


print("origina message: ", x)
print("encryption message: ", y1,"  ", y2)
print("decryption message:", dec)