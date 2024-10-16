'''Завдання 2
Створіть консольний інтерфейс (CLI) на Python для додавання нових записів до бази даних.'''

import sqlite3
from datetime import datetime

conn = sqlite3.connect('ex02.sqlite3')

cursor = conn.cursor()

def create_table():
    query = '''CREATE TABLE IF NOT EXISTS expenses(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    destination VARCHAR(50),
    amount REAL,
    time REAL
    );
    '''
    cursor.execute(query)

def add_expenses(destination: str, amount: float, time: str):
    # query = '''INSERT INTO TABLE expenses(destination, amount, time) VALUES (?,?,?);
    # '''
    query = '''INSERT INTO expenses (destination, amount, time) VALUES (?, ?, ?);'''
    cursor.execute(query, [destination, amount, time])
    conn.commit()

if __name__ == '__main__':
    create_table()
    while True:
        print('Please tell me what you gonna do')
        usr_input = input('for add expenses - 1, for exit any button ')
        if usr_input == '1':
            print('Here we go')
            usr_destination = input('what was the money used for? ')
            usr_amount = float(input('what was the amount? '))
            usr_time = input('when it was? (in format DayMonthYear)')
            add_expenses(usr_destination, usr_amount, usr_time)
        else:
            print('bye')
            break

