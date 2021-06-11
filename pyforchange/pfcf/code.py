from pyforchange.pfcf.utils import *
import pyforchange.pfcf.codel.qiskit as q

def codef(codel: str,text: str): #code function
  form="_compile.py"
  f=open(codel+form,"w")
  t=""
  if codel=="qiskit":
    t=qiskit(text)
  f.write(t)
  f.close()

def qiskit(text: str):
  T=""
  T+="from qiskit import QuantumCircuit, execute, Aer\n"
  T+="from qiskit.visualization import plot_histogram,display\n"
  s=0
  command=""
  param=""
  Q=0
  gate=""
  gatecount=0
  qdef=0
  for i in text:
    if i==",":
      pass
    elif s==1: #settings mode on
      if i!=" ":
        command+=i
      else:
        s=2
    elif s==2:
      if i!=" " and i!="\n":
        param+=i
      else:
        T+=q.settings(command,param)
        command=""
        param=""
        s=0
    elif i=="$":
      s=1
    elif qdef==1:
      if i=="q":
        Q+=1
      elif i=="\n":
        qdef=2
        T+="circuit=QuantumCircuit("+str(Q)+","+str(Q)+")\n"
    elif qdef==2:
      if i!="\n" and i!=" ":
        gate+=i
      elif i==" ":
        gatecount+=0.5
        T+=q.quantum(gate,gatecount)
        gate=""
      else:
        T+=q.quantum(gate,gatecount)
        gate=""
        gatecount=0
    elif i=="q":
      qdef=1
      Q+=1
  return T

