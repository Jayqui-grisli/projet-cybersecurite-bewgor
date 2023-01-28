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

def num_to_month(num_list):
    months = ['janvier', 'février', 'mars', 'avril', 'mai', 'juin', 'juillet', 'août', 'septembre', 'octobre', 'novembre', 'décembre']
    month_list = []
    for num in num_list:
        if 1 <= num <= 12:
            month_list.append(months[num-1])
        else:
            month_list.append(None)
    return month_list


def alternative_alphabet(dico, alphabet):
    new_words = []
    for word in dico:
        new_word = ""
        for char in word:
            if char.isalpha():
                new_word += alphabet[ord(char.lower())-97]
            else:
                new_word += char
        new_words.append(new_word)
    return new_words

def insert_special_char(dico, special_chars):
    new_words = []
    for word in dico:
        for special_char in special_chars:
            for i in range(len(word) + 1):
                new_word = word[:i] + special_char + word[i:]
                new_words.append(new_word)
    return new_words
