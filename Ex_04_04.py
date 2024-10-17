'''
Завдання 4
Створіть агрегатні функції для підрахунку загальної кількості витрат
i прибуткiв за місяць. Забезпечте відповідний інтерфейс користувача.

'''

import sqlite3
import random
conn = sqlite3.connect('ex04.sqlite3')

# cursor = conn.cursor()

def create_table():
    query = '''CREATE TABLE IF NOT EXISTS expenses(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    destination VARCHAR(50),
    expenses REAL,
    time DATE
    );
    '''
    cursor.execute(query)


def add_expenses(destination: str, amount: float, time: str):
    query = '''INSERT INTO expenses (destination, amount, time) VALUES (?, ?, ?);'''
    cursor.execute(query, [destination, amount, time])
    conn.commit()


random.choice(['drugs', 'movies', 'taxi', 'toys'])
round(random.uniform(10, 3000), 2)

if __name__ == '__main__':
    # create_table()

    for i in range(10):
        print(random.choice(['drugs', 'movies', 'taxi', 'toys']), round(random.uniform(10, 3000), 2))