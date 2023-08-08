#!/usr/bin/python

import requests
from bs4 import BeautifulSoup

site  = 'https://db-ip.com/'
ip  = input('Enter IP: ')
url = site + ip

response = requests.get(url)
html_code = response.text

soup = BeautifulSoup(html_code, 'html.parser')

#print(soup.prettify)

table = soup.find('table', {"class": "table light tcol-33 mb-3"})

print('\n'+soup.find_all('p')[0].string+'\n')

header = []
rows = []

for i, row in enumerate(table.find_all('tr')):
    if i == 0:
        header = [el.text.strip() for el in row.find_all('th')]
    else:
        rows.append([el.text.strip() for el in row.find_all('td')])

for row in rows: print('* '+header[0]+':'+row[0]+'\n* '+header[1]+':'+row[1]+'\n* '+header[2]+':'+row[2])
