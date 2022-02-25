import sys
import subprocess
import pkg_resources
from pathlib import Path

__name__ = "PyLibCheck"
__version__ = "1.0.0"
__python__ = Path(sys.executable).resolve()

class invalidType(Exception): ...
class invalidVer(Exception): ...


def checkPackage(package: list or tuple or str) -> bool:
    '''
    check if a package is installed, returns bool
    can pass in a either a tuple, list or string
    '''

def checkSpecificVer(package: list or tuple or str) -> bool:
    '''
    check if a specific version of a package is installed, returns bool
    can pass in a either a tuple, list or string
    '''




def installPackage(package: list or tuple or str):
    '''
    Install a package if they don't already have it installed
    If specific version is specified it might get buggy, use installSpecificVer() for that instead
    Accepts either tuple, list or string
    '''
    if type(package) not in [list, tuple, str]:
        raise invalidType('"{}" is not a supported type, needs to be either *list, tuple or str*'.format(type(package).__name__))
    #get all installed libs
    installed_packages = sorted(["{0}".format(i.key) for i in pkg_resources.working_set])
    if type(package) == str:
        if package not in installed_packages:
            try:
                subprocess.check_call([__python__, '-m', 'pip', 'install', lib])
            except Exception:
                pass
    else:
        for lib in package:
            if lib not in installed_packages:
                try:
                    subprocess.check_call([__python__, '-m', 'pip', 'install', lib])
                except Exception:
                    pass

def installSpecificVer(package: list or tuple or str):
    '''
    Install a specific version of a package if they don't already have it installed
    Can pass in a either a tuple, list or string
    '''
    if type(package) not in [list, tuple, str]:
        raise invalidType('"{}" is not a supported type, needs to be either *list, tuple or str*'.format(type(package).__name__))
    installed_packages = sorted(["{0}=={1}".format(i.key, i.version) for i in pkg_resources.working_set])
    if type(package) == str:
        if not "==" or not "." in [i for i in package]:
            raise invalidVer('Improper version passed, this function requires a specific version of a package, example: pylibcheck==1.0.2')
        if package not in installed_packages:
            try:
                subprocess.check_call([__python__, '-m', 'pip', 'install', lib])
            except Exception:
                pass
    else:
        for lib in package:
            if not "==" or not "." in lib:
                raise invalidVer('Improper version passed, this function requires a specific version of a package, example: pylibcheck==1.0.2')
            if lib not in installed_packages:
                try:
                    subprocess.check_call([__python__, '-m', 'pip', 'install', lib])
                except Exception:
                    pass