import helper as h
import shufflerModule as sm
#Fonction de prototype
#Applicable à :
def proto(dico):
    new_dico=[]
    for word in dico:
        #ajouter ici votre traitment du mot
        new_dico.append(inis)
    return new_dico


def initiale(dico):
    new_dico=[]
    for word in dico:
        inis=h.get_initials(word)
        new_dico.append(inis)
    return new_dico

def mixedUpper(dico):
    new_dico=[]
    for word in dico:
        inis=sm.mixedUpper(word)
        new_dico.append(inis)
    new_dico=h.merger(new_dico)
    return new_dico
