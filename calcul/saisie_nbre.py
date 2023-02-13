# -*- coding: utf-8 -*-
"""
Created on Tue Dec 13 17:35:26 2022

@author: oscar.chateauneuf
"""

from math import *
from math import sqrt

def nombre_saisie():
    entier=int(input("Saisir la valeur d'un entier ?"))
    #inter=[1,2,3,4,5,6,7,8,9,10]
    #inter=list(range(1,10))

    while not(1 <= entier <= 10):
        print("\nValeur saisie :%d", entier)
        break
  

nombre_saisie()