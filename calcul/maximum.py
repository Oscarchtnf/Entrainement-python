# -*- coding: utf-8 -*-
"""
Created on Mon Dec 19 21:01:28 2022

@author: oscar
"""

from math import *
from math import sqrt


listes=[10,19,3,1,5,8,18,16,6,7,4,11,2,14,17,12,20,13,9,15]


Maxval = None
for num in listes:
    if (Maxval is None or num > Maxval):
        Maxval = num

print("Valeur maximum :", Maxval)
#-------------------ou----------------
print("la valeur max est de :", max(listes))