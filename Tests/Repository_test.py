import sys
sys.path.insert(0, "..")

from Repository.RepositoryMock import database_mock
from mock import patch
from Repository import RepositoryCommands

class TestRepository(database_mock):
    def test_succsess(self):
        with self.mock_db_config:
            self.assertEqual(RepositoryCommands.send_request("select * from korisnik_test;"), ("korisnik_test", "*", [(1, 'Luka', 'Ciric', 'lukaciric', 'luka.ciric@yahoo.com'), (2, 'Milorad', 'Markovic', 'mikipaok', 'mikipaok@yahoo.com'), (3, 'Dejan', 'Kurdulija', 'dekikuki', 'kurdulijad@yahoo.com'), (4, 'Zdravko', 'Milinkovic', 'kozdrav', 'milinkovicz@yahoo.com')]))
            self.assertEqual(RepositoryCommands.send_request("select id, name, username from student_test where year_of_study = 4;"), ("student_test", "id, name, username", [('PR12/2018', 'Nebojsa', 'gorda'), ('PR22/2018', 'Milan', 'mastamozesvasta')]))
            self.assertEqual(RepositoryCommands.send_request("select name, lastname, email from profesor_test where department = 'DEPT';"), ("profesor_test", "name, lastname, email", [('Bojana', 'Despotovic', 'bojanadespotovic@uns.ac.rs')]))
            self.assertEqual(RepositoryCommands.send_request("insert into korisnik_test(id, name, lastname, username, email) values('6', 'mika', 'mikic', 'mikaslika', 'mik1@gmail.com');"), ("korisnik_test", "insert", 1))
            self.assertEqual(RepositoryCommands.send_request("insert into student_test value('RA60/2023', 'Sima', 'Diklic', 'disi', 'd.sima@gmail.com', 1);"), ("student_test", "insert", 1))
            self.assertEqual(RepositoryCommands.send_request("insert into profesor_test value(9, 'Miomir', 'Lisac', 'moma', 'miomirlisac@hotmail.com', 'EEPSI');"), ("profesor_test", "insert", 1))
            self.assertEqual(RepositoryCommands.send_request("update korisnik_test set name = 'zika' where lastname='mikic';"), ("korisnik_test", "update", 1))
            self.assertEqual(RepositoryCommands.send_request("update student_test set year_of_study = 5 where lastname like 'M%';"), ("student_test", "update", 3))
            self.assertEqual(RepositoryCommands.send_request("update profesor_test set department = 'ACS' where username = 'erdeljan';"), ("profesor_test", "update", 1))
            self.assertEqual(RepositoryCommands.send_request("delete from korisnik_test where id=6;"), ("korisnik_test", "delete", 1))
            self.assertEqual(RepositoryCommands.send_request("delete from student_test where id like '%2020';"), ("student_test", "delete", 1))
            self.assertEqual(RepositoryCommands.send_request("delete from profesor_test where department = 'ESI' and username = 'marinas';"), ("profesor_test", "delete", 0))

    def test_query_value(self):
        with self.mock_db_config:
            self.assertEqual(RepositoryCommands.send_request("select * from pera;"), ("REJECTED", 3000, "Not valid query for reading data: 1146 (42S02): Table 'res_test.pera' doesn't exist"))
            self.assertEqual(RepositoryCommands.send_request("select surname from student_test;"), ("REJECTED", 3000, "Not valid query for reading data: 1054 (42S22): Unknown column 'surname' in 'field list'"))
            self.assertEqual(RepositoryCommands.send_request("delete from korisnik_test where zfssdsda=6;"), ("REJECTED", 3000, "Not valid query for modify data: 1054 (42S22): Unknown column 'zfssdsda' in 'where clause'"))
            self.assertEqual(RepositoryCommands.send_request("insert into profesor_test value(1, 'Miomir', 'Lisac', 'moma', 'miomirlisac@hotmail.com', 'EEPSI');"), ("REJECTED", 3000, "Not valid query for modify data: 1062 (23000): Duplicate entry '1' for key 'profesor_test.PRIMARY'"))
            self.assertEqual(RepositoryCommands.send_request("insert into student_test value('PR200/2030', 'Nikola', 'Petrovic', 'vlox', 'dzoni@hotmail.com', 1);"), ("REJECTED", 3000, "Not valid query for modify data: 1062 (23000): Duplicate entry 'vlox' for key 'student_test.username'"))
            self.assertEqual(RepositoryCommands.send_request("insert into korisnik_test value(100, 'Nikola', 'Petrovic', 'dzoni', 'dzoni@hotmail.com', 'EEPSI');"), ("REJECTED", 3000, "Not valid query for modify data: 1136 (21S01): Column count doesn't match value count at row 1"))
            self.assertEqual(RepositoryCommands.send_request("update korisnik_test set id = 'jedan' where id = 1;"), ("REJECTED", 3000, "Not valid query for modify data: 1366 (HY000): Incorrect integer value: 'jedan' for column 'id' at row 1"))
            self.assertEqual(RepositoryCommands.send_request("update profesor_test set email = 'atlagic@uns.ac.rs' where id = 1;"), ("REJECTED", 3000, "Not valid query for modify data: 1062 (23000): Duplicate entry 'atlagic@uns.ac.rs' for key 'profesor_test.email'"))
