'''
Завдання 5
Create an Exchange Rates To USD db using API Monobank (api.monobank.ua).
Do requests via request lib, parse results, write it into db. (3 examples required)
Example: Table - Exchange Rate To USD:

id (INT PRIMARY KEY) - 1, 2, 3, ... currency_name (TEXT) - UAH currency_value (REAL)
- 39.5 current_date (DATETIME) - 10/22/2022 7:00 PM
'''

import requests
import datetime
from bs4 import BeautifulSoup

url = 'https://www.iban.com/currency-codes'
response = requests.get(url)
soup = BeautifulSoup (response.content, 'html.parser')

dd = soup.find(class_='table table-bordered downloads tablesorter').find('tbody')

my_currencies = {}

for cur in dd.find_all('tr'):
  my_currencies[cur.find_all('td')[3].text] = {'country': str(cur.find_all('td')[0].text), 'currency_id': str(cur.find_all('td')[2].text), 'currency_code':  str(cur.find_all('td')[3].text)}


url = 'https://api.monobank.ua/bank/currency'




result = requests.get(url)
# {'currencyCodeA': 840, 'currencyCodeB': 980, 'date': 1729112473, 'rateBuy': 41.05, 'rateSell': 41.4852}
for exchange in result.json():
    print(exchange)
    cur_code = exchange['currencyCodeA']
    if len(str(cur_code)) == 1:
        cur_code = '00' + str(cur_code)
    if len(str(cur_code)) == 2:
        cur_code = '0' + str(cur_code)
    try:
        print(my_currencies.get(str(cur_code))['currency_id'])
    except Exception as e:
        print(e, 'NAN')