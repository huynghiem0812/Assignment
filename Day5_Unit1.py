import requests
import openpyxl
from datetime import datetime
from parsel import Selector
import re
import csv
import pandas

current_year = datetime.now().year - 1
url_1 = 'https://www.cisa.gov/uscert/ncas/alerts'
url_2 = 'https://www.cisa.gov/uscert/ncas/alerts/' + str(current_year)

alert_list = []

workbook = openpyxl.Workbook()
worksheet = workbook.active
worksheet.append(['Alert ID', 'Alert Name', 'Release Date', 'Last Revised', 'Tips', 'Alert Link'])

response = requests.get(url_2)
temp_1 = response.text.splitlines()[290:380]
temp_2 = ''.join(temp_1)
selector = Selector(text=temp_2)
temp_3 = selector.xpath('//li').getall()

for alerts in temp_3:
    if len(re.findall('AA\d{2}-[0-9]+[A-Z]', alerts)) > 0:
        alert_list.append(alerts)
count = len(alert_list)

if count == 0:
    print('There are no alerts from US-CERT in ' + str(current_year) + '!')
else:
    for page in range(1, 2):
        alert_list_2 = []
        count_2 = 0
        response = requests.get(url_2 + '?page=' + str(page))
        temp_4 = response.text.splitlines()[290:380]
        temp_5 = ''.join(temp_4)
        selector2 = Selector(text=temp_5)
        temp_6 = selector2.xpath('//li').getall()

        for alerts_2 in temp_6:
            if len(re.findall('AA\d{2}-[0-9]+[A-Z]', alerts_2)) > 0:
                alert_list.append(alerts_2)
                alert_list_2.append(alerts_2)
        count_2 = len(alert_list_2)

        if count_2 <= 29:
            count += count_2
            file1 = open('alerts.csv', 'w', encoding='UTF8', newline='')
            csv_writer = csv.writer(file1)
            csv_writer.writerow(['Alert ID', 'Alert Name', 'Release Date', 'Last Revised', 'Tips', 'Alert Link'])

            for alert in alert_list:
                id = re.findall('AA\d{2}-[0-9]+[A-Z]', alert)[0]

                selector2 = Selector(text=alert)
                name = selector2.xpath('//a[@hreflang="en"]/text()').get()

                link = 'https://www.cisa.gov/uscert/ncas/alerts/' + id

                response = requests.get(link)
                temp_3_1 = response.text.splitlines()[250:400]
                temp_4 = ''.join(temp_3_1)
                selector3 = Selector(text=temp_4)
                temp_5 = selector3.xpath('//div[@class="submitted meta-text"]').get()
                temp_6 = re.findall('(?:January|February|March|April|May|June|July|August|September|October|November|December) [0-9]+, [0-9]+', temp_5)

                release_date = temp_6[0].strip('\"')
                try:
                    last_revised = temp_6[1].strip('\"')
                except IndexError:
                    last_revised = release_date
                tips = 'Not yet'
                csv_writer.writerow([id, name, release_date, last_revised, tips, link])
            file1.close()
            file2 = pandas.read_csv('alerts.csv')
            file2.to_excel('alerts.xlsx', header=True)
