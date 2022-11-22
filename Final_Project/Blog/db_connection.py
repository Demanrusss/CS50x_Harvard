import sqlite3

connection = sqlite3.connect('users.db')
cursor = connection.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS Users
               (id INTEGER, nickname VARCHAR(64), email VARCHAR(120), role INTEGER)''')
connection.commit()
connection.close()