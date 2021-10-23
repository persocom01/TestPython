# Import function that allows programatic importing of modules.
import importlib
# Imports all functions defined in __all__ in module.
# Note that using this method imports the functions directly into the symbol
# table.
from file_module2 import *
# Imports a package with subpackages and modules defined in the module's
# __init__.py file.
import mypackage as p
# If __init__.py is empty or the module is included in __all__ inside, you may
# possible to import a file using:
# import package_name.sub_package_name.filename
# from package_name.sub_package_name import filename
import mypackage.childpackage.smod1 as smod1
# Packages can also be imported using the built-in __import__() function
myp = __import__('mypackage')

# Demonstrates progamatic creation of variables. In this case file_module1 and
# 2 are imported.
_g = globals()
for i in range(1, 3):
    _g['m' + str(i)] = importlib.import_module('file_module' + str((i)))

# m1 was programatically imported.
m1.name('file_module1 name function')
# from file_module2 import *
name2()
# import mypackage as p
# It is possible to use name() directly because of the package __init__ file.
p.name('relative import mod1')
p.ai()
# import mypackage.childpackage.smod1 as smod1
smod1.name()
# myp = __import__('mypackage')
myp.childpackage.smod1.name()

# To import modules 1 level up the directory the script is run, use the
# following code:
# import os, sys
# currentdir = os.path.dirname(os.path.realpath(__file__))
# parentdir = os.path.dirname(currentdir)
# sys.path.append(parentdir)

# You can find more python modules from:
# https://docs.python.org/3/py-modindex.html
