import requests
from bs4 import BeautifulSoup
import re
import itertools
import os

class scraper :
    links_to_visit=[]
    url=None
    depth=0
    myPath=os.path.realpath(os.path.dirname(__file__))+"\scraped_word_list.txt"

    def __init__(self):
        #demander l'url a l'user + traiter via regex si le format est bon
        print("enter URL (format : example.something.else/stuff): ")
        self.url = input()
        regex=r"^((https://)?([A-Z]|[a-z])+\.([A-Z]|[a-z])+\.([A-Z]|[a-z])+/?)"
        while (len(re.findall(regex,self.url))==0):
            print("enter URL (format : example.something.else/stuff): ")
            self.url = input()
        if(re.search("^https://",self.url)==None):
            self.url="https://"+self.url
        
        #demander a l'user la profonderur de recherche (limitée à 3)
        print("enter depth of research (0-3) : ")
        self.depth=int(input())
        while (self.depth not in range(0,4)):
            print("enter depth of research (0-3) : ")
            self.depth=input()
        
        with open(self.myPath, "w", encoding="utf-16") as f:
            f.write("")
        #lancer la séquence de traitement
        self.links_to_visit.append(self.url)
        self.visitURL(self.depth,self.url)
        


    def visitURL(self,depth,url):
        self.links_to_visit.remove(url)
        try:
            page=requests.get(url)
            soup=BeautifulSoup(page.content,"html.parser")
            self.parseSoup(soup)
            print("visiting :",url)
        except:
            pass
        if depth==0:
            return
        else:
            #rechercher toutes les urls de la page et les ajouter à la liste de urls à visiter
            tags=soup.find_all("a")
            for each_tag in tags:
                try:
                    each_url=each_tag["href"]
                    #si l'url est relative on concatenne l'url parente pour recreer l'url
                    if (re.search("^/.*",each_url)!=None):
                        each_url=url+each_url
                    #si la balise relie une ancre sur la page on ne l'ajoute pas
                    if (re.search("^#",each_url)==None):
                        self.links_to_visit.append(each_url)
                except:
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
            for character in '‘’–.:/?,!-+*=()_|#"\';<>\n@':
                temp_str=temp_str.replace(character," ")
            temp_str=re.sub(r"(^ | +)"," ",temp_str)
            temp_str=re.sub(r"\b\w{1,2}\b"," ",temp_str)
            temp_list=temp_str.split()
            word_list.append(temp_list)
        for each_text in div_html:
            temp_str=each_text.text
            for character in '‘’–.:/?,!-+*=()_|#"\';<>\n@':
                temp_str=temp_str.replace(character," ")
            temp_str=re.sub(r" +"," ",temp_str)
            temp_str=re.sub(r"\b\w{1,2}\b"," ",temp_str)
            temp_list=temp_str.split()
            word_list.append(temp_list)
        #transformer list(list()) en list()
        flat_word_list=list(itertools.chain(*word_list))
        self.writeToFile(flat_word_list)

    def writeToFile(self,words):
        with open(self.myPath, "a", encoding="utf-16") as f:
            for each_word in words:
                f.write(each_word+"\n")

            

myscraper=scraper()