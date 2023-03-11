import sys

from colorama import Fore


def err(string):
    print("[ " + Fore.RED + "ERREUR.:" + string + Fore.RESET + " ]")
    sys.exit(-1)