import os
from pyforchange.egg.resources.modules import install
# BEWARE: There is an import in line ~51

class Lang:
    def __init__(self,name: str):
        self.name=name
        self.extension="."+self.name
        self.root="/usr/bin/python "+name+self.extension
    def write(self,T: str,name: str):
        f=open(name+self.extension,"w")
        f.write(T)
        f.close()
    def append(self,T: str,name: str):
        f=open(name+self.extension,"a")
        f.write(T)
        f.close()
    def read(self, name: str):
        f=open(name+self.extension,"r")
        text=f.read()
        f.close()
        return text
    def execute(self,name: str):
        try:
            os.system(self.root)
        except:
            print("Execute error in: "+self.root)
    def delete(self,name: str):
        os.remove(name+self.extension)
    def getLines(self,name: str):
        h=open(name+self.extension,"r")
        lines=h.readlines()
        h.close()
        return lines
    def writeLines(self,lines,name: str):
        self.write("",name)
        for i in lines:
            self.append(i,name)

# Extensions
py=Lang("py")
txt=Lang("txt")
nqa=Lang("nqa")
pfcf=Lang("pfcf")
html=Lang("html")

class Document():
    def __init__(self, name: str, output: str ="index"):
        install("bs4")
        # BEWARE: There is an import here
        from bs4 import BeautifulSoup
        self.name=name
        doc=open(self.name+".html").read()
        self.soup=BeautifulSoup(doc,features="html.parser")
        self.output=output
        lines=html.getLines(self.name)
        html.writeLines(lines, self.output)
    def write(self, text: str, id: str):
        lines=html.getLines(self.output)
        for i in range(0,len(lines)):
            l=lines[i]
            words=l.split()
            if words[0]=="$egg" and id==words[1]:
                lines[i]=text+"\n"
                html.writeLines(lines,self.output)
                return lines
    def addTag(self,tag: str, content: str, id: str):
        return self.write(makeTag(self,tag, content),id)

def makeTag(document,tag: str, content: str):
    new=document.soup.new_tag(tag)
    new.string=content
    return str(new)
