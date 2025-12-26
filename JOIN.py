import sqlite3

db = sqlite3.connect(':memory:')
cur = db.cursor()

cur.execute("CREATE TABLE users (id INTEGER, name TEXT)")
cur.execute("CREATE TABLE orders (id INTEGER, user_id INTEGER, product TEXT)")

cur.execute("INSERT INTO users VALUES (1, 'Анна')")
cur.execute("INSERT INTO users VALUES (2, 'Иван')")

cur.execute("INSERT INTO orders VALUES (1, 1, 'Книга')")
cur.execute("INSERT INTO orders VALUES (2, 1, 'Ручка')")
cur.execute("INSERT INTO orders VALUES (3, 2, 'Тетрадь')")

cur.execute('''
SELECT users.name, orders.product 
FROM users 
JOIN orders ON users.id = orders.user_id
''')

print("Кто что заказал:")
for name, product in cur.fetchall():
    print(f"{name}: {product}")

db.close()