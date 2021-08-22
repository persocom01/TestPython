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
* linter-flake8
* python-autopep8

### General packages:

* atom-beautify
* busy-signal
* file-icons
* intentions
* linter
* minimap
* open_in_cmd
* project-manager
* script

Some of the packages require using pip to install certain modules, so open up cmd and enter:

```
pip install flake8
pip install autopep8

<!-- Anaconda versions -->
conda install -y -c anaconda flake8
conda install -y -c conda-forge autopep8
```

The path `flake8` is installed to may need to be added to windows environmental variables to use `linter-flake8`. The path to the anaconda installation is probably `C:\ProgramData\Anaconda3\Scripts`.

## Known issues

While not an issue in this project itself, python's locale.getpreferredencoding() returns cp1252 in windows. This may cause problems with information from web apis. To rectify this problem insert the following code on top of python files with encoding issues:

```
import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding='utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding='utf-8')
```
