# -*- coding: utf-8 -*-
"""
Created on Wed Dec 21 14:11:56 2022

@author: Basti
"""

import smtplib, ssl
from email.mime.text import MIMEText


import random
import numpy as np





##################################
### Fonction de tirage au sort ###
##################################
def tirage():
    liste_tirages=[]
    nb_tirage=10
    compteur=1
    while compteur<nb_tirage:
        liste_nom = ["Jadoune", "Bastoche", "Ben", "Mauger", "Clem", "Dédé", "Lulu","Val"]
        L = liste_nom
    
        k=0
    
        while (L[0]== "Dédé" or L[0]=="Jadoune" or L[0]=="Mauger") or (L[1]=="Bastoche" or L[1]=="Dédé") or (L[2]=="Ben" or L[2]=="Clem" or L[2]=="Mauger") or (L[3]=="Mauger" or L[3]=="Ben" or L[3]=="Jadoune") or (L[4]== "Clem" or L[4]=="Ben" ) or (L[5]== "Bastoche" or L[5]=="Dédé" or L[5]=="Jadoune") or (L[6]== "Lulu" or L[6]== "Val") or (L[7]=="Lulu" or L[7]=="Val") or np.unique(L).size !=len(L):
            L=[]
            for i in range(0,len(liste_nom)):
                L.append(random.choice(liste_nom))
            k+=1
            #print(k)
        liste_tirages.append(L)
        compteur+=1
    liste_variable_elu = liste_tirages[random.randint(0, len(liste_tirages)-1)]
    return(liste_variable_elu)



#########################
### Init mail d'envoi ###
#########################

port = 465
user = 'tirage.au.sort.hiver2023@laposte.net'
password = 'Tirageausort1!'
sender = 'tirage.au.sort.hiver2023@laposte.net'



# liste_mail = ['bastienalgrenier@gmail.com','bastienalgrenier@gmail.com','bastienalgrenier@gmail.com',
#               'bastienalgrenier@gmail.com', 'bastienalgrenier@gmail.com','bastienalgrenier@gmail.com',
#               'bastienalgrenier@gmail.com', 'bastienalgrenier@gmail.com']

##liste des adresses mails respectant l'ordre :
## de la liste liste_nom = ["Jadoune", "Bastoche", "Ben", "Mauger", "Clem", "Dédé", "Lulu","Val"]

## Liste des mails officiels
liste_mail = ['jade.cachard@live.fr', 'bastienalgrenier@gmail.com',
'benjamin.mauger@outlook.fr', 'mauger.ant@gmail.com', 'clem.carn@wanadoo.fr',
'andrea.cachard@live.fr', 'lulu.lambert98@gmail.com', 'valentinlechartier@yahoo.fr']

liste_prenom = ["Jadoune", "Bastoche", "Ben", "Mauger", "Clem", "Dédé", "Lulu","Val"]

    
#########################################
### Tirage au sort et envoi des mails ###
#########################################



liste_tirage= tirage()

##pour tester avec un seul envoi de mail décommenter cette ligne 
# liste_mail=['andrea.cachard@live.fr']
# liste_tirage = ['osef']
# liste_prenom=['beuteu']

dico_tirage = {'adresse_mail':liste_mail, 'personne_tire':liste_tirage,'id':liste_prenom}

for indice in range(0,len(dico_tirage['adresse_mail'])):
    receivers=[dico_tirage['adresse_mail'][indice]]
    msg = MIMEText('Bonjour à toi '+dico_tirage['id'][indice]+',\nJe suis iNès, une IA créée à partir d\'Inès Cachard.\nJe viens d\'effectuer le tirage au sort pour le père Noël secret. Tu devras offrir un cadeau à '+dico_tirage['personne_tire'][indice]+'.\nBonne journée,\niNès')

    msg['Subject'] = 'Tirage au sort hiver 2023'
    msg['From'] = 'tirage.au.sort.hiver2023@laposte.net'
    msg['To'] = dico_tirage['adresse_mail'][indice]
    context = ssl.create_default_context()

    with smtplib.SMTP_SSL("smtp.laposte.net", port, context=context) as server:

        server.login(user, password)
        server.sendmail(sender, receivers, msg.as_string())
        print('mail successfully sent')





#############################
### ENVOI DU MAIL SECOURS ###  
#############################
msg_str = "Tirage officiel \n \n"

for indice in range(0,len(dico_tirage['adresse_mail'])):
    receivers=['inescachar@gmail.com']
    msg_str += 'Bonjour à toi '+dico_tirage['id'][indice]+',\nJe suis iNès, une IA créée à partir d\'Inès Cachard.\nJe viens d\'effectuer le tirage au sort pour le père Noël secret. Tu devras offrir un cadeau à '+dico_tirage['personne_tire'][indice]+'.\nBonne journée,\niNès \n \n'

msg = MIMEText(msg_str)
msg['Subject'] = 'Tirage au sort hiver 2023 - Mail de secours'
msg['From'] = 'tirage.au.sort.hiver2023@laposte.net'
msg['To'] = 'inescachar@gmail.com'  #mettre l'adresse mail d'Inès inescachar@gmail.com
context = ssl.create_default_context()

with smtplib.SMTP_SSL("smtp.laposte.net", port, context=context) as server:

    server.login(user, password)
    server.sendmail(sender, receivers, msg.as_string())
    print('mail de secours successfully sent')
     







        
liste_tirage = 'secret_defense'



   


     
        
##################################################
### Comment envoyer un mail à partir de python ###
##################################################

# import smtplib, ssl
# from email.mime.text import MIMEText

# sender = 'admin@example.com'
# receivers = ['info@example.com']

# port = 465
# user = 'admin@example.com'
# password = 'password'

# msg = MIMEText('This is test mail')

# msg['Subject'] = 'Test mail'
# msg['From'] = 'admin@example.com'
# msg['To'] = 'info@example.com'

# context = ssl.create_default_context()

# with smtplib.SMTP_SSL("smtp.websupport.sk", port, context=context) as server:

#     server.login(user, password)
#     server.sendmail(sender, receivers, msg.as_string())
#     print('mail successfully sent')

##merci https://zetcode.com/python/smtplib/
