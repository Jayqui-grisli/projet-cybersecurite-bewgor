import helper as h
import functions as f
import os


#Interaction utilisateur

#nom_sortie=input("Entrez le nom du fichier à générer \n")
nom_sortie='test'
filepath_sortie = "./sorties_txt/" + nom_sortie + ".txt"


#Lecture du fichier de configuration
# TODO : Gestion du fichier de configuration, ouverture, lecture
print(h.readConfig())
a_traite_proto=[0]

#Parsing des .txt

dictionnaires=[]
dictionnaires.append(h.readTXT("noms"))
dictionnaires.append(h.readTXT("test"))
dictionnaires.append(h.readTXT("date"))
dictionnaires.append(h.readTXT("nombres"))


#Traitement des dictionnaires

dictionnaires.append(f.prototype_fonction(dictionnaires,a_traite_proto))

#Création du dictionnaire général

dictionnaire_g=[]
for d in dictionnaires :
    for w in d :
        dictionnaire_g.append(w)

#Génération de la liste de mots de passe par permutation

generated=dictionnaire_g

#Création du txt

if os.path.isfile(filepath_sortie) :
    os.remove(filepath_sortie)
dico_genere = open(filepath_sortie,"x")
for word in dictionnaire_g :
    dico_genere.write(word)
    dico_genere.write("\n")
dico_genere.close()