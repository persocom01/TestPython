# Demonstrates that imported modules can in turn use imported modules.
import file_module1

# Optional module information.
__all__ = ['name2', ]
__version__ = '1.0'
__author__ = 'user'


def name2():
    file_module1.name('file_module2')
