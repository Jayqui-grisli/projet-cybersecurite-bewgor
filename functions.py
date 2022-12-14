import helper as h

#Fonction de prototype
#Applicable à : noms

def initiale(dico):
    new_dico=[]
    for word in dico:
        inis=h.get_initials(word)
        new_dico.append(inis)
    return new_dico



