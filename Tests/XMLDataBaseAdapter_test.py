import unittest, sys
sys.path.insert(0, "..")
from XMLDataBaseAdapter.XMLDataBaseAdapter import convert_to_sql, convert_to_xml

class TestMethods(unittest.TestCase):
    def test_successfull(self):
        self.assertEqual(convert_to_sql('<request>\n\t<verb>GET</verb>\n\t<noun>/korisnik/1</noun>\n\t<fields>id; name; username</fields>\n</request>'), 'select id, name, username from korisnik;')
        self.assertEqual(convert_to_sql('<request>\n\t<verb>GET</verb>\n\t<noun>/student/1</noun>\n\t<query>name=\'Aleksandar\'; type=\'1\'</query>\n\t<fields>id; name; lastname</fields>\n</request>'), 'select id, name, lastname from student where name=\'Aleksandar\' and type=\'1\';')
        self.assertEqual(convert_to_sql('<request>\n\t<verb>DELETE</verb>\n\t<noun>/profesor/1</noun>\n\t<query>name=\'Petar\'; type=\'1\'</query>\n</request>'), 'delete from profesor where name=\'Petar\' and type=\'1\';')
        self.assertEqual(convert_to_sql('<request>\n\t<verb>POST</verb>\n\t<noun>/korisnik/1</noun>\n\t<query>id=\'22\'; name=\'Jovan\'; lastname=\'Jovanovic\'; username=\'jova\'; year_of_study=\'1\'; type=\'1\'</query>\n</request>'), 'insert into korisnik(id, name, lastname, username, year_of_study, type) values(\'22\', \'Jovan\', \'Jovanovic\', \'jova\', \'1\', \'1\');')
        self.assertEqual(convert_to_sql('<request>\n\t<verb>GET</verb>\n\t<noun>/profesor/1</noun>\n\t<query>department=\'EEPSI\'; type=\'1\'</query>\n\t<fields>id; name; lastname; department</fields>\n</request>'), 'select id, name, lastname, department from profesor where department=\'EEPSI\' and type=\'1\';')

        self.assertEqual(convert_to_xml(("korisnik", "insert", 1)), '<response>\n\t<status>SUCCESS</status>\n\t<status_code>2000</status_code>\n\t<payload>1</payload>\n</response>')
        self.assertEqual(convert_to_xml(("korisnik", "update", 1)), '<response>\n\t<status>SUCCESS</status>\n\t<status_code>2000</status_code>\n\t<payload>1</payload>\n</response>')
        self.assertEqual(convert_to_xml(("korisnik", "delete", 1)), '<response>\n\t<status>SUCCESS</status>\n\t<status_code>2000</status_code>\n\t<payload>1</payload>\n</response>')
        self.assertEqual(convert_to_xml(("REJECTED", 3000, "Not valid query for modify data")), '<response>\n\t<status>REJECTED</status>\n\t<status_code>3000</status_code>\n\t<payload>Not valid query for modify data</payload>\n</response>')
        self.assertEqual(convert_to_xml(("REJECTED", 3000, "Not valid query for reading data")), '<response>\n\t<status>REJECTED</status>\n\t<status_code>3000</status_code>\n\t<payload>Not valid query for reading data</payload>\n</response>')
        self.assertEqual(convert_to_xml(("korisnik", "*", ((1, 'Luka', 'Ciric', 'lukaciric', 'luka.ciric@yahoo.com'), (2, 'Dejan', 'Kurdulija', 'dekikuki', 'dejankurdulija00@gmail.com')))), '<response>\n\t<status>SUCCESS</status>\n\t<status_code>2000</status_code>\n\t<payload>\n\t\t<korisnik0>\n\t\t\t<id>1</id>\n\t\t\t<name>Luka</name>\n\t\t\t<lastname>Ciric</lastname>\n\t\t\t<username>lukaciric</username>\n\t\t\t<email>luka.ciric@yahoo.com</email>\n\t\t</korisnik0>\n\t\t<korisnik1>\n\t\t\t<id>2</id>\n\t\t\t<name>Dejan</name>\n\t\t\t<lastname>Kurdulija</lastname>\n\t\t\t<username>dekikuki</username>\n\t\t\t<email>dejankurdulija00@gmail.com</email>\n\t\t</korisnik1>\n\t</payload>\n</response>')