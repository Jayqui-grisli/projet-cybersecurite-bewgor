import numpy as np
import json

def hello():
    print("hello world")

def readTXT(filename,keep_space=False):
    contents=[]
    filepath = "./dicos/" + filename + ".txt"
    file=open(filepath)
    try:
        contents_raw=file.readlines()
    finally:
        file.close()
    for i in range(len(contents_raw)):
        contents_raw[i]=contents_raw[i].replace('\n','')
        if(not keep_space):
            contents=contents+contents_raw[i].rstrip().split(' ')
        else:
            contents.append(contents_raw[i].rstrip())
    return contents

def readConfig():
    conf_file = open("config.json", "r")
    configs = json.load(conf_file)
    dicos= configs["dicos"]
    return dicos


def toUpper(contents):
    upperContent=''
    for word in contents:
        upperContent+=word.upper()
    return upperContent


def toLower(contents):
    lowerContent=''
    for word in contents:
        lowerContent+=word.lower()
    return lowerContent

def firstUpper(contents):
    firstUpperContent=[]
    for word in contents:
        firstUpperContent.append(word.title())
    return firstUpperContent


def merger(lists):
    l_merged = []
    for d in lists:
        for w in d:
            lw = [w]
            l_merged = list(set(l_merged + lw))
    return l_merged

def get_initials(string):
    words = string.split(' ')
    initials = ''
    for word in words:
        initials += word[0]
    return initials

def separate_lists(input_list):
    numbers_list = []
    strings_list = []
    for i in input_list:
        if i.isnumeric():
            numbers_list.append(int(i))
        else:
            strings_list.append(i)
    return numbers_list, strings_list
