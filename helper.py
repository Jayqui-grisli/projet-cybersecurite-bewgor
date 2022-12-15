import numpy as np

def hello():
    print("hello world")

def readTXT(filename,keep_space=True):
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
    contents=[]
    filepath = "./exemple_config.txt"
    file=open(filepath)
    try:
        contents_raw=file.readlines()
    finally:
        file.close()
    for i in range(len(contents_raw)):
        contents_raw[i]=contents_raw[i].replace('\n',',')
        contents_raw[i] = contents_raw[i].replace('|', '')
        contents.append(contents_raw[i].rstrip())
    return contents


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
