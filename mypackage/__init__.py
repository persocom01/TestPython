# Demonstrates use of relative import for packages.
from . import mod1
# Absolute import still usable.
from mypackage import childpackage

# Just like how modules can define imported functions, packages can define imported modules.
__all__ = ['mod1', ]
