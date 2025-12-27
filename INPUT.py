import sqlite3

conn = sqlite3.connect('contacts.db')
cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS contacts (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    phone TEXT
)
''')

while True:
    name = input("Введите имя (или 'стоп' для выхода): ")
    if name.lower() == 'стоп':
        break

    phone = input("Введите телефон: ")

    cursor.execute("INSERT INTO contacts (name, phone) VALUES (?, ?)", (name, phone))
    print(f"Контакт '{name}' добавлен!\n")

print("\nВсе контакты:")
cursor.execute("SELECT * FROM contacts")
for contact in cursor.fetchall():
    print(f"{contact[0]}. {contact[1]}: {contact[2]}")

conn.commit()
conn.close()