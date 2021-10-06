# FastAPI

A FastAPI and requests testing playground.

## Installation

1. Create new python environment (optional)

You might want to install FastAPI and all the packages the app needs in a separate environment, which is what venv is for. To create a new environment, open the project folder in cmd admin mode and type:

```
<!-- Non anaconda -->
python -m venv env_name
cd env_name/Scripts/activate

<!-- Ananconda -->
conda create -n env_name python==3.79
```

2. Install dependencies

With the new environment activated, install needed dependencies by entering the following:

```
<!-- Non anaconda -->
pip install fastapi
pip install python-multipart
pip install uvicorn[standard]
pip install requests-toolbelt
pip install vosk

<!-- Ananconda -->
conda install -y -c conda-forge fastapi
conda install -y -c conda-forge python-multipart
conda install -y -c conda-forge uvicorn
conda install -y -c conda-forge requests-toolbelt
<!-- Anaconda does not have a vosk installation -->
```

* `python-multipart` - needed by FastAPI to handle form data.
* `uvicorn` - an ASGI server, which is needed to run a FastAPI app.
* `requests-toolbelt` - provides support to uploading large multipart files without first loading the file into ram.
* `vosk` - the speech recognition toolkit used to covert speech to text (STT).
* `SpeechRecognition` - the api used to convert voice into a wav file.
* `pyaudio` - needed for microphone support.

## Usage

To run a FastAPI app, in the FastAPI project folder enter:

```
uvicorn main:app --reload
```

* `main` - the name of the python file the FastAPI app resides in.
* `app` - the name of the FastAPI app.
* `--reload` - reloads the server on code changes. It is recommended that this only be used during development.

Other popular options include:
* `--port int` - determines the port the api runs on. The default port is 8000.
* `--ssl_certfile path` - Together with the ssl_keyfile, enables https.
* `--ssl_keyfile path` - Together with the ssl_certfile, enables https.

Enter `uvicorn --help` to see all available options.

### Running uvicorn within the app

You may choose to define all custom server parameters inside the application file instead, like this:

```
if __name__ == '__main__':
    uvicorn.run(f'main:app', host='0.0.0.0', port=8000, log_level='debug', ssl_certfile='./cert.pem', ssl_keyfile='./key.pem')
```

In such a case, the server may be started simply by running the python file, for instance `python main.py`.

## Writing the FastAPI file

A minimal FastAPI file looks like this:

```
from fastapi import FastAPI

app = FastAPI()


@app.get('/')
async def root():
    return {'message': 'Hello World'}
```

Where `app` is the name of the app. It affects the command needed to run the file.

This comprises:

1. Importing the FastAPI module
2. Creating the FastAPI instance
3. The path operation
4. The path operation function
5. (optional) custom server parameters

### The path operation

```
@app.get('/{var}')
```

The path defines part of the url needed to use the api. The full url takes the form of `http://example-domain.com<path>`.

1. Fixed and variable paths

Paths can be fixed or variable. Including variables takes the form:

```
@app.get('/{var}')
```

Using a variable in the path creates a variable from the path. These variables are called path parameters and can be used as arguments in the path operation function.

2. Path operations

The `.get` part of the path is the path operation, which can be one of the following HTTP methods:

* post - for receiving data
* get - unlike post, a get operation cannot receive data through a message body. However, path parameters can still be used to 'send' data through a get request. They are limited to about 2000 characters, depending on browser.
* put - for updating data
* delete - for deleting data
* options
* head
* patch
* trace

Path operations are evaluated by the order they appear in the file. For example:

```
@app.get('/me')

@app.get('/{var}')
```

`@app.get('/me')` will be evaluated before `@app.get('/{var}')`, making it possible to match the former even though the latter would match all paths.

### The path operation function

Once the api is reached using the path, the path operation function is activated, which can appear as follows:

```
@app.get('/{var}')
async def get_path_param(var):
    return var
```

The path parameter `var` is passed to the function.

1. Data validation and conversion.

Data validation and conversion of path parameters can be done by defining a python type:

```
@app.get('/{var}')
async def get_path_param(var: float):
    return var
```

An error will be returned if the parameter cannot be converted to the defined type. When converting to the `bool` data type, values like `yes` and `no` are converted to `True` and `False` respectively, even though this is not the behavior of the python `bool()` function.

For json message data, more detailed data validation can be performed using a Pydantic BaseModel to define all expected input:

```
from typing import Optional
from pydantic import BaseModel

class PydanticTest(BaseModel):
    string: str
    bool: Optional[bool]
```

An error will be returned if the parameter cannot be converted to the defined type. Optional data will have value `None`, and other json keys will be ignored. For more information:
* Complex body structures: https://fastapi.tiangolo.com/tutorial/body-multiple-params/
* Detailed data validation: https://pydantic-docs.helpmanual.io/usage/types/

2. Accepting only predefined values

Instead of a data type, you may define a fixed list of values data can be by using the `Enum` class:

```
from enum import Enum

class Direction(str, Enum):
    north = 'n'
    south = 's'
    east = 'e'
    west = 'w'

@app.get('/{var}')
async def get_path_param(var: Direction):
    return f'{var.name}: {var.value}'
```

In this case, the only acceptable path parameters are `n, s, e, w` or the right side values of the Enum class. Within the function, the right side values of the class object can be returned using `var.value`. The left side can be returned using `var.name`.

3. async functions

The function can be `async` or not, depending on whether you will need `await` to use a library in the code. It is not clear when it is necessary to make the function `async`, but known uses for it are when using the `Request` object and when accepting file uploads:

```
from fastapi import Request

@app.post('/request')
async def return_json(req: Request):
   data = await req.json()
   return data

from fastapi import File, UploadFile

@app.post('/file')
async def post_file(file: UploadFile = File(...)):
   content = await file.read()
   content = content.rstrip()
   return content
```

This is because retrieving the data from the `Request` object requires use of `await`.

## Documentation

FastAPI generates automatic documentation of the api at `/docs` or an alternative at `/redoc`.

## Known issues

As of 6 Oct 2021, the `pyaudio` module only works up to python 3.6 or using anaconda to install it.
