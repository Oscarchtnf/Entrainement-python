
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 10 17:22:22 2023

@author: oscar.chateauneuf
"""

# -*- coding: utf-8 -*-
class CompteBancaire:
    def __init__(self, idNumber, nomPrenom, solde):
        self.idNumber = idNumber
        self.nomPrenom = nomPrenom
        self.solde = solde
        
    def versement(self, argent):
        self.solde = self.solde + argent
    
    def retrait(self, argent):
        if(self.solde < argent):
            print(" Impossible d'effectuer l'opération. Solde insuffisant !")
        else:
            self.solde = self.solde - argent
    
    def agios(self):
        self.solde =self.solde*95/100
    
    def afficher(self):
        print("Compte numéro : " , self.idNumber)
        print("Nom & Prénom : ", self.nomPrenom)
        print(" Solde  : ", self.solde , " euros ")
        print("Sauf erreur ou omisssion ! ")
        
monCompte = CompteBancaire(111111111, " oscar chateauneuf", 10000)
monCompte.versement(1500)
monCompte.retrait(5000)
#monCompte.agios()
monCompte.afficher()