# Demonstrates how to send files with the request body.
from requests_toolbelt import MultipartEncoder
import os


def send_request(path, post=False, **kwargs):
    import requests
    http = f'http://{path}'
    https = f'https://{path}'
    if post:
        try:
            request = requests.post(http, **kwargs)
        except requests.exceptions.ConnectionError:
            print('http request failed, trying https...')
            request = requests.post(https, **kwargs)
    else:
        try:
            request = requests.get(http, **kwargs)
        except requests.exceptions.ConnectionError:
            print('http request failed, trying https...')
            request = requests.get(https, **kwargs)
    return request


filepath = './fastapi/upload1.txt'
domain = 'localhost:8000'
path = f'{domain}/file'

with open(filepath, 'rb') as f:
    filename = os.path.basename(f.name)
    encoder = MultipartEncoder({'file': (filename, f)})
    # We use MultipartEncoder here because it is superior to how requests
    # handles a multipart encoded file. For simile files the following code
    # is sufficient:
    r = send_request(path, post=True, files={filename: f}, verify=False)
    # r = send_request(path, post=True, data=encoder, headers={'Content-Type': encoder.content_type}, verify=False)

if r.status_code == 200:
    print(r.text.strip('"'))
else:
    print('request code: ' + str(r.status_code))
