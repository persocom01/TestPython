# Demonstrates classes in python.
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
# There are 5 HTTP request methods: GET, POST, PATCH, DELETE and HEAD. They can
# be used via the format requests.method(url, other_params). The kind of
# available params can be found here: https://www.w3schools.com/python/module_requests.asp
r = requests.get(
    'https://raw.githubusercontent.com/persocom01/TestPython/master/files/file3.txt')
# stream = True is meant for large files. The file is downloaded in chunks
# instead of all at once.
r_img = requests.get(
    'https://raw.githubusercontent.com/persocom01/TestPython/master/Innocence.jpg', stream=True)

# The status codes are:
# 200	OK
# 301	Moved Permanently
# 302	Moved Temporarily
# 307	Temporary Redirect
# 400	Bad Request
# 403	Forbidden
# 404	Not Found
# 500	Internal Server Error
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
        print(v.errors)
        raise Exception('Wrong value for sex.')

# Demonstrates creation of class.
# User made classes use the UpperCaseCamelCase naming convention.
# In this case a dictionary is used to set instance attributes.


class Animal:
    # Class properties outside the __init__ function are called class
    # variables. They are shared by all instances of the class.
    # They can be overwritten in individual instances, but mutable objects like
    # lists will remain shared.
    subclasses = []

    def __init__(self, dictionary):
        # Class properties inside the __init__ function are called instance
        # variables.
        self.trick = []
        # Demonstrates setting of instance properties from a dictionary.
        for k, v in dictionary.items():
            setattr(self, k, v)

    # The built in class method property() is a special function which you can
    # pass up to 3 special functions, getter(), setter(), and deleter(). We
    # pass getter() by default when we use it as a decorator. If we do not
    # define the other two functions, the property will be effectively read
    # only, as the value cannot be changed or deleted.
    @property
    def food(self):
        if hasattr(self, '_food'):
            return self._food
        else:
            print('the food attribute does not exist')

        # Alternatively:
        # try:
        #     return self._food
        # except AttributeError:
        #     print('the food attribute does not exist')

    # Here we pass the "setter" argument.
    @food.setter
    def food(self, value):
        if not isinstance(value, str):
            raise ValueError('food must be a string')
        else:
            self._food = value

    # Here we determine what happens when we delete the attribute.
    @food.deleter
    def food(self):
        print(f'deleting value "{self._food}" from food attribute')
        del self._food

    # self makes a function usable by instances of the class. Without which,
    # it can only be used by the master class.
    def add_trick(self, trick):
        self.trick.append(trick)
        # Functions can use other functions in the same class by using
        # self.function_name()
        self.sound()

# Demonstrates creation of subclass


class Cat(Animal):
    # A staticmethod is one that can be called without creating an instance of
    # the class.
    @staticmethod
    def description():
        print('a domestic feline')

    def sound(self):
        print('Meow')


# Demonstrates calling a static method.
Cat.description()
Kuro = Cat(cats2[0])

# As this property is mutable, this line will affect the base class.
Kuro.subclasses.append('Cat')
# Class properties can be added at any time just like other languages.
Kuro.food = 'mouse'
del Kuro.food
Kuro.food = 'fish'
Kuro.add_trick('claw rush')

print('shared class list: ', Animal.subclasses)
print(Kuro.name, Kuro.sex, Kuro.color, Kuro.food)
print(Kuro.trick)


# It is also possible for a subclass to inherit from multiple classes.
# In those cases the leftmost superclass takes priority.
