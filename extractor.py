import requests
import os

def parse(content):
    links=[]
    content=content.split("<img src=")
    content.pop(0)
    for i in content:
        con=i.split()
        link=con[0]
        link=list(link)
        
        if '"' in link:
            link.remove('"')
            link.remove('"')
        else:
            link.remove("'")
            link.remove("'")
        l=""
        for i in link:
            l=l+i
         
        links.append(l)
    return links
def getimage(content,dir):
    imageurls=parse(content)
    i=1
    currentdir=os.getcwd()
    os.chdir(dir)
    for url in imageurls:
        try:
            req=requests.get(url)
            image=req.content
            file=open("image"+str(i)+".png","wb")
            file.write(image)
            file.close()
            i+=1
    
        except (requests.exceptions.InvalidSchema,requests.exceptions.MissingSchema):
            continue
    os.chdir(currentdir)
