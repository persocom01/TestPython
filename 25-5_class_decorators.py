# Demonstrates use of decorators with classes in python.


def time_this(old_fn):
    print('decorating')

    def decorated(*args, **kwargs):
        print('starting timer')
        import datetime
        before = datetime.datetime.now()
        x = old_fn(*args, **kwargs)
        after = datetime.datetime.now()
        print('Time taken = {}'.format(after - before))
        return x
    return decorated

# Demonstrates use of a decorator on a class.


def time_all_class_methods(OldCls):
    class ClassWrapper:
        def __init__(self, *args, **kwargs):
            self.instance = OldCls(*args, **kwargs)

        # This is called whenever an attribute of ClassWrapper is accessed.
        # name is the name of the attribute accessed.
        # Another method of interest is __call__ for when a function is called.
        def __getattribute__(self, name):
            # Tries to see if the attribute called actually exists.
            try:
                x = super().__getattribute__(name)
            except AttributeError:
                pass
            else:
                print(name)
                return x
            x = self.instance.__getattribute__(name)
            # Checks if x is an instance method.
            if type(x) == type(self.__init__):
                # this is equivalent of just decorating the method with time_this.
                return time_this(x)
            else:
                return x
    return ClassWrapper

# Demonstrates use of decorators to set class properties.


@time_all_class_methods
class Student:
    def __init__(self, name):
        self.name = name

    # property() is a special function which you can pass up to 3 functions as
    # arguments:
    # We pass "getter()" by default when we use it as a decorator.
    @property
    def name(self):
        print('Getting value')
        return self._name

    # Here we pass the "setter" argument.
    @name.setter
    def name(self, val):
        if not isinstance(val, str):
            raise ValueError('Name must be a string.')
        else:
            print('Setting value')
            self._name = val

    def greeting(self):
        import time
        print('Hi, my name is', self.name)
        time.sleep(1)


x = Student('Alice')
x.greeting()
