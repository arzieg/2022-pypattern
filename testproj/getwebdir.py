# https://www.codegrepper.com/code-examples/python/list+all+the+directory+in+a+website+using+python
import requests
from bs4 import BeautifulSoup

def get_url_paths(url, ext='', params={}):
    response = requests.get(url, params=params)
    if response.ok:
        response_text = response.text
    else:
        return response.raise_for_status()
    soup = BeautifulSoup(response_text, 'html.parser')
    parent = [url + node.get('href') for node in soup.find_all('a') if node.get('href').endswith(ext)]
    return parent

url = 'https://cdimage.debian.org/debian-cd/11.2.0-live/amd64/iso-hybrid/'
ext = 'iso'
result = get_url_paths(url, ext)
for i in result:
    print(i)
