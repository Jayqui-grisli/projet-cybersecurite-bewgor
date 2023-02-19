import helper as h
import functions as f
import time
import os
import numpy as np
import shufflerModule as sm


#Interaction utilisateur
skip_gen= False
do_skip=input("Voulez vous ne pas générer et récupérer les dictionnaires intermédiaires ? Si oui, tapez Y, sinon, tapez tout autre chose \n")
if do_skip=="Y" or do_skip=="y":
    skip_gen=True

if not skip_gen :
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
alpha_cesar =['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20','21','22','23','24','25','26']
alpha_l33t =['@','ß','©','d','3','ƒ','&','#','!','ʝ','k','1','m','n','0','p','q','Я','$','7','µ','v','Ш','x','Ψ','z']
s_char = ['&','@','ù','%','$']

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
            if dic_fonctions['num_to_month']: #Traitement par chaque fonction
                new_dico.append(f.num_to_month(c_dico))
            if dic_fonctions['cesar']: #Traitement par chaque fonction
                new_dico.append(f.alternative_alphabet(c_dico,alpha_cesar))
            if dic_fonctions['leet']: #Traitement par chaque fonction
                new_dico.append(f.alternative_alphabet(c_dico,alpha_l33t))
            if dic_fonctions['insert_special_char']: #Traitement par chaque fonction
                new_dico.append(f.insert_special_char(c_dico,s_char))

    new_dico_merged=h.merger(new_dico) #Fusion des listes du txt en cours de traitement
    dictionnaires.append(new_dico_merged) #Ajout des mots traités.

#Création du dictionnaire général


dictionnaire_g=h.merger(dictionnaires)

#Potentiel retour des dictionnaires intermédiaires

if skip_gen :
    num,other=h.separate_lists(dictionnaire_g)
    #fichier pour nombres
    filepath_sortie_s1 = "./sorties_txt_inter/numbers.txt"
    if os.path.isfile(filepath_sortie_s1) :
        os.remove(filepath_sortie_s1)
    dico_num = open(filepath_sortie_s1,"x")
    for word in num :
        dico_num.write(word)
        dico_num.write("\n")
    dico_num.close()
    #fichier pour autre
    filepath_sortie_s2 = "./sorties_txt_inter/other.txt"
    if os.path.isfile(filepath_sortie_s2) :
        os.remove(filepath_sortie_s2)
    dico_other = open(filepath_sortie_s2,"x")
    for word in other :
        dico_other.write(word)
        dico_other.write("\n")
    dico_other.close()



#Génération de la liste de mots de passe par permutation

else :
    print("shuffling")
    start=time.time()
    generated=sm.shuffle(dictionnaire_g,permut,filepath_sortie)
    end=time.time()
    print("done in",end-start)