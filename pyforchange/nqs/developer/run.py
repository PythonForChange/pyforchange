from pyforchange.nqs.developer.write import write
from pyforchange.egg.resources.extensions import py

def run(name: str):
    write(name)
    py.execute(name)