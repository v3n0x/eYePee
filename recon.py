#!/usr/bin/python

import requests, argparse, sys
from bs4 import BeautifulSoup

parser = argparse.ArgumentParser()
parser.add_argument('--ip', '-i', help='Enter IP address for recon', type=str)
args = parser.parse_args("--ip 1.1.1.1".split())

def eYePee(ip):
    headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) QtWebEngine/5.15.10 Chrome/87.0.4280.144 Safari/537.36'}
    url = f'https://db-ip.com/{ip}'
    response = requests.get(url, headers)
    html_code = response.text
    soup = BeautifulSoup(html_code, 'html.parser')
    table = soup.find('table', {'class': 'table light tcol-33 mb-3'})
    info = soup.find_all('p')[0].string
    header = []
    rows = []

    for i, row in enumerate(table.find_all('tr')):
        if i == 0:
            header = [el.text.strip() for el in row.find_all('th')]
        else:
            rows.append([el.text.strip() for el in row.find_all('td')])

    for row in rows: return(info + '\n* '+header[0]+':'+row[0]+'\n* '+header[1]+':'+row[1]+'\n* '+header[2]+':'+row[2])

print(eYePee(args.ip))
