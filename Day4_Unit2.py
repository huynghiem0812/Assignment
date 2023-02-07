import requests
from lxml import html
from datetime import datetime

current_year = datetime.now().year - 1
url = 'https://www.us-cert.gov/ncas/alerts/' + str(current_year)
for page in range(0, 2):
    req = requests.get(url + '?page=' + str(page))
    doc = html.fromstring(req.text)
    print("The number of security alerts issued by US-CERT in " + str(current_year)+" page " + str(page) + ":")
    print(len(doc.cssselect('.item-list li')))
