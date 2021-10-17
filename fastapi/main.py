import json
from fastapi import FastAPI, File, UploadFile, Request, WebSocket
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from enum import Enum
from typing import Optional
import pathlib
import uvicorn
import io
import vosk_stt as stt

config_path = './config/config.json'

with open(config_path, 'r') as f:
    config = json.load(f)

stt_model = config['model']
cors = config['cors']
port = config['port']

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


@app.post('/pydantic')
def post_object(data: PydanticTest):
    print('string: ' + data.string)
    print('bool: ' + str(data.bool))
    print('int: ' + str(data.int))
    print('list: ' + str(data.list))
    print('direction: ' + data.direction.name)
    return data


@app.post('/file')
async def post_file(file: UploadFile = File(...)):
    content = await file.read()
    content = content.rstrip()
    print(f'contents of uploaded file {file.filename}:')
    print(content)
    return content


@app.post('/request')
async def return_json(res: Request):
    pass
#     data = await res.json()
#     return data

# By preloading the model, api response time is reduced.
vosk = stt.Vosk(stt_model)


@app.post('/stt')
async def post_audio(file: UploadFile = File(...)):
    content = await file.read()
    with io.BytesIO() as f:
        f.write(content)
        f.seek(0)
        text = vosk.text_from_sound_file(f)
    return text


# @app.post('/audstream')
# async def websocket_endpoint(websocket: WebSocket):
#     await websocket.accept()
#     while True:
#         await asyncio.sleep(0.1)
#         payload = next(measurements)
#         await websocket.send_json(payload)


@app.get('/{query}')
def get_divide_query_by_two(query: float):
    output = query / 2
    return output


# uvicorn main:app --reload
app_name = pathlib.Path(__file__).stem
if __name__ == '__main__':
    uvicorn.run(f'{app_name}:app', host='0.0.0.0', port=port, log_level='debug', ssl_certfile='./config/cert.pem', ssl_keyfile='./config/key.pem')
