# Demonstrates how to send a get request and recieve a text response.
import requests


def get_url(path, https=False):
    if https:
        domain = 'https://localhost:8000'
    else:
        domain = 'http://localhost:8000'
    return domain + path


path = '/no'
# We use verify=False because the api is using a self signed ssl cert that will
# fail verification.
r = requests.get(get_url(path, https=False), verify=False)
# We use .strip() to remove the " from both ends of the response when parsing
# as text.
print(r.text.strip('"'))
