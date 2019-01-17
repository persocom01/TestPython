import sys

# Returns the module search path.
print(sys.path)

# Returns list of names defined by module.
# Without arguments dir() returns currently defined names.
import mymodule1
print(dir(mymodule1))

# Returns list of builtin names not returned by empty dir() function.
import builtins
print(dir(builtins))
