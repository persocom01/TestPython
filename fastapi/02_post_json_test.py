# Demonstrates how to send json messages with the request body.


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


json = {
    'string': 'string data',
    'bool': 'no',
    'int': 1.5,
    'direction': 'n'
    }

domain = 'localhost:8000'
path = f'{domain}/pydantic'
r = send_request(path, post=True, json=json, verify=False)
if r.status_code == 200:
    print(r.json())
else:
    print('request code: ' + str(r.status_code))
