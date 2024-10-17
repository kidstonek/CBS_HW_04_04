'''
Завдання 3
Змініть таблицю так, щоби можна було додати не лише витрати, а й прибутки.
'''

import sqlite3

conn = sqlite3.connect('ex03.sqlite3')

cursor = conn.cursor()

def create_table():
    query = '''CREATE TABLE IF NOT EXISTS expenses(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    destination VARCHAR(50),
    expenses REAL,
    time DATE
    );
    '''
    cursor.execute(query)

def add_column_to_table():
    query = '''ALTER TABLE expenses ADD COLUMN profit INTEGER;'''
    cursor.execute(query)


if __name__ == '__main__':
    create_table()
    add_column_to_table()