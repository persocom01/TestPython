# TestPython

A python testing playground organized by topic in the python tutorial: https://docs.python.org/3/tutorial/index.html

Workable code is written on each topic to demonstrate use of python in the topic area.

## Installation

python has to be downloaded and installed. Atom was used as text editor.

* [python 3.8.1](https://www.python.org/downloads/)
* [atom 1.43.0](https://atom.io/)

pipenv was used to install some modules in this project. As such, there is a need to open atom in the pipenv virtual development environment. To do so, open cmd in the project folder and type:

```
pipenv shell
pipenv run atom
```

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

## Known issues

While not an issue in this project itself, python's locale.getpreferredencoding() returns cp1252 in windows. This may cause problems with information from web apis in other python projects. To rectify this problem insert the following code on top of python files with encoding issues:

```
import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding='utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding='utf-8')
```
