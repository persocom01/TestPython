import sys


# Checks number of arguments passed to module when it is run.
def main():
    args = sys.argv[1:]
    if not args:
        greeting('')
    elif len(args) == 1:
        greeting(args[0])
    else:
        print('''\
This module only takes in 1 argument.
Terminating now.\
        ''')
        sys.exit()


def greeting(x):
    print('hello ' + x)


# Enables a module to be run as a standalone script.
# To run this use the command prompt and type python -m mymodule1 in the file
# directory.
if __name__ == '__main__':
    # It is also possible to pass arguments to the function at this stage
    # using main(sys.argv)
    main()
