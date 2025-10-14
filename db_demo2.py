# Практика работы с SQLITE не удалять и не связывать с проектом

import sqlite3

connection = sqlite3.connect('users.db')
cursor = connection.cursor()
cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
id INTEGER PRIMARY KEY  AUTOINCREMENT, 
name TEXT NOT NULL
)
""")
cursor.execute('INSERT INTO users (name) VALUES (?)', ('Alice',))
cursor.execute('INSERT INTO users (name) VALUES (?)', ('Dave',))
cursor.execute('UPDATE users SET name = ? WHERE id = ?', ('Alica', 1))
# cursor.execute('DELETE FROM users')
cursor.execute('DELETE FROM sqlite_sequence WHERE name ="users"')
users_to_add = [('Nick',), ('Sam',), ('John',)]
cursor.executemany('INSERT INTO users (name) VALUES (?)', users_to_add)
users_to_update = [('Scott', 1), ('Jim', 2)]
cursor.executemany('UPDATE users SET name =? WHERE id = ?', users_to_update)



cursor.execute('SELECT * FROM users')
list_of = cursor.fetchall()
print(f'Все: {list_of}')
cursor.execute('SELECT * FROM users WHERE name = "Alice"')
name_alice = cursor.fetchone()
print(f'Только Алис: {name_alice}')
cursor.execute('SELECT * FROM users WHERE name LIKE "S%"')
name_s = cursor.fetchall()
print(f'Только на С: {name_s}')
cursor.execute('SELECT * FROM users WHERE id > 2')
bigger = cursor.fetchall()
print(f'ID больше №2: {bigger}')

cursor.execute('SELECT * FROM users WHERE LENGTH (name) <4')
small_words = cursor.fetchall()
print(f'Меньше 4 символов: {small_words}')
cursor.execute('SELECT * FROM users WHERE id <= 3')
smaller_3 = cursor.fetchall()
print(f'ID меньше №3: {smaller_3}')
cursor.execute('SELECT * FROM users WHERE name LIKE "%t" OR name LIKE "%k"')
name_t_k = cursor.fetchall()
print(f'Заканчивается на Т или К: {name_t_k}')
cursor.execute('SELECT * FROM users ORDER BY name ASC LIMIT 2')
two_first_alfabet = cursor.fetchall()
print(f'Первые два по алфавиту: {two_first_alfabet}')
cursor.execute('SELECT * FROM users WHERE name LIKE "J%" or name LIKE "N%" ORDER BY id DESC LIMIT 3 ')
start_J_N= cursor.fetchall()
print(f'Имя начинается на "J" или "N": {start_J_N}')


connection.commit()
connection.close()
