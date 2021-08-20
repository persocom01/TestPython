import sys


# Checks number of arguments passed to module when it is run.
def main():
    name('file_module1')
    args = sys.argv[1:]
    if not args:
        print('no arguments passed')
    elif len(args) == 1:
        print(f'{args[0]} passed to file module1')
    else:
        print('''\
This module only takes in 1 argument.
Terminating now.\
        ''')
        sys.exit()


def name(x):
    print(f'{x}')


# Enables a module to be run as a standalone script.
# To run this use the command prompt and type python -m file_module1 in the
# file directory.
if __name__ == '__main__':
    # It is also possible to pass arguments to the function at this stage
    # using main(sys.argv)
    main()
