# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import random

############
### Init ###
############

liste_nom = ["prout","Ralouf", "Bastoche", "Ben", "Mauger", "Clem", "Dédé", "Lulu","Val"]
short_liste = [1,3,4,5,6,7,8]
k = 0 
nb_tirage = 1000000
result = []

######################
### Tirage au sort ###
######################

short_liste = [1,2,3,4,5,6,7,8]
jade = 1
bastien = 2
ben = 3
mauger = 4
clem = 5
andrea = 6
lulu = 7
val = 8

for k in range(0, nb_tirage):
 
    while (andrea==6 or andrea==2 or andrea==1):
        andrea = random.randint(1,8)
    short_liste.remove(andrea)
            
    while (jade==1 or jade==6 or jade==4 or jade == andrea):
        jade = random.randint(1,8)
    short_liste.remove(jade)
        
    while (ben==3 or ben==4 or ben==5 or ben ==andrea or ben==jade):
        ben = random.randint(1,8)
    short_liste.remove(ben)
            
    while (mauger==4 or mauger==1 or mauger==3 or mauger==andrea or mauger==jade or mauger==ben):
        mauger =random.randint(1,8)
        #print(mauger)
    short_liste.remove(mauger)

    while (val ==8 or val ==7 or val ==ben or val==jade or val==andrea or val==mauger):
        val =random.randint(1,8)
    short_liste.remove(val)
            
    while (lulu==7 or lulu==8 or lulu ==andrea or lulu==jade or lulu==ben or lulu==val or lulu==mauger):
        lulu =random.randint(1,8)
    short_liste.remove(lulu)
    

    while short_liste ==[2, 6] or short_liste ==[3,5]:
        short_liste.append(lulu)
        lulu = 7
        
        while (lulu==7 or lulu==8 or lulu ==andrea or lulu==jade or lulu==ben or lulu==val or lulu==mauger):
            lulu =random.randint(1,8)
        short_liste.remove(lulu)
        
            
    while (clem==5 or clem==3 or clem ==andrea or clem==jade or clem==ben or clem==val or clem==mauger or clem==lulu):
        clem =random.randint(1,8)
    short_liste.remove(clem)
    

    while short_liste ==[6] or short_liste ==[2]:
        short_liste.append(clem)
        clem = 5
        while (clem==5 or clem==3 or clem ==andrea or clem==jade or clem==ben or clem==val or clem==mauger or clem==lulu):
            clem =random.randint(1,8)
        short_liste.remove(clem)
        
                                              
    while (bastien==6 or bastien==2 or bastien ==andrea or bastien==jade or bastien==ben or bastien==val or bastien==mauger or bastien==clem or bastien ==lulu):
        bastien =random.randint(1,8)
    
    result.append([jade, bastien, ben, mauger, clem, andrea, lulu, val])
    short_liste = [1,2,3,4,5,6,7,8]
    jade = 1
    bastien = 2
    ben = 3
    mauger = 4
    clem = 5
    andrea = 6
    lulu = 7
    val = 8
    
###########################    
### Affichage résultats ###
###########################

liste_variable_elu = result[random.randint(0, len(result))]
for i in range(1,9):
    print(liste_nom[i] +" offre un cadeau à "+liste_nom[liste_variable_elu[i-1]])
    

print("\n")

#############
### Proba ###
#############

jade = 1
bastien = 2
ben = 3
mauger = 4
clem = 5
andrea = 6
lulu = 7
val = 8
liste_proba = [jade, bastien, ben, mauger, clem, andrea, lulu, val]


#for prenom in liste_proba:
prenom=andrea

tirage=[]
compteur = 0
for i in result:
    tirage.append(i[prenom-1])

for nom in liste_proba:
    compteur = 0
    for i in tirage:
        if i ==nom:
            compteur +=1
    print(liste_nom[prenom]+" tire "+ liste_nom[nom] +" dans "+ str(compteur/len(result)*100)+"% des cas")
            






