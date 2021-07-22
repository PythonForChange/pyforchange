import pyforchange.nqs.core.core as core
from pyforchange.egg.resources.extensions import py

def write(name: str):
	T=core.compile(name)
	py.write(T,name)