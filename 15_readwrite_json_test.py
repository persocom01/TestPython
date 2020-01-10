# Demonstrates writing files in json format, useful for complicated objects.
import json

# Changes the python default directory. With this there is no need to set the
# file directory.
# import os
# print(os.getcwd())
# os.chdir(os.getcwd() + r'\files')

file = 'file2.txt'
directory_path = r'.\files'

if directory_path is None:
    file_path = file
else:
    file_path = directory_path + '\\' + file


# Returns string of json format.
dic = {'Apple': 'A type of fruit',
       'Ball': ['A spherical object.', 'A dance party.']}
print(json.dumps(dic))

# Demonstrates writing json to txt file. It is also possible to write to .json
# file for space saving.
with open(file_path, 'w') as f:
    # Optional arguments help json file be human readable.
    json.dump(dic, f, sort_keys=True, indent=4, ensure_ascii=False)

# Shows what the file looks like in json format. If being human readable
# is not a necessity, use rb instead as it is faster.
with open(file_path, 'r') as f:
    print(f.read())

# Demonstrates retriving the dictionary from json format.
with open(file_path, 'r') as f:
    dic2 = json.load(f)
    print(dic2)
