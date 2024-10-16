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
import sqlite3


#Looking for the currency codes

url = 'https://www.iban.com/currency-codes'
response = requests.get(url)
soup = BeautifulSoup (response.content, 'html.parser')

dd = soup.find(class_='table table-bordered downloads tablesorter').find('tbody')

my_currencies = {}

for cur in dd.find_all('tr'):
  my_currencies[cur.find_all('td')[3].text] = {'country': str(cur.find_all('td')[0].text), 'currency_id': str(cur.find_all('td')[2].text), 'currency_code':  str(cur.find_all('td')[3].text)}


# Monobank API in use

conn = sqlite3.connect('ex05.sqlite3')

cursor = conn.cursor()

def create_table():
    query = '''CREATE TABLE IF NOT EXISTS exchange(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    currency1_name TEXT,
    currency2_name TEXT,
    currency_value REAL,
    time REAL
    );
    '''
    cursor.execute(query)

create_table()

def add_exchange(cur1: str, cur2: str, currency_value: float, times: str):
    query = '''INSERT INTO exchange(currency1_name, currency2_name, currency_value, time) VALUES (?, ?, ?, ?);'''
    cursor.execute(query, [cur1, cur2, currency_value, times])
    conn.commit()


def receive_all_currences():
    query = "SELECT currency1_name, currency2_name, currency_value, time FROM exchange"
    result = cursor.execute(query)
    return result.fetchall()


url = 'https://api.monobank.ua/bank/currency'

result = requests.get(url)

def currency_code(sample:int):
    if len(str(sample)) == 1:
        sample = '00' + str(sample)
    if len(str(sample)) == 2:
        sample = '0' + str(sample)
    return sample


for exchange in result.json():
    print(exchange)
    cur_code1 = currency_code(exchange['currencyCodeA'])
    cur_code2 = currency_code(exchange['currencyCodeB'])
    try:
        cur_code_1 = my_currencies.get(str(cur_code1))['currency_id']
    except Exception as e:
        cur_code_1 = 'Unknown currency'
    try:
        print(my_currencies.get(str(cur_code2))['currency_id'])
        cur_code_2 = my_currencies.get(str(cur_code2))['currency_id']
    except Exception as e:
        cur_code_2 = 'Unknown currency'
    if exchange.get('rateBuy'):
        cur_val = exchange.get('rateBuy')
    else:
        cur_val = exchange.get('rateCross')
    add_exchange(cur_code_1,cur_code_2, cur_val, exchange.get('date'))
    receive_all_currences() # not tested

