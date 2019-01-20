# Demonstrates that imported modules can in turn use imported modules.
import mymodule1

# Optional module information.
__all__ = ['greeting', ]
__version__ = '1.0'
__author__ = 'user'


def greeting(x):
    mymodule1.greeting(x)
    print('how are you?')
