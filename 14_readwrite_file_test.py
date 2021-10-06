# Demonstrates reading and writing a file.
import os
import io
import time

# open(file, mode='r', buffering=-1, encoding=None, errors=None, newline=None,
# closefd=True, opener=None)
# modes:
# r - read
# rb - read binary
# r+ - r + write
# rb+ - rb + write
# w - write. OVERWRITES file if it exists. Creates a new one if it doesn't.
# wb - write binary
# w+ - w + read
# wb+ - wb + read
# a - append. Creates a new file if it doesn't exist.
# ab - append binary
# a+ - a + read. f.seek(0) needs to be used prior to read to set the read
# position to the beginning of the file.
# ab+ - ab + read
# encoding can be import since windows does not use the same encoding as linux.
# To avoid encoding issues, use encoding='utf-8'

# File attributes:
# .closed - boolean.
# .mode - file access mode.
# .name
# .softspace - false if space explicitly required with print.

# Demonstrates reading a file.
# Using with automatically closes the file when done, otherwise, f.close()
# needs to be used to prevent resource wastage.
# To open multiple files, use:
# with open('file1', 'r') as f1, open('file2', 'r') as f2:
# .split() is used here to split file contents into a list.
# For better splitting use regex.
read_file = './files/file.txt'
with open(read_file, 'r', encoding='utf-8') as f:
    # Demonstrates how to get the filename of the file.
    filename = os.path.basename(f.name)
    print(f'contents of file {filename}')
    print(f.read().split())

# Demonstrates use of readline to read individual lines.
# The b mode is necessary for use of most seek methods other than 0 to work.
with open(read_file, 'rb') as f:
    print(f.readline())
    print(f.readline())
    # Demonstrates use of tell to read position and seek to goto position.
    print(f.tell())
    # For the second argument, 0=from beginning, 1=from current, 2=from end.
    print(f.seek(-8, 2))
    print(f.readline())

# Functionally idential to repeating readline() if you read all lines.
# readlines() returns a list of lines. Alternatively, use list(f).
with open(read_file, 'r', encoding='utf-8') as f:
    for line in f.readlines():
        print(line, end='')
    print()

# Demonstrates use of loops to read files instead of with.
# It does not close the file automatically.
try:
    f = open(read_file, 'r', encoding='utf-8')
    for line in f:
        print(line, end='')
finally:
    print(f.closed)
    print()
    f.close()

# Demonstrates writing to a file without with.
# Because changes won't be saved until the file is closed,
# it has to be closed before the new contents can be read.
# Not used in this file is the mode a for append.
begin = time.time()
write_file = './files/file2.txt'
try:
    f = open(write_file, 'w+', encoding='utf-8')
    f.write('line1\nline2')
    # Reads nothing.
    print(f.read(), end='')
finally:
    f.close()
    f = open(write_file, 'r', encoding='utf-8')
    print(f.read())
    f.close()
end = time.time()
seconds = end - begin
print('write file time: ' + str(seconds))
print()

# Demonstrates writing and reading from a temp file.
# There are times when it is convenient to write data to a temp file instead
# of dedicating a space in local storage, especially when the file is small.
# In such cases, this method is much faster.
begin = time.time()
with io.BytesIO() as f:
    f.write(b'line1\nline2')
    # Read nothing.
    print(f.read())
    # You need to seek to the beginning of the buffer to read it.
    f.seek(0)
    print(f.read())
end = time.time()
seconds = end - begin
print('write buffer time: ' + str(seconds))
