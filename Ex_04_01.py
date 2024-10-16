'''
Завдання 1
Зробіть таблицю для підрахунку особистих витрат із такими полями: id, призначення, сума, час.
'''


import sqlite3

conn = sqlite3.connect('ex01.sqlite3')

cursor = conn.cursor()

def create_table():
    query = '''CREATE TABLE IF NOT EXISTS expenses(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    destination VARCHAR(50),
    amount REAL,
    time DATE
    );
    '''
    cursor.execute(query)



if __name__ == '__main__':
    create_table()