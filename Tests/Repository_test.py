import sys
sys.path.insert(0, "..")

from Repository.RepositoryMock import database_mock
from mock import patch
from Repository import RepositoryCommands

class TestRepository(database_mock):
    def test_succsess(self):
        with self.mock_db_config:
            self.assertEqual(RepositoryCommands.send_request("select * from korisnik_test;"), ("korisnik_test", "*", [(1, 'Luka', 'Ciric', 'lukaciric', 'luka.ciric@yahoo.com'), (2, 'Milorad', 'Markovic', 'mikipaok', 'mikipaok@yahoo.com'), (3, 'Dejan', 'Kurdulija', 'dekikuki', 'kurdulijad@yahoo.com'), (4, 'Zdravko', 'Milinkovic', 'kozdrav', 'milinkovicz@yahoo.com')]))
            self.assertEqual(RepositoryCommands.send_request("insert into korisnik_test(id, name, lastname, username, email) values('6', 'mika', 'mikic', 'mikaslika', 'mik1@gmail.com')"), ("korisnik_test", "insert", 1))
            self.assertEqual(RepositoryCommands.send_request("update korisnik_test set name = 'zika' where lastname='mikic';"), ("korisnik_test", "update", 1))
            self.assertEqual(RepositoryCommands.send_request("delete from korisnik_test where id=6;"), ("korisnik_test", "delete", 1))

    # def test_query_value(self):
    #     with self.mock_db_config:
    #         self.assertEqual(RepositoryCommands.send_request("select * from pera;"), ("REJECTED", 3000, "Not valid query for reading data"))
    #         self.assertEqual(RepositoryCommands.send_request("delete from korisnik where zfssdsda=6;"), ("REJECTED", 3000, "Not valid query for modify data"))
