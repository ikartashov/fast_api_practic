import sqlite3

from anyio.pytest_plugin import get_runner


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


def add_user(name: str):
    connection = get_connection()
    try:
        cursor = connection.cursor()
        cursor.execute('SELECT * FROM users WHERE name = ?', (name,))
        name_in_base = cursor.fetchall()
        if name_in_base:
            raise ValueError(f'Пользователь {name} уже существует')
        else:
            cursor.execute('INSERT INTO users (name) VALUES (?)', (name,))
            connection.commit()
            return f'Пользователь {name} успешно добавлен'
    finally:
        connection.close()


def get_users():
    connection = get_connection()
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM users')
    rows = cursor.fetchall()
    connection.close()

    all_users = [{"id": row[0], "name": row[1]} for row in rows]
    return all_users


def get_user_by_id(user_id: int):
    connection = get_connection()
    try:
        cursor = connection.cursor()
        cursor.execute('SELECT * FROM users WHERE id = ?', (user_id,))
        user_by_id = cursor.fetchone()
        if user_by_id:
            return f'Запрашиваемый пользователь {user_by_id[1]}'
        else:
            raise ValueError(f'Пользователь под номером {user_id} еще не существует')
    finally:
        connection.close()


def update_user(user_id:int, new_name:str):
    connection = get_connection()
    try:
        cursor = connection.cursor()
        cursor.execute('SELECT * FROM users WHERE id = ?', (user_id,))
        id_in_base = cursor.fetchone()
        if id_in_base:
            cursor.execute('UPDATE users SET name = ? WHERE id = ?', (new_name, user_id))
            connection.commit()
            return f'Пользователь {new_name} успешно обновлен'
        else:
            raise ValueError(f'Пользователь не существует')
    finally:
        connection.close()

def delete_user(user_id:int):
    connection = get_connection()
    try:
        cursor = connection.cursor()
        cursor.execute('SELECT * FROM users WHERE id = ?', (user_id,))
        id_in_base = cursor.fetchone()
        if id_in_base:
            cursor.execute('DELETE FROM users WHERE id = ?', (user_id,))
            connection.commit()
            return f'Пользователь успешно удален'
        else:
            raise ValueError(f'Пользователь еще не существует')
    finally:
        connection.close()
