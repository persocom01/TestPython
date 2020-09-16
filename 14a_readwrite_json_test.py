# Demonstrates reading and writing files in json format.
import json

file = './files/file2.txt'

# Returns string of json format.
dic = {'Apple': 'A type of fruit',
       'Ball': ['A spherical object.', 'A dance party.']}
print(json.dumps(dic))

# Demonstrates writing json to txt file. It is also possible to write to .json
# file for space saving.
with open(file, 'w') as f:
    # Optional arguments help json file be human readable.
    json.dump(dic, f, sort_keys=True, indent=4, ensure_ascii=False)

# Shows what the file looks like in json format. If being human readable
# is not a necessity, use rb instead as it is faster.
# For reasons unknown, singapore computers do not automatically use utf-8. As
# such problems may occur when trying to read a json file. Use encoding dring
# file load to fix the issue.
with open(file, 'r', encoding='utf-8') as f:
    print(f.read())

# Demonstrates retriving the dictionary from json format.
with open(file, 'r') as f:
    dic2 = json.load(f)
    print(dic2)
