import unittest, sys
sys.path.insert(0, "..")
from JsonXmlAdapter.JSONXMLConverter import convert_to_xml, convert_to_json

class TestMethods(unittest.TestCase):
    def test_successfull(self):
        self.assertEqual(convert_to_xml('{"verb": "GET", "noun": "/korisnik/1", "fields": "id; name; username"}'), '<request>\n\t<verb>GET</verb>\n\t<noun>/korisnik/1</noun>\n\t<fields>id; name; username</fields>\n</request>')
        self.assertEqual(convert_to_xml('{"verb": "GET", "noun": "/student/1", "query": "name=\'Aleksandar\'; type=\'1\'", "fields": "id; name; lastname"}'), '<request>\n\t<verb>GET</verb>\n\t<noun>/student/1</noun>\n\t<query>name=\'Aleksandar\'; type=\'1\'</query>\n\t<fields>id; name; lastname</fields>\n</request>')
        self.assertEqual(convert_to_xml('{"verb": "DELETE", "noun": "/profesor/1", "query": "name=\'Petar\'; type=\'1\'"}'), '<request>\n\t<verb>DELETE</verb>\n\t<noun>/profesor/1</noun>\n\t<query>name=\'Petar\'; type=\'1\'</query>\n</request>')
        self.assertEqual(convert_to_xml('{"verb": "POST", "noun": "/korisnik/1", "query": "id=\'22\'; name=\'Jovan\'; lastname=\'Jovanovic\'; username=\'jova\'; year_of_study=\'1\'; type=\'1\'"}'), '<request>\n\t<verb>POST</verb>\n\t<noun>/korisnik/1</noun>\n\t<query>id=\'22\'; name=\'Jovan\'; lastname=\'Jovanovic\'; username=\'jova\'; year_of_study=\'1\'; type=\'1\'</query>\n</request>')
        self.assertEqual(convert_to_xml('{"verb": "GET", "noun": "/profesor/1", "query": "department=\'EEPSI\'; type=\'1\'", "fields": "id; name; lastname; department"}'), '<request>\n\t<verb>GET</verb>\n\t<noun>/profesor/1</noun>\n\t<query>department=\'EEPSI\'; type=\'1\'</query>\n\t<fields>id; name; lastname; department</fields>\n</request>')

        self.assertEqual(convert_to_json('<response>\n\t<verb>GET</verb>\n\t<noun>/korisnik/1</noun>\n\t<fields>id; name; username</fields>\n</response>'), '{"verb": "GET", "noun": "/korisnik/1", "fields": "id; name; username"}')
        self.assertEqual(convert_to_json('<response>\n\t<verb>GET</verb>\n\t<noun>/student/1</noun>\n\t<query>name=\'Aleksandar\'; type=\'1\'</query>\n\t<fields>id; name; lastname</fields>\n</response>'), '{"verb": "GET", "noun": "/student/1", "query": "name=\'Aleksandar\'; type=\'1\'", "fields": "id; name; lastname"}')
        self.assertEqual(convert_to_json('<response>\n\t<verb>DELETE</verb>\n\t<noun>/profesor/1</noun>\n\t<query>name=\'Petar\'; type=\'1\'</query>\n</response>'), '{"verb": "DELETE", "noun": "/profesor/1", "query": "name=\'Petar\'; type=\'1\'"}')
        self.assertEqual(convert_to_json('<response>\n\t<verb>POST</verb>\n\t<noun>/korisnik/1</noun>\n\t<query>id=\'22\'; name=\'Jovan\'; lastname=\'Jovanovic\'; username=\'jova\'; year_of_study=\'1\'; type=\'1\'</query>\n</response>'),'{"verb": "POST", "noun": "/korisnik/1", "query": "id=\'22\'; name=\'Jovan\'; lastname=\'Jovanovic\'; username=\'jova\'; year_of_study=\'1\'; type=\'1\'"}')
        self.assertEqual(convert_to_json('<response>\n\t<verb>GET</verb>\n\t<noun>/profesor/1</noun>\n\t<query>department=\'EEPSI\'; type=\'1\'</query>\n\t<fields>id; name; lastname; department</fields>\n</response>'),'{"verb": "GET", "noun": "/profesor/1", "query": "department=\'EEPSI\'; type=\'1\'", "fields": "id; name; lastname; department"}')
