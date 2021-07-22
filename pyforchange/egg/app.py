#Imports
from pyforchange.egg.resources.console import get, clearConsole
from pyforchange.egg.resources.extensions import py
from pyforchange.egg.resources.constants import *
from pyforchange.egg.resources.modules import install, upgrade, Repo
from pyforchange.egg.resources.help import help
from pyforchange.egg.resources.auth import login, register
# BEWARE: There are imports in lines: ~17 & ~21

def eggConsole(condition: bool = True):
    print(white+"Egg Console is now running")
    logged=0
    while condition:
        i=get("egg")
        if i=="$nqs":
            # BEWARE: There is an import here
            from pyforchange.nqs.developer.app import developerConsole
            developerConsole()
        elif i=="$new":
            # BEWARE: There is an import here
            from pyforchange.news.app import journalistConsole
            journalistConsole()
        elif i=="$login":
            login()
        elif i=="$register":
            register()
        elif i=="$install":
            print(white+"Package:")
            name=get("egg")
            install(name)
        elif i=="$upgrade":
            print(white+"Package:")
            name=get("egg")
            upgrade(name)
        elif i=="$pull":
            print(white+"Repo:")
            name=get("egg")
            repo=Repo(name)
            print(white+"Package:")
            package=get("egg")
            last=repo.pull(package)
        elif i=="$help":
            help()
        elif i=="$clear":
            clearConsole()
        elif i=="$end":
            print(white+"Egg Console stopped running")
            return "done"
        else:
    	    pass