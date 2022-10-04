import helper as h

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
