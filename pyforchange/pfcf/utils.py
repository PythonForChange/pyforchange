import time, os, json, math

def getLines(adress: str):
  h=open(adress,"r")
  lines=h.readlines()
  h.close()
  return lines

def sleep(i: int =100):
  time.sleep(i/1000)

def delete(name: str,fileformat:str =".pfcf"):
  os.remove(name+fileformat)

def dump(structure, file):
  json.dump(structure, file, indent=2)

def clearConsole():
  command = 'clear'
  if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls    
    command = 'cls'
  os.system(command)

def floor(f: float):
  return math.floor(f)

class Parser():
  def __init__(self,name: str ="Parser"):
    self.sep=[',']
    self.sec=['|']
    self.ski=["\""]
    self.vip=["\\"]
    self.den=["~"]
    self.name=name
  def compare(self,x: str,arr):
    k = False
    for i in arr:
      k =( k or x==i)
    return k
  def separator(self,x: str ):
    return self.compare(x,self.sep)
  def section(self,x: str):
    return self.compare(x,self.sec)
  def skip(self,x: str):
    return self.compare(x,self.ski)
  def isVip(self,x: str):
    return self.compare(x,self.vip)
  def isDeny(self,x: str):
    return self.compare(x,self.den)

def execute(name):
  try:
    t="/usr/bin/python "+name+".py"
    os.system(t)
  except:
    print("Execute error in: "+"/usr/bin/python "+name+".py")