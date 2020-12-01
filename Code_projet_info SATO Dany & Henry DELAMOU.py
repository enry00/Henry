# -*- coding: utf-8 -*-
"""
Created on Thu Nov 19 13:41:09 2020

@author: Henry DELAMOU and Dany SATO
"""


#importation des bibliothèques pandas et matplotlib
import pandas as pd #pour gérer et analyser facilement les données
import matplotlib.pyplot as plt# pour la visualisation des données
print(" I-1 Affichage des courbes de la variable, des variables statistiques en fonction du temps et détection automatique des anomalies" )
v=int(input(' -Veuillez entrer le numéro de la variable (Ex:noise=1,temp=2, hum=3,lum=4,co2=5): '))
#lire le fichier csv du projet
Emplacement_fichier= r'C:\Users\HP\Desktop\Cours IVP1\Algo et programmation\EIVP_KM.csv'#lien pour l'emplacement du fichier
Em_f=Emplacement_fichier
#lire le fichier en choisissant la colonne date 'sent_at' comme index
df0= pd.read_csv(Em_f,sep=";",index_col='sent_at',parse_dates=True) #parse_dates=True indique que la colonne 'sent_at' est pour les dates
#Diviser le fichier en fonction des 6 capteurs
    # 1er Capteur
cap1=(df0['id']==1)
u=df0[cap1]
    # 2e Capteur
cap2=(df0['id']==2)
d=df0[cap2]
    # 3e Capteur
cap3=(df0['id']==3)
t=df0[cap3]
    # 4e Capteur
cap4=(df0['id']==4)
q=df0[cap4]
    # 5e Capteur
cap5=(df0['id']==5)
c=df0[cap5]
    # 6e Capteur
cap6=(df0['id']==6)
s=df0[cap6]
#Fonctions pour afficher les graphes de la température et les variables statistiques correspondantes pour les 6 capteurs
def cap_1t():#pour le capteur 1 ('1' indique le numéro du capteur et 't' la variable température)
    plt.figure(figsize=(20,5))# taille du graphe (x,y) avec x pour les abscisses et y pour les ordonnées
    plt.subplot(1,2,1)#Affichage dans la colonne 1 du plan
    u['temp'].plot(label='Température capteur 1',alpha=2,lw=5,ls='-.',c='red')
    #utilisation des fonctions min(), max(),std(),mean(),var(),median() de pandas pour le calcul des variables statistiques
    u['temp'].resample('h').min().plot(alpha=2,label='minimum',c='green')#resample('h') regroupe nos données par heure
    u['temp'].resample('h').max().plot(alpha=2,label='maximum')
    u['temp'].resample('h').mean().plot(lw=3,ls=':',alpha=2,label='moyenne',c='black')
    u['temp'].resample('h').median().plot(lw=2, ls='--',alpha=2,label='médiane',c='yellow')
    plt.legend()#Affichage de la légende
    plt.subplot(1,2,2)#Affichage dans la colonne 2 du plan
    u['temp'].resample('h').var().plot(lw=3, ls=':',alpha=2,label='variance')
    u['temp'].resample('h').std().plot(alpha=2,label='écart type')# std() pour le calcul de l'écart-type 
    plt.legend()#Affichage de la légende
#On procède de la manière pour les autres fonctions jouant le même rôle que cap_1t() (ligne 57-463)
def cap_2t():#pour le capteur 2
    plt.figure(figsize=(20,5))
    plt.subplot(1,2,1)#Affichage dans la colonne 1 du plan
    d['temp'].plot(label='Température capteur 2',alpha=2,lw=2,ls='-.',c='red')
    d['temp'].resample('h').min().plot(alpha=2,label='minimum')
    d['temp'].resample('h').max().plot(alpha=2,label='maximum')
    d['temp'].resample('h').mean().plot(lw=3,ls=':',alpha=2,label='moyenne',c='black')
    d['temp'].resample('h').median().plot(lw=2, ls='--',alpha=2,label='médiane',c='yellow')
    plt.legend()#Affichage de la légende
    plt.subplot(1,2,2)#Affichage dans la colonne 2 du plan
    d['temp'].resample('h').var().plot(lw=3, ls=':',alpha=2,label='variance')
    d['temp'].resample('h').std().plot(alpha=2,label='écart type')
    plt.legend()
def cap_3t():# pour le capteur 3
    plt.figure(figsize=(20,5))
    plt.subplot(1,2,1)#Affichage dans la colonne 1 du plan
    t['temp'].plot(label='Température capteur 3',alpha=2,lw=2,ls='-.',c='red')
    t['temp'].resample('h').min().plot(alpha=2,label='minimum')
    t['temp'].resample('h').max().plot(alpha=2,label='maximum')
    t['temp'].resample('h').mean().plot(lw=3,ls=':',alpha=2,label='moyenne',c='black')
    t['temp'].resample('h').median().plot(lw=2, ls='--',alpha=2,label='médiane',c='yellow')
    plt.legend()#Affichage de la légende
    plt.subplot(1,2,2)#Affichage dans la colonne 2 du plan
    t['temp'].resample('h').var().plot(lw=3, ls=':',alpha=2,label='variance')
    t['temp'].resample('h').std().plot(alpha=2,label='écart type')
    plt.legend() 
def cap_4t():
    plt.figure(figsize=(20,5))
    plt.subplot(1,2,1)#Affichage dans la colonne 1 du plan
    q['temp'].plot(label='Température capteur 4',alpha=2,lw=2,ls='-.',c='red')
    q['temp'].resample('h').min().plot(alpha=2,label='minimum')
    q['temp'].resample('h').max().plot(alpha=2,label='maximum')
    q['temp'].resample('h').mean().plot(lw=4,ls=':',alpha=2,label='moyenne',c='black')
    q['temp'].resample('h').median().plot(lw=2, ls='--',alpha=2,label='médiane',c='yellow')
    plt.legend()#Affichage de la légende
    plt.subplot(1,2,2)#Affichage dans la colonne 2 du plan
    q['temp'].resample('h').var().plot(lw=3, ls=':',alpha=2,label='variance')
    q['temp'].resample('h').std().plot(alpha=2,label='écart type')
    plt.legend()
def cap_5t():
    plt.figure(figsize=(20,5))
    plt.subplot(1,2,1)#Affichage dans la colonne 1 du plan
    c['temp'].plot(label='Température capteur 5',alpha=2,lw=2,ls='-.',c='yellow')
    c['temp'].resample('h').min().plot(alpha=2,label='minimum')
    c['temp'].resample('h').max().plot(alpha=2,label='maximum')
    c['temp'].resample('h').mean().plot(lw=3,ls=':',alpha=2,label='moyenne',c='black')
    c['temp'].resample('h').median().plot(lw=2, ls='--',alpha=2,label='médiane')
    c['2019-08-21 17:15:09+02:00':'2019-08-23 14:45:05+02:00']['temp'].plot(alpha=2, label='anomalie 2',ls=':',lw=6,c='blue')
    plt.legend()#Affichage de la légende
    plt.subplot(1,2,2)#Affichage dans la colonne 2 du plan
    c['temp'].resample('h').var().plot(lw=3, ls=':',alpha=2,label='variance')
    c['temp'].resample('h').std().plot(alpha=2,label='écart type')
    plt.legend() 
def cap_6t():
    plt.figure(figsize=(20,5))
    plt.subplot(1,2,1)#Affichage dans la colonne 1 du plan
    s['temp'].plot(label='Température capteur 6',alpha=2,lw=2,ls='-.',c='red')
    s['temp'].resample('h').min().plot(alpha=2,label='minimum')
    s['temp'].resample('h').max().plot(alpha=2,label='maximum')
    s['temp'].resample('h').mean().plot(lw=3,ls=':',alpha=2,label='moyenne',c='black')
    s['temp'].resample('h').median().plot(lw=2, ls='--',alpha=2,label='médiane',c='yellow')
    plt.legend()#Affichage de la légende
    plt.subplot(1,2,2)#Affichage dans la colonne 2 du plan
    s['temp'].resample('h').var().plot(lw=3, ls=':',alpha=2,label='variance')
    s['temp'].resample('h').std().plot(alpha=2,label='écart type')
    plt.legend()
    plt.show()
#Fonctions pour afficher les graphes du bruit et les variables statistiques correspondantes pour les 6 capteurs
def cap_1n():
    plt.figure(figsize=(20,5))
    plt.subplot(1,2,1)#Affichage dans la colonne 1 du plan
    u['noise'].plot(label='Bruit capteur 1',alpha=2,lw=2,ls='-.',c='red')
    u['noise'].resample('h').min().plot(alpha=2,label='minimum')
    u['noise'].resample('h').max().plot(alpha=2,label='maximum')
    u['noise'].resample('h').mean().plot(lw=3,ls=':',alpha=2,label='moyenne',c='black')
    u['noise'].resample('h').median().plot(lw=2, ls='--',alpha=2,label='médiane',c='yellow')
    plt.legend()#Affichage de la légende
    plt.subplot(1,2,2)#Affichage dans la colonne 2 du plan
    u['noise'].resample('h').var().plot(lw=3, ls=':',alpha=2,label='variance')
    u['noise'].resample('h').std().plot(alpha=2,label='écart type')
    plt.legend() 
def cap_2n():
    plt.figure(figsize=(20,5))
    plt.subplot(1,2,1)#Affichage dans la colonne 1 du plan
    d['noise'].plot(label='Bruit capteur 2',alpha=2,lw=2,ls='-.',c='red')
    d['noise'].resample('h').min().plot(alpha=2,label='minimum')
    d['noise'].resample('h').max().plot(alpha=2,label='maximum')
    d['noise'].resample('h').mean().plot(lw=3,ls=':',alpha=2,label='moyenne',c='black')
    d['noise'].resample('h').median().plot(lw=2, ls='--',alpha=2,label='médiane',c='yellow')
    plt.legend()#Affichage de la légende
    plt.subplot(1,2,2)#Affichage dans la colonne 2 du plan
    d['noise'].resample('h').var().plot(lw=3, ls=':',alpha=2,label='variance')
    d['noise'].resample('h').std().plot(alpha=2,label='écart type')
    plt.legend() 
def cap_3n():
    plt.figure(figsize=(20,5))
    plt.subplot(1,2,1)#Affichage dans la colonne 1 du plan
    t['noise'].plot(label='Bruit capteur 3',alpha=2,lw=2,ls='-.',c='red')
    t['noise'].resample('h').min().plot(alpha=2,label='minimum')
    t['noise'].resample('h').max().plot(alpha=2,label='maximum')
    t['noise'].resample('h').mean().plot(lw=3,ls=':',alpha=2,label='moyenne',c='black')
    t['noise'].resample('h').median().plot(lw=2, ls='--',alpha=2,label='médiane',c='yellow')
    plt.legend()#Affichage de la légende
    plt.subplot(1,2,2)#Affichage dans la colonne 2 du plan
    t['noise'].resample('h').var().plot(lw=3, ls=':',alpha=2,label='variance')
    t['noise'].resample('h').std().plot(alpha=2,label='écart type')
    plt.legend() 
def cap_4n():
    plt.figure(figsize=(20,5))
    plt.subplot(1,2,1)#Affichage dans la colonne 1 du plan
    q['noise'].plot(label='Bruit capteur 4',alpha=2,lw=2,ls='-.',c='red')
    q['noise'].resample('h').min().plot(alpha=2,label='minimum')
    q['noise'].resample('h').max().plot(alpha=2,label='maximum')
    q['noise'].resample('h').mean().plot(lw=3,ls=':',alpha=2,label='moyenne',c='black')
    q['noise'].resample('h').median().plot(lw=2, ls='--',alpha=2,label='médiane',c='yellow')
    plt.legend()#Affichage de la légende
    plt.subplot(1,2,2)#Affichage dans la colonne 2 du plan
    q['noise'].resample('h').var().plot(lw=3, ls=':',alpha=2,label='variance')
    q['noise'].resample('h').std().plot(alpha=2,label='écart type')
    plt.legend()
def cap_5n():
    plt.figure(figsize=(20,5))
    plt.subplot(1,2,1)#Affichage dans la colonne 1 du plan
    c['noise'].plot(label='Bruit capteur 5',alpha=2,lw=2,ls='-.',c='yellow')
    c['noise'].resample('h').min().plot(alpha=2,label='minimum')
    c['noise'].resample('h').max().plot(alpha=2,label='maximum')
    c['noise'].resample('h').mean().plot(lw=3,ls=':',alpha=2,label='moyenne',c='black')
    c['noise'].resample('h').median().plot(lw=2, ls='--',alpha=2,label='médiane')
    c['2019-08-21 17:15:09+02:00':'2019-08-23 14:45:05+02:00']['noise'].plot(alpha=2, label='anomalie 2',ls=':',lw=6,c='blue')
    plt.legend()#Affichage de la légende
    plt.subplot(1,2,2)#Affichage dans la colonne 2 du plan
    c['noise'].resample('h').var().plot(lw=3, ls=':',alpha=2,label='variance')
    c['noise'].resample('h').std().plot(alpha=2,label='écart type')
    plt.legend()
def cap_6n():
    plt.figure(figsize=(20,5))
    plt.subplot(1,2,1)#Affichage dans la colonne 1 du plan
    s['noise'].plot(label='Bruit capteur 6',alpha=2,lw=2,ls='-.',c='red')
    s['noise'].resample('h').min().plot(alpha=2,label='minimum')
    s['noise'].resample('h').max().plot(alpha=2,label='maximum')
    s['noise'].resample('h').mean().plot(lw=3,ls=':',alpha=2,label='moyenne',c='black')
    s['noise'].resample('h').median().plot(lw=2, ls='--',alpha=2,label='médiane',c='yellow')
    plt.legend()#Affichage de la légende
    plt.subplot(1,2,2)#Affichage dans la colonne 2 du plan
    s['noise'].resample('h').var().plot(lw=3, ls=':',alpha=2,label='variance')
    s['noise'].resample('h').std().plot(alpha=2,label='écart type')
    plt.legend()
    plt.show()    
#Fonctions pour afficher les graphes de l'humidité et les variables statistiques correspondantes pour les 6 capteurs
def cap_1h():
    plt.figure(figsize=(20,5))
    plt.subplot(1,2,1)#Affichage dans la colonne 1 du plan
    u['humidity'].plot(label='Humidité capteur 1',alpha=2,lw=2,ls='-.',c='red')
    u['humidity'].resample('h').min().plot(alpha=2,label='minimum')
    u['humidity'].resample('h').max().plot(alpha=2,label='maximum')
    u['humidity'].resample('h').mean().plot(lw=3,ls=':',alpha=2,label='moyenne',c='black')
    u['humidity'].resample('h').median().plot(lw=2, ls='--',alpha=2,label='médiane',c='yellow')
    plt.legend()#Affichage de la légende
    plt.subplot(1,2,2)#Affichage dans la colonne 2 du plan
    u['humidity'].resample('h').var().plot(lw=3, ls=':',alpha=2,label='variance')
    u['humidity'].resample('h').std().plot(alpha=2,label='écart type')
    plt.legend() 
def cap_2h():
    plt.figure(figsize=(20,5))
    plt.subplot(1,2,1)#Affichage dans la colonne 1 du plan
    d['humidity'].plot(label='Humidité capteur 2',alpha=2,lw=2,ls='-.',c='red')
    d['humidity'].resample('h').min().plot(alpha=2,label='minimum')
    d['humidity'].resample('h').max().plot(alpha=2,label='maximum')
    d['humidity'].resample('h').mean().plot(lw=3,ls=':',alpha=2,label='moyenne',c='black')
    d['humidity'].resample('h').median().plot(lw=2, ls='--',alpha=2,label='médiane',c='yellow')
    plt.legend()#Affichage de la légende
    plt.subplot(1,2,2)#Affichage dans la colonne 2 du plan
    d['humidity'].resample('h').var().plot(lw=3, ls=':',alpha=2,label='variance')
    d['humidity'].resample('h').std().plot(alpha=2,label='écart type')
    plt.legend()
def cap_3h():
    plt.figure(figsize=(20,5))
    plt.subplot(1,2,1)#Affichage dans la colonne 1 du plan
    t['humidity'].plot(label='Humidité capteur 3',alpha=2,lw=2,ls='-.',c='red')
    t['humidity'].resample('h').min().plot(alpha=2,label='minimum')
    t['humidity'].resample('h').max().plot(alpha=2,label='maximum')
    t['humidity'].resample('h').mean().plot(lw=3,ls=':',alpha=2,label='moyenne',c='black')
    t['humidity'].resample('h').median().plot(lw=2, ls='--',alpha=2,label='médiane')
    plt.legend()#Affichage de la légende
    plt.subplot(1,2,2)#Affichage dans la colonne 2 du plan
    t['humidity'].resample('h').var().plot(lw=3, ls=':',alpha=2,label='variance')
    t['humidity'].resample('h').std().plot(alpha=2,label='écart type')
    plt.legend()
def cap_4h():
    plt.figure(figsize=(20,5))
    plt.subplot(1,2,1)#Affichage dans la colonne 1 du plan
    q['humidity'].plot(label='Humidité capteur 4',alpha=2,lw=2,ls='-.',c='red')
    q['humidity'].resample('h').min().plot(alpha=2,label='minimum')
    q['humidity'].resample('h').max().plot(alpha=2,label='maximum')
    q['humidity'].resample('h').mean().plot(lw=3,ls=':',alpha=2,label='moyenne',c='black')
    q['humidity'].resample('h').median().plot(lw=2, ls='--',alpha=2,label='médiane')
    plt.legend()#Affichage de la légende
    plt.subplot(1,2,2)#Affichage dans la colonne 2 du plan
    q['humidity'].resample('h').var().plot(lw=3, ls=':',alpha=2,label='variance')
    q['humidity'].resample('h').std().plot(alpha=2,label='écart type')
    plt.legend()
def cap_5h():
    plt.figure(figsize=(20,5))
    plt.subplot(1,2,1)#Affichage dans la colonne 1 du plan
    c['humidity'].plot(label='Humidité capteur 5',alpha=2,lw=2,ls='-.',c='yellow')
    c['humidity'].resample('h').min().plot(alpha=2,label='minimum')
    c['humidity'].resample('h').max().plot(alpha=2,label='maximum')
    c['humidity'].resample('h').mean().plot(lw=3,ls=':',alpha=2,label='moyenne',c='black')
    c['humidity'].resample('h').median().plot(lw=2, ls='--',alpha=2,label='médiane')
    c['2019-08-21 17:15:09+02:00':'2019-08-23 14:45:05+02:00']['humidity'].plot(alpha=2, label='anomalie 2',ls=':',lw=6,c='blue')
    plt.legend()#Affichage de la légende
    plt.subplot(1,2,2)#Affichage dans la colonne 2 du plan
    c['humidity'].resample('h').var().plot(lw=3, ls=':',alpha=2,label='variance')
    c['humidity'].resample('h').std().plot(alpha=2,label='écart type')
    plt.legend() 
def cap_6h():
    plt.figure(figsize=(20,5))
    plt.subplot(1,2,1)#Affichage dans la colonne 1 du plan
    s['humidity'].plot(label='Humidité capteur 6',alpha=2,lw=2,ls='-.',c='red')
    s['humidity'].resample('h').min().plot(alpha=2,label='minimum')
    s['humidity'].resample('h').max().plot(alpha=2,label='maximum')
    s['humidity'].resample('h').mean().plot(lw=3,ls=':',alpha=2,label='moyenne',c='black')
    s['humidity'].resample('h').median().plot(lw=2, ls='--',alpha=2,label='médiane',c='yellow')
    plt.legend()#Affichage de la légende
    plt.subplot(1,2,2)#Affichage dans la colonne 2 du plan
    s['humidity'].resample('h').var().plot(lw=3, ls=':',alpha=2,label='variance')
    s['humidity'].resample('h').std().plot(alpha=2,label='écart type')
    plt.legend()
    plt.show()
#Fonctions pour afficher les graphes de la lulinosité pour les 6 capteurs
def cap_1l():
    plt.figure(figsize=(20,5))
    plt.subplot(1,2,1)#Affichage dans la colonne 1 du plan
    u['lum'].plot(label='Luminosité capteur 1',alpha=2,lw=2,ls='-.',c='yellow')
    u['lum'].resample('h').min().plot(alpha=2,label='minimum')
    u['lum'].resample('h').max().plot(alpha=2,label='maximum')
    u['lum'].resample('h').mean().plot(lw=3,ls=':',alpha=2,label='moyenne',c='black')
    u['lum'].resample('h').median().plot(lw=2, ls='--',alpha=2,label='médiane',c='yellow') 
    limite=u['lum'].quantile(.87)
    anomalie = u[u['lum']>limite]
    anomalie['lum'].plot(label='anomalie 1',c='red',ls='--',lw=5) 
    plt.legend()#Affichage de la légende
    plt.subplot(1,2,2)#Affichage dans la colonne 2 du plan
    u['lum'].resample('h').var().plot(lw=3, ls=':',alpha=2,label='variance')
    u['lum'].resample('h').std().plot(alpha=2,label='écart type')      
    plt.legend() 
def cap_2l():
    plt.figure(figsize=(20,5))
    plt.subplot(1,2,1)#Affichage dans la colonne 1 du plan
    d['lum'].plot(label='Luminosité capteur 2',alpha=2,lw=2,ls='-.',c='red')
    d['lum'].resample('h').min().plot(alpha=2,label='minimum')
    d['lum'].resample('h').max().plot(alpha=2,label='maximum')
    d['lum'].resample('h').mean().plot(lw=3,ls=':',alpha=2,label='moyenne',c='black')
    d['lum'].resample('h').median().plot(lw=2, ls='--',alpha=2,label='médiane',c='yellow')
    limite=d['lum'].quantile(.90)
    anomalie = d[d['lum']>limite]
    anomalie['lum'].plot(label='anomalie 1',c='red',ls='--',lw=5)
    plt.legend()#Affichage de la légende
    plt.subplot(1,2,2)#Affichage dans la colonne 2 du plan
    d['lum'].resample('h').var().plot(lw=3, ls=':',alpha=2,label='variance')
    d['lum'].resample('h').std().plot(alpha=2,label='écart type')
    plt.legend() 
def cap_3l():
    plt.figure(figsize=(20,5))
    plt.subplot(1,2,1)#Affichage dans la colonne 1 du plan
    t['lum'].plot(label='Luminosité capteur 3',alpha=2,lw=2,ls='-.',c='red')
    t['lum'].resample('h').min().plot(alpha=2,label='minimum')
    t['lum'].resample('h').max().plot(alpha=2,label='maximum')
    t['lum'].resample('h').mean().plot(lw=3,ls=':',alpha=2,label='moyenne',c='black')
    t['lum'].resample('h').median().plot(lw=2, ls='--',alpha=2,label='médiane',c='yellow')
    limite=t['lum'].quantile(.82)
    anomalie = t[t['lum']>limite]
    anomalie['lum'].plot(label='anomalie 1',c='red',ls='--',lw=5)
    plt.legend()#Affichage de la légende
    plt.subplot(1,2,2)#Affichage dans la colonne 2 du plan
    t['lum'].resample('h').var().plot(lw=3, ls=':',alpha=2,label='variance')
    t['lum'].resample('h').std().plot(alpha=2,label='écart type')
    plt.legend()
def cap_4l():
    plt.figure(figsize=(20,5))
    plt.subplot(1,2,1)#Affichage dans la colonne 1 du plan
    q['lum'].plot(label='Luminosité capteur 4',alpha=2,lw=2,ls='-.',c='red')
    q['lum'].resample('h').min().plot(alpha=2,label='minimum')
    q['lum'].resample('h').max().plot(alpha=2,label='maximum')
    q['lum'].resample('h').mean().plot(lw=3,ls=':',alpha=2,label='moyenne',c='black')
    q['lum'].resample('h').median().plot(lw=2, ls='--',alpha=2,label='médiane',c='yellow')
    limite=q['lum'].quantile(.82)
    anomalie = q[q['lum']>limite]
    anomalie['lum'].plot(label='anomalie 1',c='red',ls='--',lw=5)
    plt.legend()#Affichage de la légende
    plt.subplot(1,2,2)#Affichage dans la colonne 2 du plan
    q['lum'].resample('h').var().plot(lw=3, ls=':',alpha=2,label='variance')
    q['lum'].resample('h').std().plot(alpha=2,label='écart type')
    plt.legend() 
def cap_5l():
    plt.figure(figsize=(20,5))
    plt.subplot(1,2,1)#Affichage dans la colonne 1 du plan
    c['lum'].plot(label='Luminosité capteur 5',alpha=2,lw=2,ls='-.',c='yellow')
    c['lum'].resample('h').min().plot(alpha=2,label='minimum')
    c['lum'].resample('h').max().plot(alpha=2,label='maximum')
    c['lum'].resample('h').mean().plot(lw=3,ls=':',alpha=2,label='moyenne',c='black')
    c['2019-08-21 17:15:09+02:00':'2019-08-23 14:45:05+02:00']['lum'].plot(alpha=2, label='anomalie 2',ls=':',lw=6,c='blue')
    c['lum'].resample('h').median().plot(lw=2, ls='--',alpha=2,label='médiane')
    limite=c['lum'].quantile(.95)
    anomalie = c[c['lum']>limite]
    anomalie['lum'].plot(label='anomalie 1',c='red',ls='--',lw=5)
    c['lum']['2019-08-23 20:45:00+02:00':'2019-08-24 07:45:00+02:00'].plot(label='anomalie3 (valeurs "lum" non nulles)',c='red',ls='--',lw=5)
    c['lum']['2019-08-24 20:45:00+02:00':'2019-08-25 07:45:00+02:00'].plot(label='anomalie3 (valeurs "lum" non nulles)',c='red',ls='--',lw=5)
    plt.legend()#Affichage de la légende
    plt.subplot(1,2,2)#Affichage dans la colonne 2 du plan
    c['lum'].resample('h').var().plot(lw=3, ls=':',alpha=2,label='variance')
    c['lum'].resample('h').std().plot(alpha=2,label='écart type')
    plt.legend() 
def cap_6l():
    plt.figure(figsize=(20,5))
    plt.subplot(1,2,1)#Affichage dans la colonne 1 du plan
    s['lum'].plot(label='Luminosité capteur 6',alpha=2,lw=2,ls='-.',c='red')
    s['lum'].resample('h').min().plot(alpha=2,label='minimum')
    s['lum'].resample('h').max().plot(alpha=2,label='maximum')   
    s['lum'].resample('h').mean().plot(lw=3,ls=':',alpha=2,label='moyenne',c='black')
    s['lum'].resample('h').median().plot(lw=2, ls='--',alpha=2,label='médiane',c='yellow')
    limite=s['lum'].quantile(.85)
    anomalie = s[s['lum']>limite]
    anomalie['lum'].plot(label='anomalie 1',c='red',ls='--',lw=5)
    plt.legend()#Affichage de la légende
    plt.subplot(1,2,2)#Affichage dans la colonne 2 du plan
    s['lum'].resample('h').var().plot(lw=3, ls=':',alpha=2,label='variance')
    s['lum'].resample('h').std().plot(alpha=2,label='écart type')
    plt.legend()
    plt.show()
#Fonctions pour afficher les graphes du CO2 et les variables statistiques correspondantes pour les 6 capteurs
def cap_1c():
    plt.figure(figsize=(20,5))
    plt.subplot(1,2,1)#Affichage dans la colonne 1 du plan
    u['co2'].plot(label='CO2 capteur 1',alpha=2,lw=2,ls='-.',c='red')
    u['co2'].resample('h').min().plot(alpha=0.8,label='minimum')
    u['co2'].resample('h').max().plot(alpha=0.8,label='maximum')
    u['co2'].resample('h').mean().plot(lw=3,ls=':',alpha=2,label='moyenne',c='black')
    u['co2'].resample('h').median().plot(lw=3, ls='--',alpha=2,label='médiane',c='yellow')
    plt.legend()#Affichage de la légende
    plt.subplot(1,2,2)#Affichage dans la colonne 2 du plan
    u['co2'].resample('h').var().plot(lw=3, ls=':',alpha=2,label='variance')
    u['co2'].resample('h').std().plot(alpha=0.8,label='écart type')
    plt.legend() 
def cap_2c():
    plt.figure(figsize=(20,5))
    plt.subplot(1,2,1)#Affichage dans la colonne 1 du plan
    d['co2'].plot(label='CO2 capteur 2',alpha=2,lw=2,ls='-.',c='red')
    d['co2'].resample('h').min().plot(alpha=2,label='minimum')
    d['co2'].resample('h').max().plot(alpha=2,label='maximum')
    d['co2'].resample('h').mean().plot(lw=3,ls=':',alpha=2,label='moyenne',c='black')
    d['co2'].resample('h').median().plot(lw=2, ls='--',alpha=2,label='médiane',c='yellow')
    plt.legend()#Affichage de la légende
    plt.subplot(1,2,2)#Affichage dans la colonne 2 du plan
    d['co2'].resample('h').var().plot(lw=3, ls=':',alpha=2,label='variance')
    d['co2'].resample('h').std().plot(alpha=2,label='écart type')
    plt.legend()
def cap_3c():
    plt.figure(figsize=(20,5))
    plt.subplot(1,2,1)#Affichage dans la colonne 1 du plan
    t['co2'].plot(label='CO2 capteur 3',alpha=2,lw=2,ls='-.',c='red')
    t['co2'].resample('h').min().plot(alpha=2,label='minimum')
    t['co2'].resample('h').max().plot(alpha=2,label='maximum')
    t['co2'].resample('h').mean().plot(lw=3,ls=':',alpha=2,label='moyenne',c='black')
    t['co2'].resample('h').median().plot(lw=2, ls='--',alpha=2,label='médiane',c='yellow')
    plt.legend()#Affichage de la légende
    plt.subplot(1,2,2)#Affichage dans la colonne 2 du plan
    t['co2'].resample('h').var().plot(lw=3, ls=':',alpha=2,label='variance')
    t['co2'].resample('h').std().plot(alpha=2,label='écart type')
    plt.legend() 
def cap_4c():
    plt.figure(figsize=(20,5))
    plt.subplot(1,2,1)#Affichage dans la colonne 1 du plan
    q['co2'].plot(label='CO2 capteur 4',alpha=2,lw=2,ls='-.',c='red')
    q['co2'].resample('h').min().plot(alpha=2,label='minimum')
    q['co2'].resample('h').max().plot(alpha=2,label='maximum')
    q['co2'].resample('h').mean().plot(lw=3,ls=':',alpha=2,label='moyenne',c='black')
    q['co2'].resample('h').median().plot(lw=2, ls='--',alpha=2,label='médiane',c='yellow')
    plt.legend()#Affichage de la légende
    plt.subplot(1,2,2)#Affichage dans la colonne 2 du plan
    q['co2'].resample('h').var().plot(lw=3, ls=':',alpha=2,label='variance')
    q['co2'].resample('h').std().plot(alpha=2,label='écart type')
    plt.legend()
def cap_5c():
    plt.figure(figsize=(20,5))
    plt.subplot(1,2,1)#Affichage dans la colonne 1 du plan
    c['co2'].plot(label='CO2 capteur 5',alpha=2,lw=2,ls='-.',c='yellow')
    c['co2'].resample('h').min().plot(alpha=2,label='minimum')
    c['co2'].resample('h').max().plot(alpha=2,label='maximum')
    c['2019-08-21 17:15:09+02:00':'2019-08-23 14:45:05+02:00']['co2'].plot(alpha=2, label='anomalie 2',ls=':',lw=6,c='blue')
    c['co2'].resample('h').mean().plot(lw=3,ls=':',alpha=2,label='moyenne',c='black')
    c['co2'].resample('h').median().plot(lw=2, ls='--',alpha=2,label='médiane')
    plt.legend()#Affichage de la légende
    plt.subplot(1,2,2)#Affichage dans la colonne 2 du plan
    c['co2'].resample('h').var().plot(lw=3, ls=':',alpha=2,label='variance')
    c['co2'].resample('h').std().plot(alpha=2,label='écart type')
    plt.legend()
def cap_6c():
    plt.figure(figsize=(20,5))
    plt.subplot(1,2,1)#Affichage dans la colonne 1 du plan
    s['co2'].plot(label='CO2 capteur 6',alpha=2,lw=2,ls='-.',c='red')
    s['co2'].resample('h').min().plot(alpha=2,label='minimum')
    s['co2'].resample('h').max().plot(alpha=2,label='maximum')
    s['co2'].resample('h').mean().plot(lw=3,ls=':',alpha=2,label='moyenne',c='black')
    s['co2'].resample('h').median().plot(lw=2, ls='--',alpha=2,label='médiane',c='yellow')
    plt.legend()#Affichage de la légende
    plt.subplot(1,2,2)#Affichage dans la colonne 2 du plan
    s['co2'].resample('h').var().plot(lw=3, ls=':',alpha=2,label='variance')
    s['co2'].resample('h').std().plot(alpha=2,label='écart type')
    plt.legend()#Affichage de la légende  
    plt.show()
#Appel des fonctions qui affichent les graphes des variables et les variables statistiques correspondantes pour les 6 capteurs en fonction du chiffre entrépar l'utilisateur
if v==1:
    cap_1n()
    cap_2n()
    cap_3n()
    cap_4n()
    cap_5n()
    cap_6n()
if v==2:
    cap_1t()
    cap_2t()
    cap_3t()
    cap_4t()
    cap_5t()
    cap_6t()
if v==3:
    cap_1h()
    cap_2h()
    cap_3h()
    cap_4h()
    cap_5h()
    cap_6h()
if v==4:
    cap_1l()
    cap_2l()
    cap_3l()
    cap_4l()
    cap_5l()
    cap_6l()
if v==5:
    cap_1c()
    cap_2c()
    cap_3c()
    cap_4c()
    cap_5c()
    cap_6c()
if v<1 :#Pousser l'utilisateur à choisir les bons numéros des variables 
    print('Vous devez choisir de 1 à 5 (Ex : noise=1,temp=2, hum=3,lum=4,co2=5)')
if  v>5:
    print('Vous devez choisir de 1 à 5 (Ex : noise=1,temp=2, hum=3,lum=4,co2=5)')
#indice de corrélaton entre deux variables:       
#indice de corrélation entre le bruit et la température (1)
def ind_ca1():
    plt.figure(figsize=(15,5))
    #Affichage des deux courbes à étudier
    u['noise'].plot(label='Bruit capteur 1',alpha=2)
    u['temp'].plot(label='Température capteur 1',alpha=2) 
    #Utilisation de la fonction corr() de pandas
    ic=str(u['noise'].corr(u['temp'])) 
    print("L'indice de corrélation est :",ic)
    plt.legend()
    plt.show() 
def ind_ca2():
    plt.figure(figsize=(15,5))
    #Affichage des deux courbes à étudier
    d['noise'].plot(label='Bruit capteur 2',alpha=2)
    d['temp'].plot(label='Température capteur 2',alpha=2)
    #Utilisation de la fonction corr() de pandas
    ic=str(d['noise'].corr(d['temp']))
    print("L'indice de corrélation est :",ic)
    plt.legend()
    plt.show()   
def ind_ca3():
    plt.figure(figsize=(15,5))
    #Affichage des deux courbes à étudier
    t['noise'].plot(label='Bruit capteur 3',alpha=2)
    t['temp'].plot(label='Température capteur 3',alpha=2)
    #Utilisation de la fonction corr() de pandas
    ic=str(t['noise'].corr(t['temp']))
    print("L'indice de corrélation est :",ic)
    plt.legend()
    plt.show() 
def ind_ca4():
    plt.figure(figsize=(15,5))
    #Affichage des deux courbes à étudier
    q['noise'].plot(label='Bruit capteur 4',alpha=2)
    q['temp'].plot(label='Température capteur 4',alpha=2)
    #Utilisation de la fonction corr() de pandas
    ic=str(q['noise'].corr(q['temp']))
    print("L'indice de corrélation est :",ic)
    plt.legend()
    plt.show() 
#On procédera de la même manière pour implémenter les fonctions ci-dessous (ligne 547-1004)
def ind_ca5():
    plt.figure(figsize=(15,5))
    c['noise'].plot(label='Bruit capteur 5',alpha=2)
    c['temp'].plot(label='Température capteur 5',alpha=2)
    ic=str(c['noise'].corr(c['temp']))
    print("L'indice de corrélation est :",ic)
    plt.legend()
    plt.show() 
def ind_ca6():
    plt.figure(figsize=(15,5))
    s['noise'].plot(label='Bruit capteur 6',alpha=2)
    s['temp'].plot(label='Température capteur 6',alpha=2)
    ic=str(t['noise'].corr(t['temp']))
    print("L'indice de corrélation est :",ic)
    plt.legend()
    plt.show() 
#indice de corrélation entre le bruit et l'humidité (2)
def ind_cb1():
    plt.figure(figsize=(15,5))
    u['noise'].plot(label='Bruit capteur 1',alpha=2)
    u['humidity'].plot(label='Humidité capteur 1',alpha=2)
    ic=str(u['noise'].corr(u['humidity']))
    print("L'indice de corrélation est :",ic)
    plt.legend()
    plt.show() 
def ind_cb2():
    plt.figure(figsize=(15,5))
    d['noise'].plot(label='Bruit capteur 2',alpha=2)
    d['humidity'].plot(label='Humidité capteur 2',alpha=2)
    ic=str(d['noise'].corr(d['humidity']))
    print("L'indice de corrélation est :",ic)
    plt.legend()
    plt.show()   
def ind_cb3():
    plt.figure(figsize=(15,5))
    t['noise'].plot(label='Bruit capteur 3',alpha=2)
    t['humidity'].plot(label='Humidité capteur 3',alpha=2)
    ic=str(t['noise'].corr(t['humidity']))
    print("L'indice de corrélation est :",ic)
    plt.legend()
    plt.show() 
def ind_cb4():
    plt.figure(figsize=(15,5))
    q['noise'].plot(label='Bruit capteur 4',alpha=2)
    q['humidity'].plot(label='Humidité capteur 4',alpha=2)
    ic=str(q['noise'].corr(q['humidity']))
    print("L'indice de corrélation est :",ic)
    plt.legend()
    plt.show() 
def ind_cb5():
    plt.figure(figsize=(15,5))
    c['noise'].plot(label='Bruit capteur 5',alpha=2)
    c['humidity'].plot(label='Humidité capteur 5',alpha=2)
    ic=str(c['noise'].corr(c['humidity']))
    print("L'indice de corrélation est :",ic)
    plt.legend()
    plt.show() 
def ind_cb6():
    plt.figure(figsize=(15,5))
    s['noise'].plot(label='Bruit capteur 6',alpha=2)
    s['humidity'].plot(label='Humidité capteur 6',alpha=2)
    ic=str(t['noise'].corr(t['humidity']))
    print("L'indice de corrélation est :",ic)
    plt.legend()
    plt.show() 
#indice de corrélation entre le bruit et la luminosité (3)
def ind_cc1():
    plt.figure(figsize=(15,5))
    u['noise'].plot(label='Bruit capteur 1',alpha=2)
    u['lum'].plot(label='Luminoosité capteur 1',alpha=2)
    ic=str(u['noise'].corr(u['lum']))
    print("L'indice de corrélation est :",ic)
    plt.legend()
    plt.show() 
def ind_cc2():
    plt.figure(figsize=(15,5))
    d['noise'].plot(label='Bruit capteur 2',alpha=2)
    d['lum'].plot(label='Luminoosité capteur 2',alpha=2)
    ic=str(d['noise'].corr(d['lum']))
    print("L'indice de corrélation est :",ic)
    plt.legend()
    plt.show()   
def ind_cc3():
    plt.figure(figsize=(15,5))
    t['noise'].plot(label='Bruit capteur 3',alpha=2)
    t['lum'].plot(label='Luminoosité capteur 3',alpha=2)
    ic=str(t['noise'].corr(t['lum']))
    print("L'indice de corrélation est :",ic)
    plt.legend()
    plt.show() 
def ind_cc4():
    plt.figure(figsize=(15,5))
    q['noise'].plot(label='Bruit capteur 4',alpha=2)
    q['lum'].plot(label='Luminoosité capteur 4',alpha=2)
    ic=str(q['noise'].corr(q['lum']))
    print("L'indice de corrélation est :",ic)
    plt.legend()
    plt.show() 
def ind_cc5():
    plt.figure(figsize=(15,5))
    c['noise'].plot(label='Bruit capteur 5',alpha=2)
    c['lum'].plot(label='Luminoosité capteur 5',alpha=2)
    ic=str(c['noise'].corr(c['lum']))
    print("L'indice de corrélation est :",ic)
    plt.legend()
    plt.show() 
def ind_cc6():
    plt.figure(figsize=(15,5))
    s['noise'].plot(label='Bruit capteur 6',alpha=2)
    s['lum'].plot(label='Luminoosité capteur 6',alpha=2)
    ic=str(t['noise'].corr(t['lum']))
    print("L'indice de corrélation est :",ic)
    plt.legend()
    plt.show() 
#indice de corrélation entre le bruit et le CO2 (4)
def ind_cd1():
    plt.figure(figsize=(15,5))
    u['noise'].plot(label='Bruit capteur 1',alpha=2)
    u['co2'].plot(label='CO2 capteur 1',alpha=2)
    ic=str(u['noise'].corr(u['co2']))
    print("L'indice de corrélation est :",ic)
    plt.legend()
    plt.show() 
def ind_cd2():
    plt.figure(figsize=(15,5))
    d['noise'].plot(label='Bruit capteur 2',alpha=2)
    d['co2'].plot(label='CO2 capteur 2',alpha=2)
    ic=str(d['noise'].corr(d['co2']))
    print("L'indice de corrélation est :",ic)
    plt.legend()
    plt.show()   
def ind_cd3():
    plt.figure(figsize=(15,5))
    t['noise'].plot(label='Bruit capteur 3',alpha=2)
    t['co2'].plot(label='CO2 capteur 3',alpha=2)
    ic=str(t['noise'].corr(t['co2']))
    print("L'indice de corrélation est :",ic)
    plt.legend()
    plt.show() 
def ind_cd4():
    plt.figure(figsize=(15,5))
    q['noise'].plot(label='Bruit capteur 4',alpha=2)
    q['co2'].plot(label='CO2 capteur 4',alpha=2)
    ic=str(q['noise'].corr(q['co2']))
    print("L'indice de corrélation est :",ic)
    plt.legend()
    plt.show() 
def ind_cd5():
    plt.figure(figsize=(15,5))
    c['noise'].plot(label='Bruit capteur 5',alpha=2)
    c['co2'].plot(label='CO2 capteur 5',alpha=2)
    ic=str(c['noise'].corr(c['co2']))
    print("L'indice de corrélation est :",ic)
    plt.legend()
    plt.show() 
def ind_cd6():
    plt.figure(figsize=(15,5))
    s['noise'].plot(label='Bruit capteur 6',alpha=2)
    s['co2'].plot(label='CO2 capteur 6',alpha=2)
    ic=str(t['noise'].corr(t['co2']))
    print("L'indice de corrélation est :",ic)
    plt.legend()
    plt.show() 
 #indice de corrélation entre le CO2 et la température (5)
def ind_ce1():
    plt.figure(figsize=(15,5))
    u['co2'].plot(label='CO2 capteur 1',alpha=2)
    u['temp'].plot(label='Température capteur 1',alpha=2)
    ic=str(u['co2'].corr(u['temp']))
    print("L'indice de corrélation est :",ic)
    plt.legend()
    plt.show() 
def ind_ce2():
    plt.figure(figsize=(15,5))
    d['co2'].plot(label='CO2 capteur 2',alpha=2)
    d['temp'].plot(label='Température capteur 2',alpha=2)
    ic=str(d['co2'].corr(d['temp']))
    print("L'indice de corrélation est :",ic)
    plt.legend()
    plt.show()   
def ind_ce3():
    plt.figure(figsize=(15,5))
    t['co2'].plot(label='CO2 capteur 3',alpha=2)
    t['temp'].plot(label='Température capteur 3',alpha=2)
    ic=str(t['co2'].corr(t['temp']))
    print("L'indice de corrélation est :",ic)
    plt.legend()
    plt.show() 
def ind_ce4():
    plt.figure(figsize=(15,5))
    q['co2'].plot(label='CO2 capteur 4',alpha=2)
    q['temp'].plot(label='Température capteur 4',alpha=2)
    ic=str(q['co2'].corr(q['temp']))
    print("L'indice de corrélation est :",ic)
    plt.legend()
    plt.show() 
def ind_ce5():
    plt.figure(figsize=(15,5))
    c['co2'].plot(label='CO2 capteur 5',alpha=2)
    c['temp'].plot(label='Température capteur 5',alpha=2)
    ic=str(c['co2'].corr(c['temp']))
    print("L'indice de corrélation est :",ic)
    plt.legend()
    plt.show() 
def ind_ce6():
    plt.figure(figsize=(15,5))
    s['co2'].plot(label='CO2 capteur 6',alpha=2)
    s['temp'].plot(label='Température capteur 6',alpha=2)
    ic=str(t['co2'].corr(t['temp']))
    print("L'indice de corrélation est :",ic)
    plt.legend()
    plt.show()    
 #indice de corrélation entre la luminosité et la température (6)
def ind_cf1():
    plt.figure(figsize=(15,5))
    u['lum'].plot(label='Luminosité capteur 1',alpha=2)
    u['temp'].plot(label='Température capteur 1',alpha=2)
    ic=str(u['lum'].corr(u['temp']))
    print("L'indice de corrélation est :",ic)
    plt.legend()
    plt.show() 
def ind_cf2():
    plt.figure(figsize=(15,5))
    d['lum'].plot(label='Luminosité capteur 2',alpha=2)
    d['temp'].plot(label='Température capteur 2',alpha=2)
    ic=str(d['lum'].corr(d['temp']))
    print("L'indice de corrélation est :",ic)
    plt.legend()
    plt.show()   
def ind_cf3():
    plt.figure(figsize=(15,5))
    t['lum'].plot(label='Luminosité capteur 3',alpha=2)
    t['temp'].plot(label='Température capteur 3',alpha=2)
    ic=str(t['lum'].corr(t['temp']))
    print("L'indice de corrélation est :",ic)
    plt.legend()
    plt.show() 
def ind_cf4():
    plt.figure(figsize=(15,5))
    q['lum'].plot(label='Luminosité capteur 4',alpha=2)
    q['temp'].plot(label='Température capteur 4',alpha=2)
    ic=str(q['lum'].corr(q['temp']))
    print("L'indice de corrélation est :",ic)
    plt.legend()
    plt.show() 
def ind_cf5():
    plt.figure(figsize=(15,5))
    c['lum'].plot(label='Luminosité capteur 5',alpha=2)
    c['temp'].plot(label='Température capteur 5',alpha=2)
    ic=str(c['lum'].corr(c['temp']))
    print("L'indice de corrélation est :",ic)
    plt.legend()
    plt.show() 
def ind_cf6():
    plt.figure(figsize=(15,5))
    s['lum'].plot(label='Luminosité capteur 6',alpha=2)
    s['temp'].plot(label='Température capteur 6',alpha=2)
    ic=str(t['lum'].corr(t['temp']))
    print("L'indice de corrélation est :",ic)
    plt.legend()
    plt.show()    
#indice de corrélation entre le l'humidité et la température (7)
def ind_cg1():
    plt.figure(figsize=(15,5))
    u['humidity'].plot(label='Humidité capteur 1',alpha=2)
    u['temp'].plot(label='Température capteur 1',alpha=2)
    ic=str(u['humidity'].corr(u['temp']))
    print("L'indice de corrélation est :",ic)
    plt.legend()
    plt.show() 
def ind_cg2():
    plt.figure(figsize=(15,5))
    d['humidity'].plot(label='Humidité capteur 2',alpha=2)
    d['temp'].plot(label='Température capteur 2',alpha=2)
    ic=str(d['humidity'].corr(d['temp']))
    print("L'indice de corrélation est :",ic)
    plt.legend()
    plt.show()   
def ind_cg3():
    plt.figure(figsize=(15,5))
    t['humidity'].plot(label='Humidité capteur 3',alpha=2)
    t['temp'].plot(label='Température capteur 3',alpha=2)
    ic=str(t['humidity'].corr(t['temp']))
    print("L'indice de corrélation est :",ic)
    plt.legend()
    plt.show() 
def ind_cg4():
    plt.figure(figsize=(15,5))
    q['humidity'].plot(label='Humidité capteur 4',alpha=2)
    q['temp'].plot(label='Température capteur 4',alpha=2)
    ic=str(q['humidity'].corr(q['temp']))
    print("L'indice de corrélation est :",ic)
    plt.legend()
    plt.show() 
def ind_cg5():
    plt.figure(figsize=(15,5))
    c['humidity'].plot(label='Humidité capteur 5',alpha=2)
    c['temp'].plot(label='Température capteur 5',alpha=2)
    ic=str(c['humidity'].corr(c['temp']))
    print("L'indice de corrélation est :",ic)
    plt.legend()
    plt.show() 
def ind_cg6():
    plt.figure(figsize=(15,5))
    s['humidity'].plot(label='Humidité capteur 6',alpha=2)
    s['temp'].plot(label='Température capteur 6',alpha=2)
    ic=str(t['humidity'].corr(t['temp']))
    print("L'indice de corrélation est :",ic)
    plt.legend()
    plt.show()     
 #indice de corrélation entre l'humidité et la luminosité (8)
def ind_ch1():
    plt.figure(figsize=(15,5))
    u['humidity'].plot(label='Humidité capteur 1',alpha=2)
    u['lum'].plot(label='Luminosité capteur 1',alpha=2)
    ic=str(u['humidity'].corr(u['lum']))
    print("L'indice de corrélation est :",ic)
    plt.legend()
    plt.show() 
def ind_ch2():
    plt.figure(figsize=(15,5))
    d['humidity'].plot(label='Humidité capteur 2',alpha=2)
    d['lum'].plot(label='Luminosité capteur 2',alpha=2)
    ic=str(d['humidity'].corr(d['lum']))
    print("L'indice de corrélation est :",ic)
    plt.legend()
    plt.show()   
def ind_ch3():
    plt.figure(figsize=(15,5))
    t['humidity'].plot(label='Humidité capteur 3',alpha=2)
    t['lum'].plot(label='Luminosité capteur 3',alpha=2)
    ic=str(t['humidity'].corr(t['lum']))
    print("L'indice de corrélation est :",ic)
    plt.legend()
    plt.show() 
def ind_ch4():
    plt.figure(figsize=(15,5))
    q['humidity'].plot(label='Humidité capteur 4',alpha=2)
    q['lum'].plot(label='Luminosité capteur 4',alpha=2)
    ic=str(q['humidity'].corr(q['lum']))
    print("L'indice de corrélation est :",ic)
    plt.legend()
    plt.show() 
def ind_ch5():
    plt.figure(figsize=(15,5))
    c['humidity'].plot(label='Humidité capteur 5',alpha=2)
    c['lum'].plot(label='Luminosité capteur 5',alpha=2)
    ic=str(c['humidity'].corr(c['lum']))
    print("L'indice de corrélation est :",ic)
    plt.legend()
    plt.show() 
def ind_ch6():
    plt.figure(figsize=(15,5))
    s['humidity'].plot(label='Humidité capteur 6',alpha=2)
    s['lum'].plot(label='Luminosité capteur 6',alpha=2)
    ic=str(t['humidity'].corr(t['lum']))
    print("L'indice de corrélation est :",ic)
    plt.legend()
    plt.show()    
#indice de corrélation entre l'humidité et le CO2 (9)
def ind_ci1():
    plt.figure(figsize=(15,5))
    u['humidity'].plot(label='Humidité capteur 1',alpha=2)
    u['co2'].plot(label='CO2 capteur 1',alpha=2)
    ic=str(u['humidity'].corr(u['co2']))
    print("L'indice de corrélation est :",ic)
    plt.legend()
    plt.show() 
def ind_ci2():
    plt.figure(figsize=(15,5))
    d['humidity'].plot(label='Humidité capteur 2',alpha=2)
    d['co2'].plot(label='CO2 capteur 2',alpha=2)
    ic=str(d['humidity'].corr(d['co2']))
    print("L'indice de corrélation est :",ic)
    plt.legend()
    plt.show()   
def ind_ci3():
    plt.figure(figsize=(15,5))
    t['humidity'].plot(label='Humidité capteur 3',alpha=2)
    t['co2'].plot(label='CO2 capteur 3',alpha=2)
    ic=str(t['humidity'].corr(t['co2']))
    print("L'indice de corrélation est :",ic)
    plt.legend()
    plt.show() 
def ind_ci4():
    plt.figure(figsize=(15,5))
    q['humidity'].plot(label='Humidité capteur 4',alpha=2)
    q['co2'].plot(label='CO2 capteur 4',alpha=2)
    ic=str(q['humidity'].corr(q['co2']))
    print("L'indice de corrélation est :",ic)
    plt.legend()
    plt.show() 
def ind_ci5():
    plt.figure(figsize=(15,5))
    c['humidity'].plot(label='Humidité capteur 5',alpha=2)
    c['co2'].plot(label='CO2 capteur 5',alpha=2)
    ic=str(c['humidity'].corr(c['co2']))
    print("L'indice de corrélation est :",ic)
    plt.legend()
    plt.show() 
def ind_ci6():
    plt.figure(figsize=(15,5))
    s['humidity'].plot(label='Humidité capteur 6',alpha=2)
    s['co2'].plot(label='CO2 capteur 6',alpha=2)
    ic=str(t['humidity'].corr(t['co2']))
    print("L'indice de corrélation est :",ic)
    plt.legend()
    plt.show()     
#indice de corrélation entre la luminosité et CO2 (10)
def ind_cj1():
    plt.figure(figsize=(15,5))
    u['lum'].plot(label='Luminosité capteur 1',alpha=2)
    u['co2'].plot(label='CO2 capteur 1',alpha=2)
    ic=str(u['lum'].corr(u['co2']))
    print("L'indice de corrélation est :",ic)
    plt.legend()
    plt.show() 
def ind_cj2():
    plt.figure(figsize=(15,5))
    d['lum'].plot(label='Luminosité capteur 2',alpha=2)
    d['co2'].plot(label='CO2 capteur 2',alpha=2)
    ic=str(d['lum'].corr(d['co2']))
    print("L'indice de corrélation est :",ic)
    plt.legend()
    plt.show()   
def ind_cj3():
    plt.figure(figsize=(15,5))
    t['lum'].plot(label='Luminosité capteur 3',alpha=2)
    t['co2'].plot(label='CO2 capteur 3',alpha=2)
    ic=str(t['lum'].corr(t['co2']))
    print("L'indice de corrélation est :",ic)
    plt.legend()
    plt.show() 
def ind_cj4():
    plt.figure(figsize=(15,5))
    q['lum'].plot(label='Luminosité capteur 4',alpha=2)
    q['co2'].plot(label='CO2 capteur 4',alpha=2)
    ic=str(q['lum'].corr(q['co2']))
    print("L'indice de corrélation est :",ic)
    plt.legend()
    plt.show() 
def ind_cj5():
    plt.figure(figsize=(15,5))
    c['lum'].plot(label='Luminosité capteur 5',alpha=2)
    c['co2'].plot(label='CO2 capteur 5',alpha=2)
    ic=str(c['lum'].corr(c['co2']))
    print("L'indice de corrélation est :",ic)
    plt.legend()
    plt.show() 
def ind_cj6():
    plt.figure(figsize=(15,5))
    s['lum'].plot(label='Luminosité capteur 6',alpha=2)
    s['co2'].plot(label='CO2 capteur 6',alpha=2)
    ic=str(t['lum'].corr(t['co2']))
    print("L'indice de corrélation est :",ic)
    plt.legend()
    plt.show() 
#Appel des fonctions qui calcul l'indice de corrélation en fonction de lettre entrée par l'utilisateur
print(" I-2 Calcul de l'indice de corrélation")
idc=input(" -Choisissez vos deux variables pour calculer l'indice de corrélation  (Ex : bruit_température = a; bruit_humdité = b; bruit_luminosité = c; bruit_CO2 = d; température_CO2 = e; température_luminosité = f; température_humidité = g; huminosité_luminosité = h; huminosité_CO2 = i; luminosité_CO2 = j) :")
if idc=='a':
    ind_ca1()
    ind_ca2()
    ind_ca3()
    ind_ca4()
    ind_ca5()
    ind_ca6()
if idc=='b':
    ind_cb1()
    ind_cb2()
    ind_cb3()
    ind_cb4()
    ind_cb5()
    ind_cb6()  
if idc=='c':
    ind_cc1()
    ind_cc2()
    ind_cc3()
    ind_cc4()
    ind_cc5()
    ind_cc6()
if idc=='d':
    ind_cd1()
    ind_cd2()
    ind_cd3()
    ind_cd4()
    ind_cd5()
    ind_cd6()
if idc=='e':
    ind_ce1()
    ind_ce2()
    ind_ce3()
    ind_ce4()
    ind_ce5()
    ind_ce6()
if idc=='f':
    ind_cf1()
    ind_cf2()
    ind_cf3()
    ind_cf4()
    ind_cf5()
    ind_cf6()
if idc=='g':
    ind_cg1()
    ind_cg2()
    ind_cg3()
    ind_cg4()
    ind_cg5()
    ind_cg6()
if idc=='h':
    ind_ch1()
    ind_ch2()
    ind_ch3()
    ind_ch4()
    ind_ch5()
    ind_ch6()
if idc=='i':
    ind_ci1()
    ind_ci2()
    ind_ci3()
    ind_ci4()
    ind_ci5()
    ind_ci6()
if idc=='j':
    ind_cj1()
    ind_cj2()
    ind_cj3()
    ind_cj4()
    ind_cj5()
    ind_cj6()
#Calcul de l'indice humidex
print("I-3 Calcul de l'indice humidex")
#Envoyer l'utilisateur à entrer le numéro du capteur pour lequel il veut étudier l'indice humidex
idh=int(input(" -Entrer le numéro du capteur pour lequel vous voulez étudiez l'indice humidex (Ex : 1 pour le capteur1, 2 pour le capteur2......) :" ))
#Nous allons ajouter une colonne "Indice Humidex" à chaque dataframe correspondants aux différents capteurs   
def idh_cap1(): #fonction qui affiche les valeurs des indices humidex et la courbe humidex du capteur 1
    u['indice humidex']=u['temp']+((0.0339555556*(10**(7.5*(u['temp']/(237.7+u['temp'])))) *u['humidity'])-5.55555556) #formule indice humidex
    plt.figure(figsize=(15,5))
    u['indice humidex'].plot(label='Indice humidex capteur 1',alpha=1)#indexation de la colonne et nom de la courbe
    print(u)#affichage des valeurs des indices "humidex"
    #Affichage de la courbe de l'indice "Humide" avec la légende
    plt.legend()
    plt.show() 
def idh_cap2(): #fonction qui affiche les valeurs des indices humidex et la courbe humidex du capteur 2
    d['indice humidex']=d['temp']+((0.0339555556*(10**(7.5*(d['temp']/(237.7+d['temp'])))) *d['humidity'])-5.55555556) #formule indice humidex
    plt.figure(figsize=(15,5))
    d['indice humidex'].plot(label='Indice humidex capteur 2',alpha=1)#indexation de la colonne et nom de la courbe
    print(d)#affichage des valeurs des indices "humidex"
    #Affichage de la courbe de l'indice "Humide" avec la légende
    plt.legend()
    plt.show() 
def idh_cap3(): #fonction qui affiche les valeurs des indices humidex et la courbe humidex du capteur 3
    t['indice humidex']=t['temp']+((0.0339555556*(10**(7.5*(t['temp']/(237.7+t['temp'])))) *t['humidity'])-5.55555556) #formule indice humidex
    plt.figure(figsize=(15,5))
    t['indice humidex'].plot(label='Indice humidex capteur 3',alpha=1)
    print(t)#affichage des valeurs des indices "humidex"
    #Affichage de la courbe de l'indice "Humide" avec la légende
    plt.legend()
    plt.show() 
def idh_cap4(): #fonction qui affiche les valeurs des indices humidex et la courbe humidex du capteur 4
    q['indice humidex']=q['temp']+((0.0339555556*(10**(7.5*(q['temp']/(237.7+q['temp'])))) *q['humidity'])-5.55555556) #formule indice humidex
    plt.figure(figsize=(15,5))
    q['indice humidex'].plot(label='Indice humidex capteur 4',alpha=1)
    print(q)#affichage des valeurs des indices "humidex"
    #Affichage de la courbe de l'indice "Humide" avec la légende
    plt.legend()
    plt.show() 
def idh_cap5(): #fonction qui affiche les valeurs des indices humidex et la courbe humidex du capteur 5
    c['indice humidex']=c['temp']+((0.0339555556*(10**(7.5*(c['temp']/(237.7+c['temp'])))) *c['humidity'])-5.55555556) #formule indice humidex
    plt.figure(figsize=(15,5))
    c['indice humidex'].plot(label='Indice humidex capteur 5',alpha=1)
    print(c)
    plt.legend()
    plt.show() 
def idh_cap6(): #fonction qui affiche les valeurs des indices humidex et la courbe humidex du capteur 6
    s['indice humidex']=s['temp']+((0.0339555556*(10**(7.5*(s['temp']/(237.7+s['temp'])))) *s['humidity'])-5.55555556)  #formule indice humidex
    plt.figure(figsize=(15,5))
    s['indice humidex'].plot(label='Indice humidex capteur 6',alpha=1)
    print(s)
    plt.legend()
    plt.show() 
#Appel des fonctions qui affichent les valeurs des indices humidex et la courbe humidex en fonction du chiffre entré par l'utilisateur
if idh==1:
    idh_cap1()
if idh==2:
    idh_cap2()
if idh==3:
    idh_cap3()
if idh==4:
    idh_cap4()
if idh==5:
    idh_cap5()
if idh==6:
    idh_cap6()
if idh>6:
    print("Vous devez choisir un chiffre de 1 à 6 car on a 6 capteur")
if idh<0:  
    print("Vous devez choisir un chiffre de 1 à 6 car on a 6 capteur")
#Signification des valeurs de l'indice humidex
print("  D'après Environnement Canada, un indice humidex de :\n¤ moins de 30, aucun inconfort ;\n¤ 30 à 39, un certain inconfort ;\n¤ au-dessus de 40, beaucoup d'inconfort ;\n¤ au-dessus de 45, il y a danger : un coup de chaleur est probable ;\n¤ au-dessus de 54, un coup de chaleur est imminent.")


    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    