# Demonstrates how to send a get request and recieve a text response.
domain = 'localhost:8000'
path = f'{domain}/10.2'


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


# We use verify=False because the api is using a self signed ssl cert that will
# fail verification.
r = send_request(path, verify=False)
# A success retuirns code 200. More infomration here:
# https://developer.mozilla.org/en-US/docs/Web/HTTP/Status
if r.status_code == 200:
    # We use .strip() to remove the " from both ends of the response when
    # parsing as text.
    print(r.text.strip('"'))
else:
    print('request code: ' + str(r.status_code))
