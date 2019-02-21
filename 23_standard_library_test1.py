# Demonstrates how to use some modules from the std library.
import os
import shutil
import glob
import zlib
import sys
import re
import urllib.request
import json
from datetime import date

# Current working directory.
print(os.getcwd())
# Change working directory.
# To go back up, use os.chdir('..').
os.chdir(os.getcwd() + r'\files')
# Runs commands in cmd. In this case returns working directory.
# Other commands include mkdir (make directory) and rmdir.
print(os.system('echo %cd%'))
print()
# Making text file.
os.system('del test.txt')
os.system('echo testing > test.txt')
os.system('del test.txt')
# dir and help are common general commands.
# The first lists all possible commands,
# the second retrieves help documentation.
# print(dir(os))
# print(help(os))

# Suggested module for file and directory management.
shutil.copyfile('file.txt', 'test.txt')

# Makes file lists from wildcard searches.
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

# sys.argv is used to determine if the script is called in cmd with the
# correct marameters. sys.arg[0] always contains the script name if
# cmd is not run.
print(sys.argv)
print()
# Usage of sys.argv will be demonstrated in mymodule1.py

# Regular expression functions.
text = 'The quick brown fox jumps over the lazy dog.'
words_containing_o = re.findall(r'\b\w*o[a-z]*', text)
print(words_containing_o)
print()

# urllib is basically a worse version of requests module.
url = 'https://raw.githubusercontent.com/persocom01/TestPython/master/files/file3.txt'
result = json.load(urllib.request.urlopen(url))
print(result)
print()

# Datetime manipulation.
now = date.today()
print(now)
format = "%m-%d-%y. %d %b %Y is a %A on the %d day of %B."
print(now.strftime(format))
# Calendar math YYYY, M, D format.
y2k = date(1999, 12, 31)
time_since = now - y2k
print(time_since.days)
print()
