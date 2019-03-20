def time_this(old_fn):
    print('decorating')

    def new_fn(*args, **kwargs):
        print('starting timer')
        import datetime
        before = datetime.datetime.now()
        x = old_fn(*args, **kwargs)
        after = datetime.datetime.now()
        print('Time taken = {}'.format(after - before))
        return x
    return new_fn


def time_all_class_methods(OldCls):
    class NewCls:
        def __init__(self, *args, **kwargs):
            self.oInstance = OldCls(*args, **kwargs)

        def __getattribute__(self, name):
            """
            this is called whenever any attribute of a NewCls object is accessed. This function first tries to
            get the attribute off NewCls. If it fails then it tries to fetch the attribute from self.oInstance (an
            instance of the decorated class). If it manages to fetch the attribute from self.oInstance, and
            the attribute is an instance method then `time_this` is applied.
            """
            try:
                x = super().__getattribute__(name)
            except AttributeError:
                pass
            else:
                print(name)
                return x
            x = self.oInstance.__getattribute__(name)
            if type(x) == type(self.__init__):  # it is an instance method
                # this is equivalent of just decorating the method with time_this
                return time_this(x)
            else:
                return x
    return NewCls


@time_all_class_methods
class Foo(object):
    def a(self, x, y):
        print("entering a")
        import time
        print(x, y)
        time.sleep(y - x)
        print("exiting a")


x = Foo()
x.a(3, 4)

# @time_all_class_methods
# class Student:
#     def __init__(self, name):
#         self.name = name
#
#     # property() is a special function which you can pass up to 3 functions as
#     # arguments:
#     # We pass "getter()" by default when we use it as a decorator.
#     @property
#     def name(self):
#         print('Getting value')
#         return self._name
#
#     # Here we pass the "setter" argument.
#     @name.setter
#     def name(self, val):
#         if not isinstance(val, str):
#             raise ValueError('Name must be a string.')
#         else:
#             print('Setting value')
#             self._name = val
#
#
# x = Student()
# x.name = 'as'
