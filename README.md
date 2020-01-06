# TestPython

A python testing playground organized by topic in the python tutorial: https://docs.python.org/3/tutorial/index.html

Workable code is written on each topic to demonstrate use of python in the topic area.

## Installation

pipenv was used to install some modules in this project. As such, there is a need to open it in a virtual development environment.

I use the atom ide, and open this project by opening cmd in the project folder and typing:

pipenv shell

pipenv run atom

### Atom packages used:

* Hydrogen
* atom-ide-debugger-python
* linter-flake8
* python-autopep8
* python-debugger

### General packages:

* atom-beautify
* busy-signal
* file-icons
* intentions
* minimap
* open_in_cmd
* project-manager
* script

## Noted issues

Python's locale.getpreferredencoding() returns cp1252 in windows. This may cause problems with information from certain web apis. To rectify this problem, type:

import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding='utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding='utf-8')
