# Import function that allows programatic importing of modules.
import importlib
# Imports all functions defined in __all__ in module.
# Note that using this method imports the functions directly into the symbol
# table.
from mymodule2 import *
# Imports a package with subpackages and modules defined in __init__.py.
import mypackage as p
# If the modules are not defined, a from packagename import modulename is
# required instead.
from mypackage import mod1
from mypackage.childpackage import mod2

# Demonstrates progamatic creation of variables. In this case mymodule1 and 2
# are imported.
_g = globals()
for i in range(1, 3):
    _g['m' + str(i)] = importlib.import_module('mymodule' + str((i)))

x = 'Bob'

m1.greeting(x)
greeting(x)
p.mod1.question(x)
mod1.reply(x)
p.childpackage.mod2.goodbye(x)
mod2.goodbye2(x)

# You can find more python modules from:
# https://docs.python.org/3/py-modindex.html
