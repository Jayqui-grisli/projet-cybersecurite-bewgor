import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse
import re
import itertools
import os

class scraper :
    links_to_visit=[]
    url=None
    depth=0
    myPath_words=os.path.realpath(os.path.dirname(__file__))+"\scraped_word_list.txt"
    myPath_numbers=os.path.realpath(os.path.dirname(__file__))+"\scraped_number_list.txt"
    stay_on_domain=False
    domain=""

    def __init__(self):
        #demander l'url a l'user + traiter via regex si le format est bon
        print("enter URL (format : example.something.else/stuff): ")
        self.url = input()
        regex=r"^((https://)?([A-Z]|[a-z])+\.([A-Z]|[a-z])+\.([A-Z]|[a-z])+/?)"
        while (len(re.findall(regex,self.url))==0):
            print("enter URL (format : example.something.else/stuff): ")
            self.url = input()
        if(re.search(r"^https://",self.url)==None):
            self.url="https://"+self.url
        
        #demander a l'user la profonderur de recherche (limitée à 3)
        print("enter depth of research (0-3) : ")
        self.depth=int(input())
        while (self.depth not in range(0,4)):
            print("enter depth of research (0-3) : ")
            self.depth=input()

        #demander a l'user s'il souhaite rester sur le domaine
        if(self.depth>0):
            print("Stay on domain (y/n) ?")
            temp_char=input()
            while(temp_char!="y" and temp_char!="n"):
                print("Stay on domain (y/n) ?")
                temp_char=input()
            if(temp_char=="y"):
                self.stay_on_domain=True
                self.domain=urlparse(self.url).netloc

        with open(self.myPath_words, "w", encoding="utf-16") as f:
            f.write("")
        with open(self.myPath_numbers, "w", encoding="utf-16") as f:
            f.write("")
        #lancer la séquence de traitement
        self.links_to_visit.append(self.url)
        self.visitURL(self.depth,self.url)
        


    def visitURL(self,depth,url):
        self.links_to_visit.remove(url)
        soup=None
        try:
            page=requests.get(url)
            soup=BeautifulSoup(page.content,"html.parser")
            self.parseSoup(soup)
            print("visiting :",url)
        except:
            print("ERROR requesting :",url)
            pass
        if depth==0:
            return
        else:
            if (soup is not None):
                #rechercher toutes les urls de la page et les ajouter à la liste de urls à visiter
                tags=soup.find_all("a")
                for each_tag in tags:
                    try:
                        each_url=each_tag["href"]
                        if(not self.stay_on_domain):
                            #si l'url est relative on concatenne l'url parente pour recreer l'url
                            if (re.search(r"^/.+",each_url)!=None):
                                each_url=url+each_url
                            #si la balise relie une ancre sur la page on ne l'ajoute pas
                            if (re.search(r"^#",each_url)==None):
                                self.links_to_visit.append(each_url)
                        else:
                            #si l'url est relative on concatenne l'url parente pour recreer l'url
                            if (re.search(r"^/.*",each_url)!=None):
                                each_url=url+each_url
                            #l'url doit contenir le domaine du site initial
                            if(re.search(rf"\b(https://)?{re.escape(self.domain)}",each_url)!=None):
                                self.links_to_visit.append(each_url)
                    except:
                        print("ERROR parsing",each_tag)
                        pass
        for each_unvisited in self.links_to_visit:
            self.visitURL(depth-1,each_unvisited)


    def parseSoup(self,soup):
        word_list=[]
        #je n'ai pas de meilleure solution pour tout extraire que de regarder dans les par et les div
        div_html=soup.find_all("div")
        p_html=soup.find_all("p")
        for each_text in p_html:
            temp_str=each_text.text
            #supprimer les charactères spéciaux, les espaces et les mots de 1 à 2 lettres
            for character in '‘’–.:/?,!-+*=()_|#"\';<>\n@»«][':
                temp_str=temp_str.replace(character," ")
            temp_str=re.sub(r"(^ | +)"," ",temp_str)
            temp_str=re.sub(r"\b\w{1,2}\b"," ",temp_str)
            temp_list=temp_str.split()
            word_list.append(temp_list)
        for each_text in div_html:
            temp_str=each_text.text
            for character in '‘’–.:/?,!-+*=()_|#"\';<>\n@][»«':
                temp_str=temp_str.replace(character," ")
            temp_str=re.sub(r" +"," ",temp_str)
            temp_str=re.sub(r"\b\w{1,2}\b"," ",temp_str)
            temp_list=temp_str.split()
            word_list.append(temp_list)
        #transformer list(list()) en list() et supprimer les doublons
        flat_word_list=list(itertools.chain(*word_list))
        self.writeToFile([*set(flat_word_list)])

    def writeToFile(self,words):
        file_numbers=open(self.myPath_numbers,"a",encoding="utf-16")
        for each_word in words:
            if (re.search(r"^[0-9]+\b",each_word)!=None):
                file_numbers.write(each_word+"\n")
        file_numbers.close()
        file_words=open(self.myPath_words,"a",encoding="utf-16")
        for each_word in words :
            if (re.search(r"^[0-9]+",each_word)==None):
                file_words.write(each_word+"\n")
        file_words.close()

myscraper=scraper()