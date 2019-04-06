#!/usr/bin/python
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

import sys
import re
import os
import shutil
import zipfile
# import commands

# Use for testing file in atom.
# Comment out if running from cmd.
# print(os.getcwd())
# os.chdir(os.getcwd() + r'\google-python-exercises')

"""Copy Special exercise
"""

# +++your code here+++
# Write functions and modify main() to call them


def get_special_paths(dirname):
    """Given a dirname, returns a list of all its special files."""
    result = []
    paths = os.listdir(dirname)
    for path in paths:
        match = re.search(r'__(\w+)__', path)
        if match:
            result.append(os.path.abspath(os.path.join(dirname, path)))
    return result


# print(get_special_paths(os.getcwd() + r'\copyspecial'))


def copy_to(paths, to_dir):
    """Copy all of the given files to the given dir, creating it if necessary."""
    if not os.path.exists(to_dir):
        os.mkdir(to_dir)
    for path in paths:
        filename = os.path.basename(path)
        shutil.copy(path, os.path.join(to_dir, filename))


# copy_to(get_special_paths(os.getcwd() + r'\copyspecial'),
#         os.path.join(os.getcwd() + r'\copyspecial', 'test'))


def zip_to(paths, zfile):
    """Zip up all of the given files into a new zip file with the given name."""
    with zipfile.ZipFile(zfile, 'w') as zip:
        for file in paths:
            zip.write(file)


# zip_to(get_special_paths(os.getcwd() + r'\copyspecial'),
#        os.path.join(os.getcwd() + r'\copyspecial', 'testzip.zip'))


def main():
    # This basic command line argument parsing code is provided.
    # Add code to call your functions below.

    # Make a list of command line arguments, omitting the [0] element
    # which is the script itself.
    args = sys.argv[1:]
    if not args:
        print("usage: [--todir dir][--tozip zipfile] dir [dir ...]"
              )
        sys.exit(1)

    # todir and tozip are either set from command line
    # or left as the empty string.
    # The args array is left just containing the dirs.
    todir = ''
    if args[0] == '--todir':
        todir = args[1]
        del args[0:2]

    tozip = ''
    if args[0] == '--tozip':
        tozip = args[1]
        del args[0:2]

    if len(args) == 0:
        print("error: must specify one or more dirs")
        sys.exit(1)

    # +++your code here+++
    # Call your functions
    paths = []
    for dirname in args:
        paths.extend(get_special_paths(dirname))

    if todir:
        copy_to(paths, todir)
    elif tozip:
        zip_to(paths, tozip)
    else:
        print('\n'.join(paths))


if __name__ == "__main__":
    main()
