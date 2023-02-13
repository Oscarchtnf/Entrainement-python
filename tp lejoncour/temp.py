# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
from math import *
from math import sqrt

print("quelle est votre nom ?")

nom=input()
print("bonjour", nom)
print(len(nom))
#-----------------------------------
x=nom[0] #pêrmet d'afficher le premier caractere de la variable x
y=nom[2:6]#pêrmet d'afficher seulement les caractere entre a et b 
print(x,y)

#-----------------------------------

k=1
var = 2*k
print("pour k=%d, sin(2k)=%.3f"%(k,sin(var)))

#-----------------------------------

liste1=[1,6,78,42,5]
liste2=['jour', 27, 'lundi', 1]
liste3=[]
print(len(liste1))
print(len(liste2))
print(len(liste3))

sousliste1=liste1[2:4]
print(sousliste1) #afficher la tranche du 2eme element inclus au 4eme inclus de liste 1

n=10
liste4=n*[15]
print(liste4)

#-----------------------------------
#concatenation de la liste 1 et 2
print("liste1 est egale a {} et liste 2 est egale a {}".format(liste1, liste2))
print(f"bonjour {nom} j'ai une liste de nbr{liste1} Cette variable est de type{type(liste1)}")

#-----------------------------------
#ajouter un élément dans une liste
liste2.append('mois')
print(liste2)
#insérer un élément dans une liste a une position précise
liste1.insert(3,18)#mettre 18 apres le 3eme nombre
print(liste1)
#supprimer un élément dans une liste 
liste1.remove(18)
print(liste1)

#---------------------------------------------------------
#---------------------------------------------------------
#----------------|TP   2| boucle etc..--------------------------
#----------------|Exemple 1--------------------------
print("\n ndonner un nombre :")#affiche la demande
x=float(input("x ?"))#x prend la valeur du nombre envoyé

if x>=0:#si x est superieur ou égale a 0 ,faire les instructions suivantes
    y=sqrt(x)#y est egale a la racine carré de x
    print("La racine de {:.2f} est {:.3f}".format(x, y))
else:
    print("On ne peux pas prendre la racine d'un nombre réel")

print("Au revoir")

#----------------|Exemple 2--------------------------
print("\n Quelle age avez vous ?")#affiche la demande
a=int(input("a = "))#a prend la valeur entiere du nombre entier donné

if a<18:#si vous avez au dessus de 18 ans, faire les instructions suivantes
    print("Votre place de cinéma coute 4euros")
elif a>=18 and a<25:#Si vous avez enytre 18 et 25 ans faire les instructions suivantes
    print("Votre place de cnéma coute 5euros")
else:#sinon faire les instructions suivantes
    print("Votre place de cinéma coute 7euros")

#----------------|Exemple 3--------------------------

p_seuil=2.3 #p_seuil prend la valeur de 2.3
v_seuil=7.41 #v_seuil prend la valeur de 7.41
print("\nSeuil pression : {} bars \nSeuil volume :{} cm3\n".format(p_seuil, v_seuil))#remplace {} par les variable donné

pression = float(input("Pression courante : "))#pression prend la valeur float du nombre rentrée
volume = float(input("Volulme courant : "))

if (pression > p_seuil) and (volume > v_seuil):#si la pression et le volume sont superieur au valeur courante faire l'instruction suivante
    print("Pression ET volume trop élevés. Stoppez !")
elif pression > p_seuil :#Si la pression et suprerieur au seuil
    print("Il faut diminuer la pression avant d'augmenter le volume")
elif volume > v_seuil :#Si volume est superieur au seuil pression
    print("Vous devez diminuer le volume")
else:#sinon faire les instructions suivantes
    print("Tout va bien !")

#----------------|Exemple 4--------------------------


a=0 #a prend la valeur de 0
b=10 #b prend la valeur de 10
while a < b:#tant que "a" < "a" b incrémenter de 1 la valeur a 
    print(a, end="")
    a = a + 1

print("\n\nAutre exploitation :")

while b:#tant que b
    b = b - 1
    if b % 2 !=0:#si rest eun nbr different de 0 il affiche la valeur b 
        print(b,end="")   
print()


