from pyforchange.pfcf.read import *
from pyforchange.pfcf.utils import *

class FilesTree:
  def __init__(self,familyName: str ="tree",form: str =".pfcf"):
    self.name=familyName
    self.format=form
    self.reset()
  def reset(self):
    self.adress=self.name+"_hist"+self.format
    try:
      lines=self.getLines(self.adress)
      for i in lines:
        delete(self.name+"_"+str(i))
    except:
      pass
  def lastLine(self):
    lines=getLines(self.adress)
    return lines[len (lines)-1]
  def register(self,t: str):
    with open(self.adress, 'a') as h:
      h.write(t+"\r\n")

class LogFile:
  def __init__(self,name: str ="log",form: str =".pfcf"):
    self.name=name
    self.format=form
    self.reset()
    self.h=FilesTree(self.name)
  def row(self,t: str):
    self.text=self.text+str(t)+","
  def section(self):
    self.text=self.text+"|"
  def vip(self,t: str):
    s=self.p.vip[0]
    text=""
    for i in t:
      text+=s+i
    return text
  def den(self,t: str):
    s=self.p.den[0]
    text=s
    for i in t:
      text+=i
    text+=s
    return text
  def reset(self,resetParserYesOrNo: int =1):
    self.text=""
    self.adress=self.name+self.format
    if resetParserYesOrNo:
      self.p=Parser()
  def export(self):
    try:
      i=int(self.h.lastLine())+1
    except:
      i=0
    f=open(self.name+"_"+str(i)+self.format,"w")
    f.write(self.text)
    f.close()
    self.h.register(str(i))
  def readFrom(self,adress: str,printYesOrNo: int =1):
    self.text=read(adress,1,1)[1]   
  def read(self,name: str ="|",printYesOrNo: int =1):
    self.export()
    i=int(self.h.lastLine())
    if name=="|":
      self.readFrom(self.name+"_"+str(i)+self.format,printYesOrNo)
    else:
      self.readFrom(name,printYesOrNo)
  def fromDict(self,data):
    name=self.name+".json"
    with open(name, 'w') as file:
      dump(data, file)
    self.readFrom(name)
