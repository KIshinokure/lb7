import sqlite3

db = sqlite3.connect('simple.db')
cur = db.cursor()

cur.execute("CREATE TABLE IF NOT EXISTS users (id INTEGER, name TEXT, email TEXT)")

cur.execute("CREATE INDEX IF NOT EXISTS idx_email ON users(email)")

cur.execute("DELETE FROM users")

cur.execute("INSERT INTO users VALUES (1, 'Анна', 'anna@mail.ru')")
cur.execute("INSERT INTO users VALUES (2, 'Иван', 'ivan@mail.ru')")

cur.execute("SELECT * FROM users WHERE email = 'ivan@mail.ru'")
print("Найден:", cur.fetchone())

db.commit()
db.close()