# coding: utf-8
import sqlite3 #Import du module Sql
from moduleMain import *
from humain import *

conn = sqlite3.connect('languages.db') #Création du fichier BD
cursor = conn.cursor()

#Création de la table Humains
cursor.execute("""
CREATE TABLE IF NOT EXISTS Languages (
start VARCHAR(255),
continueGame VARCHAR(255),
settings VARCHAR(255),
leaveMenu VARCHAR(255),
test VARCHAR(255),
language VARCHAR(255),
close VARCHAR(255),
francais VARCHAR(255),
anglais VARCHAR(255),
temporary VARCHAR(255),
leaveGame VARCHAR(255),
check VARCHAR(255),
yes VARCHAR(255),
no VARCHAR(255)
)
""")

conn.commit()

#Création du dictionnaire contenant l'humain 1
dicoFrench = {"start" : "Nouvelle Partie"}

dicoEnglish = {"start" : "New Game"}

#print(humainDico)

#Importation de l'humain depuis le dictionnaire vers la table Humains
cursor = conn.cursor()
cursor.execute("INSERT INTO Humains(prenom, nom, age, ageV, genre, sexe, \
sexeV, taille, tailleV, poids, poidsV, ethnie, ethnieV, musculature, \
musculatureV, cheveux, cheveuxV, yeux, yeuxV, style, styleV, tolerance, \
orientPol, classeSoc, classeSocV, violence, intelligence) VALUES (:prenom, \
:nom, :age, :ageV, :genre, :sexe, :sexeV, :taille, :tailleV, :poids, :poidsV, \
:ethnie, :ethnieV, :musculature, :musculatureV, :cheveux, :cheveuxV, :yeux, \
:yeuxV, :style, :styleV, :tolerance, :orientPol, :classeSoc, :classeSocV, \
:violence, :intelligence)", humainDico)
conn.commit()



#Création du dictionnaire contenant l'humain 2
humain2Dico = {"prenom" : humain2.prenom, "nom" : humain2.nom, "age" : humain2.age, \
"ageV" : humain2.ageV, "genre" : humain2.genre, "sexe" : humain2.sexe, \
"sexeV" : humain2.sexeV, "taille" : humain2.taille, "tailleV" : humain2.tailleV, \
"poids" : humain2.poids, "poidsV" : humain2.poidsV, "ethnie" : humain2.ethnie, \
"ethnieV" : humain2.ethnieV, "musculature" : humain2.musculature, \
"musculatureV" : humain2.musculatureV, "cheveux" : humain2.cheveux, \
"cheveuxV" : humain2.cheveuxV, "yeux" : humain2.yeux, "yeuxV" : humain2.yeuxV, \
"style" : humain2.style, "styleV" : humain2.styleV, "tolerance" : humain2.tolerance, \
"orientPol" : humain2.orientPol, "classeSoc" : humain2.classeSoc, \
"classeSocV" : humain2.classeSocV, "violence" : humain2.violence, \
"intelligence" : humain2.intelligence}

#print(humain2Dico)

#Importation de l'humain 2 depuis le dictionnaire vers la table Humains
cursor = conn.cursor()
cursor.execute("INSERT INTO Humains(prenom, nom, age, ageV, genre, sexe, \
sexeV, taille, tailleV, poids, poidsV, ethnie, ethnieV, musculature, \
musculatureV, cheveux, cheveuxV, yeux, yeuxV, style, styleV, tolerance, \
orientPol, classeSoc, classeSocV, violence, intelligence) VALUES (:prenom, \
:nom, :age, :ageV, :genre, :sexe, :sexeV, :taille, :tailleV, :poids, :poidsV, \
:ethnie, :ethnieV, :musculature, :musculatureV, :cheveux, :cheveuxV, :yeux, \
:yeuxV, :style, :styleV, :tolerance, :orientPol, :classeSoc, :classeSocV, \
:violence, :intelligence)", humain2Dico)
conn.commit()
conn.close()

conn = sqlite3.connect("base.db")
cursor = conn.cursor()
cursor.execute("SELECT * FROM Humains")
resultat = cursor.fetchall()
#print(resultat)

#db.close()


