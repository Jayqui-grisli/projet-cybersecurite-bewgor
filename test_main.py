import helper as h
import os

mot="test"

mot_up=h.toUpper(mot)

print(mot_up)

nom_sortie=input("Entrez le nom du fichier à générer \n")
print(nom_sortie)

if os.path.isfile("genere.txt") :
    os.remove("genere.txt")