from mysql.connector import Error
import unittest

from Repository import read_items
from Repository import execute_rest

class TestRepository(unittest.TestCase):
    def test_succsess(self):
        self.assertAlmostEqual(read_items("select * from korisnik;"), [(1, 'Luka', 'Ciric', 'lukaciric', 'luka.ciric@yahoo.com'), (2, 'Milorad', 'Markovic', 'mikipaok', 'mikipaok@yahoo.com'), (3, 'Dejan', 'Kurdulija', 'dekikuki', 'kurdulijad@yahoo.com'), (4, 'Zdravko', 'Milinkovic', 'kozdrav', 'milinkovicz@yahoo.com')])
        self.assertAlmostEqual(execute_rest("insert into korisnik(id, name, lastname, username, email) values('6', 'mika', 'mikic', 'mikaslika', 'mik1@gmail.com')"), 1)
        self.assertAlmostEqual(execute_rest("update korisnik set name = 'zika' where lastname='mikic';"), 1)
        self.assertAlmostEqual(execute_rest("delete from korisnik where id=6;"), 1)

    def test_query_value(self):
        # self.assertRaises(Error, read_items, True)
        # self.assertRaises(Error, execute_rest, True)
        self.assertRaises(Exception, read_items, True)
        self.assertRaises(Exception, execute_rest, True)
