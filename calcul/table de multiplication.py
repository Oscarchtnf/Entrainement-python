# -*- coding: utf-8 -*-
"""
Created on Tue Jan 10 17:27:09 2023

@author: oscar.chateauneuf
"""

for n in range(1,10):
    #insert separator
    print("--------------------------------------")
    print("la table de multiplication de  : ", n," est :")
    for i in range(1,10):
        print(i , " x ", n, " = ",i*n)
