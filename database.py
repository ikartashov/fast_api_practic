import sqlite3


def get_connection():
    connection = sqlite3.connect('users_practice.db')
    return connection


def create_table():
    connection = get_connection()
    cursor = connection.cursor()
    cursor.execute(
        'CREATE TABLE IF NOT EXISTS users ('
        'id INTEGER PRIMARY KEY AUTOINCREMENT,'
        'name TEXT NOT NULL)')
    connection.commit()
    connection.close()


def add_user(name:str):
    connection = get_connection()
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM users WHERE name = ?', (name,))
    name_in_base = cursor.fetchall()
    if name_in_base:
        raise ValueError(f'Пользователь {name} уже существует')
    else:
        cursor.execute('INSERT INTO users (name) VALUES (?)', (name,))
        connection.commit()
    connection.close()

def get_users():
    connection = get_connection()
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM users')
    rows = cursor.fetchall()
    connection.close()

    all_users = [{"id": row[0], "name": row[1]} for row in rows]
    return all_users
