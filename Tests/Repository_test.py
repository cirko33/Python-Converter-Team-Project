from select import select
import unittest, sys
sys.path.insert(0, "..")

from Repository.Repository import read_items
from Repository.Repository import execute_rest
from mysql.connector import Error

class TestRepository(unittest.TestCase):
    def test_succsess(self):
        self.assertAlmostEqual(read_items("select * from korisnik;"), ("korisnik", "*", ((1, 'Luka', 'Ciric', 'lukaciric', 'luka.ciric@yahoo.com'), (2, 'Milorad', 'Markovic', 'mikipaok', 'mikipaok@yahoo.com'), (3, 'Dejan', 'Kurdulija', 'dekikuki', 'kurdulijad@yahoo.com'), (4, 'Zdravko', 'Milinkovic', 'kozdrav', 'milinkovicz@yahoo.com'))))
        self.assertAlmostEqual(execute_rest("insert into korisnik(id, name, lastname, username, email) values('6', 'mika', 'mikic', 'mikaslika', 'mik1@gmail.com')"), ("korisnik", "insert", 1))
        self.assertAlmostEqual(execute_rest("update korisnik set name = 'zika' where lastname='mikic';"), ("korisnik", "update", 1))
        self.assertAlmostEqual(execute_rest("delete from korisnik where id=6;"), ("korisnik", "delete", 1))

    def test_query_value(self):
        self.assertAlmostEqual(read_items("select * from pera;"), ("REJECTED", 3000, "Not valid query for reading data"))
        self.assertAlmostEqual(execute_rest("delete from korisnik where zfssdsda=6;"), ("REJECTED", 3000, "Not valid query for modify data"))
