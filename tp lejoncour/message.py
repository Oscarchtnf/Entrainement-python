# -*- coding: utf-8 -*-
"""
Created on Tue Jan  3 16:20:15 2023

@author: oscar.chateauneuf
"""
from math import *

class Message:
    
#Constructeur avec un argument optionnel
    def __init__(self, msg=""):
        self.msg = msg
#Autre methode de la classe
    def ajouter(self, texte):
        self.msg += texte
    
    def afficher(self):
        print(self.msg)
    
    def vider(self):
        self.msg=""
    
    def longueur(self):
        return len(self.msg)
   
    def chercher(self, texte):
        if texte in self.msg:
            return self.msg.index(texte)
        return -1
            
    def inserer(self, texte, i):
        self.msg=self.msg[:i]+texte+self.msg[i:]
        
    def remplacer(self, mot1, mot2):
        while mot1!="":
            print(self.msg)
            self.msg=""
            self.msg += mot1 + mot2
            print(self.msg)
            self.msg=self.msg.replace(mot1, mot2)
            print(self.msg)
            break
        while self.msg==self.msg.replace(mot1, mot2) :
            print(len(self.msg))
            break
        return -1
    
    #def remplacer2(self, mot3, mot4):
    #    self.vider()
     #   p1=self.msg.index(mot3)
     #   p1=self.msg.index(mot3)
      #  l1=len(mot3)
       # print(p1)
        #print(l1)
      #  avant=message[:]
       # apres=message[:]
        #self.msg = avant + mot4 + apres
    
    def majuscules(self, phrase):
        list1=phrase.split(" ")
        for i in range(len(list1)):
            list1[i]=list1[i].capitalize()
        phrase=" ".join(list1)
        print(phrase)
#---------------------------ou----------------------
        #uppercase_phrase=phrase.title()
        #print(uppercase_phrase)
            
#Programme de test de la classe
if __name__ == "__main__":
    message = Message("Salut")
    message.ajouter(" les amis")
    message.afficher()
    message.longueur() 
    
    longueur=message.longueur()
    print(longueur)
    
    pos=message.chercher("les")
    print(pos)
    
    message.inserer('Je suis oscar',0)
    message.afficher()
    message.vider()
    message.afficher()
    
    message.remplacer("lacrim", "poutine")
    
   # message.remplacer2("casque", "gilet")
    
    message.majuscules("au bord de la mer")