import json
from fastapi import FastAPI, File, UploadFile, Request, WebSocket
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from enum import Enum
from typing import Optional
import pathlib
import uvicorn
import base64
import time
import modules.vosk_stt.vosk as stt

config_path = './config/config.json'

try:
    with open(config_path, 'r') as f:
        config = json.load(f)
except Exception as e:
    print(f'error reading config file: {e}')

# Models can be found from: https://alphacephei.com/vosk/models
stt_model = config['model'] or './model'
cors = config['cors'] or ['*']
port = config['port'] or 8000
certfile = config['https']['certfile'] or './cert.pem'
keyfile = config['https']['keyfile'] or './key.pem'

app = FastAPI()

# Cross origin error is something you may encounter when the browser attempts
# to access the api in a different origin, which is a combination of protocol
# (http, https), domain (myapp.com, localhost, localhost.myapp.com), and port
# (80, 443, 8080). Using CORSMiddleware allows you to define permitted domains
# Documentation here: https://fastapi.tiangolo.com/tutorial/cors/
app.add_middleware(
    CORSMiddleware,
    allow_origins=cors,
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*'],
)


class Direction(str, Enum):
    north = 'n'
    south = 's'
    east = 'e'
    west = 'w'


class PydanticTest(BaseModel):
    string: str
    bool: bool
    int: int
    list: Optional[list] = None
    direction: Direction


@app.get(config['commands']['get_help'] or '/')
def get_help():
    return config['commands']


@app.get(config['commands']['get_divide_query_by_two'] or '/{query}')
def get_divide_query_by_two(query: float):
    output = query / 2
    return output


@app.post(config['commands']['post_pydantic'] or '/pydantic')
def post_object(data: PydanticTest):
    print('post json with data validation')
    print('string: ' + data.string)
    print('bool: ' + str(data.bool))
    print('int: ' + str(data.int))
    print('list: ' + str(data.list))
    print('direction: ' + data.direction.name)
    return data


@app.post(config['commands']['post_file'] or '/file')
async def post_file_upload(file: UploadFile = File(...)):
    print('post file')
    # This is the async way to get file contents according to:
    # https://fastapi.tiangolo.com/tutorial/request-files/
    # You can also get the file contents by using non async file.file.read(),
    # or pass the whole file using file.file.
    # content = file.file.read()
    content = await file.read()
    content = content.rstrip()
    print(f'file {file.filename} contents:')
    print(content.decode('utf-8'))
    return content


@app.post(config['commands']['post_encoded_file'] or '/_file')
def post_encoded_file(file: bytes = File(...)):
    print('post encoded bytes file')
    try:
        content = base64.b64decode(file).decode()
        encoded_message = file.decode()
        print('encoded contents:')
        print(encoded_message)
        print()
    except base64.binascii.Error:
        content = file.decode()
    content = content.rstrip()
    print('file contents:')
    print(content)
    return content


@app.post(config['commands']['post_request'] or '/req')
async def return_json(res: Request):
    pass
#     data = await res.json()
#     return data

# By preloading the model, api response time is reduced.
vosk = stt.Vosk(stt_model)


@app.post(config['commands']['post_speech2text'] or '/stt')
def post_audio(file: UploadFile = File(...)):
    start = time.time()
    with file.file as f:
        text = vosk.text_from_sound_file(f)
    print(f'[vosk_stt]speech to text: {text}')
    end = time.time()
    total = start - end
    print(f'[vosk_stt]transcription time: {total}')
    return text


# @app.post('/audstream')
# async def websocket_endpoint(websocket: WebSocket):
#     await websocket.accept()
#     while True:
#         await asyncio.sleep(0.1)
#         payload = next(measurements)
#         await websocket.send_json(payload)


# uvicorn main:app --reload
app_name = pathlib.Path(__file__).stem
if __name__ == '__main__':
    if config['https']['enabled']:
        uvicorn.run(f'{app_name}:app', host='0.0.0.0', port=port, log_level='debug', ssl_certfile=f'{certfile}', ssl_keyfile=f'{keyfile}')
    else:
        uvicorn.run(f'{app_name}:app', reload=True)
