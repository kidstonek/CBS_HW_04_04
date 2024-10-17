'''
Завдання 4
Створіть агрегатні функції для підрахунку загальної кількості витрат
i прибуткiв за місяць. Забезпечте відповідний інтерфейс користувача.

'''

import sqlite3
import random
conn = sqlite3.connect('ex04.sqlite3')

cursor = conn.cursor()

def create_table():
    query = '''CREATE TABLE IF NOT EXISTS expenses(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    destination VARCHAR(50),
    expenses REAL,
    time DATE,
    profit REAL
    );
    '''
    cursor.execute(query)


def add_expenses(destination: str, expenses: float, time: str, income: float):
    query = '''INSERT INTO expenses (destination, expenses, time, profit) VALUES (?, ?, ?, ?);'''
    cursor.execute(query, [destination, expenses, time, income])
    conn.commit()


random.choice(['drugs', 'movies', 'taxi', 'toys', 'games'])
round(random.uniform(10, 3000), 2)

if __name__ == '__main__':
    create_table()
    print('do you want to fill the db?')
    usr_in = int(input('1 - to fill db, other will leave it blank '))
    if usr_in == 1:
        times = int(input("how many rows do you need?"))
        for i in range(times):
            expenses_for = random.choice(['drugs', 'movies', 'taxi', 'toys', 'games'])
            expenses = round(random.uniform(10, 3000), 2)
            income = round(random.uniform(10, 3000), 2)
            expenses_date = f'{random.randint(1991, 2024)}-{random.randint(1, 12)}-{random.randint(1, 31)}'
            add_expenses(expenses_for, expenses, expenses_date, income)



