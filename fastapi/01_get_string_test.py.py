# Demonstrates how to send a get request and recieve a text response.
domain = 'http://localhost:8000'
path = f'{domain}/10.2'


def send_request(path, post=False, **kwargs):
    import requests
    if post:
        try:
            request = requests.post(path, **kwargs)
        except requests.exceptions.ConnectionError as e:
            print('http(s) request failed, perhaps try the other...')
            raise e
    else:
        try:
            request = requests.get(path, **kwargs)
        except requests.exceptions.ConnectionError as e:
            print('http(s) request failed, perhaps try the other...')
            raise e
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
