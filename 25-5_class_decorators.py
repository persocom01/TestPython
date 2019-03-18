# Demonstrates use of decorators with classes in python.


class Student:
    def __init__(self, name):
        self.name = name

    @property
    def name(self):
        print('Getting value')
        return self._name

    @name.setter
    def name(self, val):
        if not isinstance(val, str):
            raise ValueError('Name must be a string.')
        else:
            print('Setting value')
            self._name = val


x = Student('Cassy')

print(x.name)
