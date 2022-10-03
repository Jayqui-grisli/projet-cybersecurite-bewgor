



from email import contentmanager


def hello():
    print("hello world")

def parseTXT(filepath):
    file=open(filepath)
    try:
        contents=file.readlines()
    finally:
        file.close()
    for i in range(len(contents)):
        contents[i]=contents[i].replace('\n','')
        contents[i]=contents[i].replace(' ','')
    return contents
