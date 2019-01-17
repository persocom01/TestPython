import os
os.chdir(os.getcwd() + r'\TestPython/')

# Demonstrates writing files in json format, which is useful for more complicated objects.
import json

# Returns string of json format.
dic = {'Apple': 'A type of fruit', 'Ball': ['A spherical object.', 'A dance party.']}
print(json.dumps(dic))

# Demonstrates writing json to txt file. It is also possible to write to .json file for space saving.
with open('file2.txt', 'w') as f:
    # Optional arguments help json file be human readable.
    json.dump(dic, f, sort_keys=True, indent=4, ensure_ascii=False)

with open('file2.txt', 'r') as f:
    print(f.read())

# Demonstrates retriving the dictionary from json format.
with open('file2.txt', 'r') as f:
    dic2 = json.load(f)
    print(dic2)
