import helper as h

#Fonction de prototype
#Applicable à : noms
def prototype_fonction(dicos,a_traite):
    new_dico=[]
    for i in a_traite :
        #traitement du dico
        for word in dicos[i]:
            new_dico.append(word)
    return new_dico

