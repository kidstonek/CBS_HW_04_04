'''
Завдання 4
Створіть агрегатні функції для підрахунку загальної кількості витрат
i прибуткiв за місяць.
Забезпечте відповідний інтерфейс користувача.

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


def search_expenses(needed_period: str):
    query = f'''SELECT 
    SUM(expenses) AS total_expenses, 
    SUM(profit) AS total_profit, 
    (SUM(expenses) - SUM(profit)) AS tot
    FROM expenses e 
    WHERE time LIKE ?;
    '''
    result = cursor.execute(query, [needed_period])
    return result.fetchall()


def expenses_date_():
    tmp_year = random.randint(2000, 2024)
    mnt = random.randint(1, 12)
    dayy = random.randint(1, 31)
    tmp_month = '0' + str(mnt) if mnt < 10 else mnt
    tmp_day = '0' + str(dayy) if dayy < 10 else dayy
    return f'{tmp_year}-{tmp_month}-{tmp_day}'


if __name__ == '__main__':
    create_table()
    print('do you want to fill the db?')
    usr_in = input('1 - to fill db, other will leave it blank ')
    if usr_in == '1':
        times = int(input("how many rows do you need? "))
        for i in range(times):
            expenses_for = random.choice(['drugs', 'movies', 'taxi', 'toys', 'games'])
            expenses = round(random.uniform(10, 3000), 2)
            income = round(random.uniform(10, 3000), 2)
            expenses_date = expenses_date_()
            add_expenses(expenses_for, expenses, expenses_date, income)
        print('the data was added')
    while True:
        print('if you want to see type:\n1 - expenses and income for exect period')
        usr_input = input("what you decide?: ")
        if usr_input == '1':
            usr_year = input('input needed year (XXXX): ')
            usr_month = input('input number for the month: ')
            if int(usr_month) < 10:
                usr_month = '0' + usr_month
            my_question_time = f"{usr_year}%-{usr_month}-%"
            answer = search_expenses(my_question_time)
            print(answer[0])
            print(f'In year {usr_year} and {usr_month} your balance was: income {answer[0][1]}, you have spent {answer[0][0]}')
            print(f'In TOTAL: {answer[0][2]}')
            input('....')
        else:
            print('bye')
            break


