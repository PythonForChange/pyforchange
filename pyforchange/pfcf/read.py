from pyforchange.pfcf.utils import *
from pyforchange.pfcf.code import *

def read(name: str,printYesOrNo: int =1,returnText: int =0):
  lines=getLines(name+".pfcf")
  T=""
  t=""
  code=""
  codel="" #code language
  m=0
  codem=0
  p=Parser()
  lineCount=0
  for k in lines:
    count=0
    for i in range(0,len(k)):
      j=k[i]
      if  p.isDeny(j):
        if m==2:
          m=0
        else:
          m=2
      elif  p.isVip(j):
        m=1
      elif m==2: #Comment mode on
        pass
      elif m==1: #Vip mode on
        t+=j
        m=0
      elif j=="<" or j==">":
        codem+=1
      elif codem==4:
        try:
          codef(codel,code)
          codem==0
          codel=""
          code=""
        except:
          print("Sintax error")
      elif codem==3:
        pass
      elif codem==2:
        code+=j
      elif codem==1: #Code mode on
        codel+=j
      elif p.separator(j):
        T+=t+"\n"
        t=""
      elif p.section(j):
        T+="\n"
      elif  p.skip(j):
        pass
      elif j!="\n":
        t+=j
      count+=1
    lineCount+=1
  if printYesOrNo:
    print(T)
  if returnText:
    a={T,k}
    return a
  return T

def executepfcf(name: str,delta: int =400):
  while True:
    T=read(name)
    f=open(name+".txt","w")
    f.write(T)
    f.close()
    sleep(delta)
    clearConsole()