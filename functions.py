import helper as h


def prototype_fonction(dicos,a_traite):
    new_dico=[]
    for i in a_traite :
        #traitement du dico
        for word in dicos[i]:
            new_dico.append(h.toUpper(word))
    return new_dico



def traitement_date(file_name):
    wordlist = []
    file_path = "./dicos/" + file_name + ".txt"
    for name in h.readTXT(file_path):
        wordlist.append(name)
    return wordlist


def traitement_nomh(file_name):
    wordlist = []
    file_path="./dicos/"+file_name+".txt"
    for name in h.readTXT(file_path) :
        wordlist.append(name)
    return wordlist


def traitement_nombre(file_name):
    wordlist = []
    return wordlist
