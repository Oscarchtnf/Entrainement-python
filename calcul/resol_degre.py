# -*- coding: utf-8 -*-
"""
Created on Tue Dec 13 16:32:58 2022

@author: oscar.chateauneuf
"""

from math import *
from math import sqrt


def discriminant():
    a = float(input('Donner la valeur de a ?'))
    b = float(input('Donner la valeur de b ?'))
    c = float(input('Donner la valeur de c ?'))
    discriminant = (b*b) + (4*a*c)
    print("Le discriminant est de :", discriminant)
    
    
    if discriminant > 0 :
        x1=float((-b-sqrt(discriminant))/(2*a))
        x2=float((-b+sqrt(discriminant))/(2*a))
        print("Alors l'équation admet 2 solutions réel notés x1=%s et x2=%s"%(x1, x2))

    elif discriminant < 0 :
        print("Alors l'équation admet aucune solution")
   
    else :
        x0=float(-b/(2*a))
        print("Alors l'équation admet 1 solutions réel notés x0=%s"%(x0))
        
        

discriminant()
