import pip, sys, subprocess
import importlib as il
from pyforchange.egg.resources.constants import white

def install(name: str):
    try:
        install_option_2(name)
        #raise Exception("error")
    except:
        print(white+"Install failed")
        print(white+"Retrying...")
        try:
            install_option_1(name)
        except:
            print(white+"Install failed")
            return "error"
    print(white+name+" succesfully installed")
    return "done"
        
def install_option_1(name: str):
    #Implement pip using pip package
    pip.main(['install', name])
    return "done"

def install_option_2(name: str):
    #Implement pip as a subprocess
    if name=="$upgrade":
        subprocess.check_call([sys.executable, '-m', 'pip', 'install', '--upgrade', 'pip'])
    else:
        subprocess.check_call([sys.executable, '-m', 'pip', 'install', name])
    return "done"

def upgrade(name: str):
    try:
        subprocess.check_call([sys.executable, '-m', 'pip', 'install', '--upgrade', name])
    except:
        print(white+name+" succesfully ugraded")
    return "done"

class Repo():
    def __init__(self,name: str):
        self.name=name
    def pull(self,package: str,functions: str = ""):
        funcs=functions.split(" ")
        try:
            package="github_com.PythonForChange."+self.name+"."+package
            _temp = il.__import__(package, globals(), locals(), funcs, 0)
            return _temp
        except:
            print(white+"Pull failed")
