# Demonstrates reading and writing a file.

# File modes:
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
with open(read_file, 'r') as f:
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
with open(read_file, 'r') as f:
    for line in f.readlines():
        print(line, end='')
    print()

# Demonstrates use of loops to read files instead of with.
# It does not close the file automatically.
try:
    f = open(read_file, 'r')
    for line in f:
        print(line, end='')
finally:
    print(f.closed)
    print()
    f.close()

# Demonstrates writing to a file.
# Because changes won't be saved until the file is closed,
# it has to be closed before the new contents can be read.
# Not used in this file is the mode a for append.
write_file = './files/file2.txt'
try:
    f = open(write_file, 'w+')
    f.write('line1\nline2')
    # Reads nothing.
    print(f.read(), end='')
finally:
    f.close()
    f = open(write_file, 'r')
    print(f.read())
    f.close()
