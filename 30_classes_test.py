import os
import json
import cerberus
import requests
import shutil

# Write data to file. Push it to github manually.
cats = [{'name': 'Kuro', 'sex': 'M', 'color': 'Black'},
        {'name': 'Shiro', 'sex': 'F', 'color': 'White'}]
file_path = os.path.join(os.getcwd() + r'\files', 'file3.txt')
with open(file_path, 'w') as f:
    json.dump(cats, f, sort_keys=False, indent=4, ensure_ascii=False)

# Demonstrates use of requests to retrieve files online.
r = requests.get(
    'https://raw.githubusercontent.com/persocom01/TestPython/master/files/file3.txt')
# stream = True is meant for large files. The file is downloaded in chunks
# instead of all at once.
r_img = requests.get(
    'https://raw.githubusercontent.com/persocom01/TestPython/master/Innocence.jpg', stream=True)

# status code 200 means the request was sucessful.
if r.status_code == 200:
    # request module contains its own json decoder, so json.load isn't required.
    cats2 = r.json()

img_file_path = os.path.join(os.getcwd() + r'\files', 'copied_image.jpg')
if r_img.status_code == 200:
    with open(img_file_path, 'wb') as f:
        # Alternatively, you can iterate over the chunks using:
        # for chunk in r_img:
            # f.write(chunk)
        r_img.raw.decode_content = True
        shutil.copyfileobj(r_img.raw, f)

# Demonstrates use of cerberus validator.
# If only the type needs to be validated, use isinstance(object, type) instead.
schema = {
    'sex': {'type': 'string', 'allowed': ['M', 'F']}
}

# allow_unknown=True allows unknown keys to exist.
v = cerberus.Validator(schema, allow_unknown=True)

for key in cats2:
    if not v.validate(key):
        raise Exception('Wrong value for sex.')
        print(v.errors)

# Demonstrates creation of class.
# In this case a dictionary is used to set instance attributes.


class Animal:
    # Class properties not inside the __init__ function are called class
    # variables. They are shared by all instances of the class.
    # They can be overwritten in individual instances, but mutable objects like
    # lists will remain shared.
    subclasses = []

    def __init__(self, dictionary):
        # Class properties inside the __init__ function are called instance
        # variables.
        self.trick = []
        for k, v in dictionary.items():
            setattr(self, k, v)

    def add_trick(self, trick):
        self.trick.append(trick)

# Demonstrates creation of subclass


class Cat(Animal):
    def sound(self):
        print('Meow')


Kuro = Cat(cats2[0])

# As this property is mutable, this line will affect the base class.
Kuro.subclasses.append('Cat')
Kuro.add_trick('claw rush')
Kuro.sound()

print('shared class list: ', Animal.subclasses)
print(Kuro.name, Kuro.sex, Kuro.color)
print(Kuro.trick)


# It is also possible for a subclass to inherit from multiple classes.
# In those cases the leftmost superclass takes priority.
