import time, os
from pyforchange.egg.resources.constants import *

def sleep(i: int =100):
  time.sleep(i/1000)

def clearConsole():
  command = 'clear'
  if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls    
    command = 'cls'
  os.system(command)

def display(T,delta: int =400,condition: bool = True):
  while condition:
    print(T)
    sleep(delta)
    clearConsole()

def get(tag: str):
  i=input(blue+"$"+tag+"> "+green)
  return i