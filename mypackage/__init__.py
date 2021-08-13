# The __init__.py is used to cause python to identify the folder as an
# importable package. It is normally kept blank, but can be written such that
# only specific files and functions can be imported.
# Demonstrates use of relative import for packages.
from . import mod1
# Absolute import still usable.
from mypackage import childpackage

# Just like how modules can define imported functions, packages can define imported modules.
__all__ = ['mod1', ]
