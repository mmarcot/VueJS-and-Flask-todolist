import sqlite3

connection = sqlite3.connect('database.db')

with open('schema.sql') as f:
    connection.executescript(f.read())

cur = connection.cursor()

cur.execute("INSERT INTO todoitems (content) VALUES (?)", ('Content for the first post',))
cur.execute("INSERT INTO todoitems (content) VALUES (?)", ('Second Post',))
cur.execute("INSERT INTO todoitems (content) VALUES (?)", ("Hello world",))

connection.commit()
connection.close()