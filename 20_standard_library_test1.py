# Demonstrates how to use some modules from the std library.
import os
import shutil
import glob
import zlib
import zipfile
import sys
import urllib.request
import json
import datetime
import timeit
import doctest

# Current working directory.
print(os.getcwd())
# Change working directory.
# To go back up, use os.chdir('..').
os.chdir(os.getcwd() + r'\files')
# Lists all files and folders in a directory.
print(os.listdir(os.getcwd()))
# Makes and removes a directory. Path can also be used instead.
# os.makedirs does the same thing but also creates all intemediate dirs
# if you give it a path.
os.mkdir('testdir')
os.rmdir('testdir')
# A common command that joins the directory path to the filename.
file_path = os.path.abspath(os.path.join(os.getcwd(), 'test.txt'))
print(file_path)
# Returns the filename again.
print(os.path.basename(file_path))
# Runs commands in cmd. In this case returns working directory.
# Other commands include mkdir (make directory) and rmdir.
print(os.system('echo %cd%'))
print()

# Checks if file exists.
if os.path.exists(file_path):
    os.system('del test.txt')
# Making text file.
os.system('echo testing > test.txt')
os.system('del test.txt')
# dir and help are common general commands.
# The first lists all possible commands,
# the second retrieves help documentation.
# print(dir(os))
# print(help(os))

# Suggested module for file and directory management.
shutil.copyfile('file.txt', 'test.txt')
# Does the same as above but you can use path as a target instead of filename.
# If a dir is specified as target path, the file will have the same name as
# the original.
# shutil.copy('file.txt',
#             os.path.join(os.getcwd(), 'test.txt'))

# Makes file lists from wildcard searches.
# If wildcard searches are not required, use os.listdir(path) instead.
# Note that glob returns files with their full path, while os.listdir lists
# directory and filenames only.
# Demonstrated here with data compression.
print(glob.glob('*.txt'))
# You need rb here to perform compression.
for file in glob.glob('*.txt'):
    with open(file, 'rb') as f:
        original_data = f.read()
        compressed_data = zlib.compress(original_data, zlib.Z_BEST_COMPRESSION)
        compress_ratio = (float(len(original_data)) -
                          float(len(compressed_data))) / float(len(original_data))
        print('{}: {} => {} or {:.2%} compression'.format(
            file, len(original_data), len(compressed_data), compress_ratio))
print()

# Dealing with zipfiles.
filename = 'zipfile.zip'
# Writing a zipfile.
with zipfile.ZipFile(filename, 'w') as zip:
    for file in glob.glob('*.txt'):
        zip.write(file)

with zipfile.ZipFile(filename, 'r') as zip:
    # Lists contents of zipfile.
    zip.printdir()
    # Extracts to target dir. Defaults to working dir if target not specified.
    zip.extractall(os.getcwd() + r'\zipdir')
print()

# sys.argv is used to determine if the script is called in cmd with the
# correct marameters. sys.arg[0] always contains the script name if
# cmd is not run.
print(sys.argv)
print()
# Usage of sys.argv will be demonstrated in mymodule1.py

# urllib is basically a worse version of requests module.
url = 'https://raw.githubusercontent.com/persocom01/TestPython/master/files/file3.txt'
result = json.load(urllib.request.urlopen(url))
print(result)
print()

# Datetime manipulation.
now = datetime.date.today()
print(now)
format = '%m-%d-%y. %d %b %Y is a %A on the %d day of %B.'
print(now.strftime(format))
# Calendar math YYYY, M, D format.
y2k = datetime.date(1999, 12, 31)
time_since = now - y2k
print(time_since.days)
print()

# Timing processes.
zip_process = timeit.Timer(
    stmt='zlib.compress(data, zlib.Z_BEST_COMPRESSION)',
    setup='import zlib; data=open(\'file3.txt\', \'rb\').read()',
)
time_taken_in_microseconds = zip_process.timeit(1) * 10**6
print('Time taken for 1 interation(s) =',
      time_taken_in_microseconds, 'microseconds')
# It is also possible to time simple statements.
print(timeit.timeit('10**6', number=1000000))
print()

# doctest scans for and validates modules.
# It allows you to put module tests in ''' comments '''.
# The tests must be written in the below specific way,
# with >>> module(input) indicating the module run with the result below.
# Error results are written in the below specific way.


def celcius_to_kelvin(x):
    '''
    >>> celcius_to_kelvin(1)
    274.15
    >>> celcius_to_kelvin(-500)
    Traceback (most recent call last):
        ...
    ValueError: Temperature cannot be below -273.15 degrees Celcius.
    '''

    if x < -273.15:
        raise ValueError(
            'Temperature cannot be below -273.15 degrees Celcius.')
    else:
        return x + 273.15


print(celcius_to_kelvin(1))
print()
print(doctest.testmod())
