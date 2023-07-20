# -*- coding: utf-8 -*-
"""
Created on Wed Dec 21 13:06:07 2022

@author: Basti
"""

import random
import numpy as np


############
### Init ###
############

liste_tirages=[]
nb_tirage=10
compteur=1



######################
### Tirage au sort ###
######################

while compteur<nb_tirage:
    liste_nom = ["Ralouf", "Bastoche", "Ben", "Mauger", "Clem", "Dédé", "Lulu","Val"]
    L = liste_nom

    k=0

    while (L[0]== "Dédé" or L[0]=="Ralouf" or L[0]=="Mauger") or (L[1]=="Bastoche" or L[1]=="Dédé") or (L[2]=="Ben" or L[2]=="Clem" or L[2]=="Mauger") or (L[3]=="Mauger" or L[3]=="Ben" or L[3]=="Ralouf") or (L[4]== "Clem" or L[4]=="Ben" ) or (L[5]== "Bastoche" or L[5]=="Dédé" or L[5]=="Ralouf") or (L[6]== "Lulu" or L[6]== "Val") or (L[7]=="Lulu" or L[7]=="Val") or np.unique(L).size !=len(L):
        L=[]
        for i in range(0,len(liste_nom)):
            L.append(random.choice(liste_nom))
        k+=1
        #print(k)
    liste_tirages.append(L)
    compteur+=1




###########################    
### Affichage résultats ###
###########################


liste_variable_elu = liste_tirages[random.randint(0, len(liste_tirages)-1)]
for i in range(0,len(liste_nom)):
    print(liste_nom[i] +" offre un cadeau à "+liste_variable_elu[i])

print("\n")
#############
### Proba ###
#############

jade = 0
bastien = 1
ben = 2
mauger = 3
clem = 4
andrea = 5
lulu = 6
val = 7
liste_proba = [jade, bastien, ben, mauger, clem, andrea, lulu, val]




#sujet=andrea
for sujet in liste_proba:

    tirage=[]
    compteur_1 = 0
    for i in liste_tirages:
        tirage.append(i[sujet])

    for nom in liste_nom:
        compteur_1 = 0
        for i in tirage:
            if i ==nom:
                compteur_1 +=1
        print(liste_nom[sujet]+" tire "+ nom +" dans "+ str(compteur_1/len(liste_tirages)*100)+"% des cas")
    print("\n")
    
