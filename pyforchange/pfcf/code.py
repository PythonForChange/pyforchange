from pyforchange.pfcf.utils import *
import pyforchange.pfcf.codel.qiskit as q
import pyforchange.pfcf.codel.wolfram as w

def codef(codel: str,text: str): #code function
  form="_compile.py"
  f=open(codel+form,"w")
  t=""
  if codel=="qiskit":
    t=qiskit(text)
  elif codel=="wolfram":
    t=wolfram(text)
  elif codel=="python":
    t=text
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

def wolfram(text: str):
  T=""
  T+="from wolframclient.evaluation import WolframLanguageSession\n"
  T+="from wolframclient.language import wl, wlexpr\n"
  T+="session = WolframLanguageSession()\n"
  s=0
  command=""
  param=""
  t=""
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
        T+=w.settings(command,param)
        command=""
        param=""
        s=0
    elif i=="$":
      s=1
    elif i=="\n" and t!="":
      T+="session.evaluate(wlexpr(\'"+t+"\'))\n"
      t=""
    elif i!="\n":
      t+=i
  return T
