import sys
import mymodule1
import builtins

# Returns the module search path.
print(sys.path)

# Returns list of names defined by module.
# Without arguments dir() returns currently defined names.
print(dir(mymodule1))

# Returns list of builtin names not returned by empty dir() function.
print(dir(builtins))
