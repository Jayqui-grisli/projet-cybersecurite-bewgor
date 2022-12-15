import helper as h
import functions as f
import os
import numpy as np
import shufflerModule as sm


#Interaction utilisateur

nom_sortie=input("Entrez le nom du fichier à générer \n")
permut=input("Entrez le nombre de permuation (3 par défault)\n /!\ Au delà de 5, vous risquez de mourrir avant la fin de l'exéctution du programme /!\ \n")
if nom_sortie=='':
    nom_sortie='default'
if permut=='':
    permut=3
else :
    permut = int(permut)
filepath_sortie = "./sorties_txt/" + nom_sortie + ".txt"


#Lecture du fichier de configuration

conf=h.readConfig() #Lecturee du fichier de configuration
ldicos=[]
for dico in conf: #Récupération des noms des txts
    ldicos.append(dico["name"])

#Traitement des dictionnaires

dictionnaires=[]

for dic in ldicos :
    c_dico=h.readTXT(dic) #Parsing du txt
    new_dico=[c_dico]
    for d in conf :
        if d["name"]==dic:
            list_fonctions = d["functions"] #Récupération de la liste des fonctions pour ce dictionnaire
            dic_fonctions = {}
            for dicf in list_fonctions:
                dic_fonctions.update(dicf) #Transformation en dictionnaires

            if dic_fonctions['initiale']: #Traitement par chaque fonction
                new_dico.append(f.initiale(c_dico))
            if dic_fonctions['mixedUpper']: #Traitement par chaque fonction
                new_dico.append(f.mixedUpper(c_dico))

    new_dico_merged=h.merger(new_dico) #Fusion des listes du txt en cours de traitement
    dictionnaires.append(new_dico_merged) #Ajout des mots traités.




#Création du dictionnaire général


dictionnaire_g=h.merger(dictionnaires)

#Génération de la liste de mots de passe par permutation

generated=dictionnaire_g
#generated=sm.shuffle(dictionnaire_g,permut)

#Création du txt

if os.path.isfile(filepath_sortie) :
    os.remove(filepath_sortie)
dico_genere = open(filepath_sortie,"x")
for word in dictionnaire_g :
    dico_genere.write(word)
    dico_genere.write("\n")
dico_genere.close()