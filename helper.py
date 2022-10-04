import numpy as np

def hello():
    print("hello world")

def readTXT(filepath,keep_space=False):
    contents=[]
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


def toUpper(contents):
    upperContent=[]
    for word in contents:
        upperContent.append(word.upper())
    return upperContent


def toLower(contents):
    lowerContent=[]
    for word in contents:
        lowerContent.append(word.lower())
    return lowerContent

def firstUpper(contents):
    firstUpperContent=[]
    for word in contents:
        firstUpperContent.append(word.title())
    return firstUpperContent
