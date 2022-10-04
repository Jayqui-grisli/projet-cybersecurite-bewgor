
def hello():
    print("hello world")

def readTXT(filepath,keep_space=False):
    file=open(filepath)
    try:
        contents=file.readlines()
    finally:
        file.close()
    for i in range(len(contents)):
        contents[i]=contents[i].replace('\n','')
        if(not keep_space):
                contents[i]=contents[i].replace(' ','')
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
