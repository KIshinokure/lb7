import sqlite3
import unittest


class TestSimple(unittest.TestCase):

    def test_simple_query(self):
        conn = sqlite3.connect(':memory:')
        cur = conn.cursor()

        # 2. Создаем таблицу
        cur.execute("CREATE TABLE test (id INTEGER, value TEXT)")

        # 3. Добавляем данные
        cur.execute("INSERT INTO test VALUES (1, 'Hello')")
        conn.commit()

        # 4. Проверяем
        cur.execute("SELECT value FROM test WHERE id = 1")
        result = cur.fetchone()[0]

        # 5. Утверждение
        self.assertEqual(result, 'Hello')

        conn.close()


if __name__ == '__main__':
    unittest.main()