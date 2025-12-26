import sqlite3

conn = sqlite3.connect('shop.db')
cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS products (
    id INTEGER PRIMARY KEY,
    name TEXT,
    price REAL
)
''')

products = [
    ('Хлеб', 50.5),
    ('Молоко', 80.0),
    ('Яблоки', 120.0)
]

cursor.executemany("INSERT INTO products (name, price) VALUES (?, ?)", products)

cursor.execute("SELECT * FROM products WHERE price > ?", (70,))
expensive = cursor.fetchall()
print("Дорогие товары:", expensive)

conn.commit()
conn.close()