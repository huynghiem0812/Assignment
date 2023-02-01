import requests
from bs4 import BeautifulSoup

url = 'https://en.wikipedia.org/wiki/Tenterfield,_New_South_Wales'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

for img in soup.find_all('img'):
    img_url = img.get('src')
    if 'http' not in img_url:
        img_url = 'https:' + img_url
    print(img_url)
    with open(img_url.split("/")[-1], 'wb') as f:
        response = requests.get(img_url)
        f.write(response.content)