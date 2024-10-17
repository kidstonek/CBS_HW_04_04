'''Завдання 2
Створіть консольний інтерфейс (CLI) на Python для додавання нових записів до бази даних.'''

import sqlite3

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
    query = '''INSERT INTO expenses (destination, amount, time) VALUES (?, ?, ?);'''
    cursor.execute(query, [destination, amount, time])
    conn.commit()

def correct_date():
    year = input('please provide year: ')
    month = ''
    day = ''

    while True:
        month = int(input('please provide number of the month: '))
        if 0 < int(month) <= 12:
            if int(month) < 10:
                month = '0' + str(month)
            break
        else:
            print('Incorrect input - should be from 1 to 12')

    while True:
        day = int(input('please provide number of the day: '))
        if month != '02':
            if 0 < day <= 31:
                day = '0' + str(day) if day < 10 else str(day)
                break
            else:
                print('Incorrect input - should be from 1 to 31')
        else:
            if 0 < day <= 28:
                day = '0' + str(day) if day < 10 else str(day)
                break
            else:
                print('Incorrect input - should be from 1 to 28')

    return f'{year}-{month}-{day}'

if __name__ == '__main__':
    create_table()
    while True:
        print('Please tell me what you gonna do')
        usr_input = input('for add expenses - 1, for exit any button ')
        if usr_input == '1':
            print('Here we go')
            usr_destination = input('what was the money used for? ')
            usr_amount = float(input('what was the amount? '))
            usr_time = correct_date()
            add_expenses(usr_destination, usr_amount, usr_time)
        else:
            print('bye')
            break

