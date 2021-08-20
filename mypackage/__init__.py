# The __init__.py is used to cause python to identify the folder as an
# importable package. It is often kept blank, but by filling it out you can
# avoid having to import files in the package individually.
# Demonstrates use of relative import for packages. Use . for current dir and
# .. for one level up.
from .mod1 import name
# Absolute import still usable.
from mypackage.mod1 import ai
from mypackage import childpackage

# Just like how modules can define imported functions, packages can define
# which files within the package can be imported.
# __all__ = ['mod1', 'mod2']
__all__ = ['mod1']
