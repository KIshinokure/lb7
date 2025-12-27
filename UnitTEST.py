import sqlite3
import unittest


class TestSimple(unittest.TestCase):

    def test_simple_query(self):
        conn = sqlite3.connect(':memory:')
        cur = conn.cursor()

        cur.execute("CREATE TABLE test (id INTEGER, value TEXT)")

        cur.execute("INSERT INTO test VALUES (1, 'Hello')")
        conn.commit()

        cur.execute("SELECT value FROM test WHERE id = 1")
        result = cur.fetchone()[0]

        self.assertEqual(result, 'Hello')

        conn.close()


if __name__ == '__main__':
    unittest.main()