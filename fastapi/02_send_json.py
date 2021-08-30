import requests


def get_url(path, https=False):
    if https:
        domain = 'https://localhost:8000'
    else:
        domain = 'http://localhost:8000'
    return domain + path


json = {
    'string': 'string data',
    'bool': 'no',
    'int': 1.5,
    'direction': 'n'
    }

path = '/pydantic'
r = requests.post(get_url(path, https=False), json=json, verify=False)
print(r.json())
