import sys


# Checks number of arguments passed to module when it is run.
# It is also possible to use sys.argv[1] to pass arguments
# to the module like input.
def main(argv):
    if len(argv) > 1:
        print('''\
This module does not require arguments.
Terminating now.\
        ''')
        sys.exit()


def greeting(x):
    print('hello ' + x)


# Enables a module to be run as a standalone script.
# To run this use the command prompt and type python -m mymodule1 in the file
# directory.
if __name__ == '__main__':
    main(sys.argv)
    greeting('')
