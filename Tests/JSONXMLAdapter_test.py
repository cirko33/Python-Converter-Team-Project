import unittest
from JsonXmlAdapter.JSONXMLAdapter import ConvertToXML, ConvertToJSON

class TestMethods(unittest.TestCase):
    def test_successfull(self):
        self.assertEqual(ConvertToXML('{"verb": "GET", "noun": "/resurs/1", "fields": "id; name; email"}'), '<request>\n\t<verb>GET</verb>\n\t<noun>/resurs/1</noun>\n\t<fields>id; name; email</fields>\n</request>')
        self.assertEqual(ConvertToXML('{"verb": "GET", "noun": "/resurs/1", "query": "name=\'pera\'; type=1", "fields": "id; name; lastname"}'), '<request>\n\t<verb>GET</verb>\n\t<noun>/resurs/1</noun>\n\t<query>name=\'pera\'; type=1</query>\n\t<fields>id; name; lastname</fields>\n</request>')
        self.assertEqual(ConvertToXML('{"verb": "DELETE", "noun": "/resurs/1", "query": "name=\'pera\'; type=1", "fields": "id; name; lastname"}'), '<request>\n\t<verb>DELETE</verb>\n\t<noun>/resurs/1</noun>\n\t<query>name=\'pera\'; type=1</query>\n\t<fields>id; name; lastname</fields>\n</request>')
        self.assertEqual(ConvertToXML('{"verb": "POST", "noun": "/resurs/1", "query": "username=\'dekikuki\'; type=1", "fields": "id; name; lastname; username"}'), '<request>\n\t<verb>POST</verb>\n\t<noun>/resurs/1</noun>\n\t<query>username=\'dekikuki\'; type=1</query>\n\t<fields>id; name; lastname; username</fields>\n</request>')
        self.assertEqual(ConvertToXML('{"verb": "GET", "noun": "/resurs/1", "query": "department=\'EEPSI\'; type=1", "fields": "id; name; lastname; department"}'), '<request>\n\t<verb>GET</verb>\n\t<noun>/resurs/1</noun>\n\t<query>department=\'EEPSI\'; type=1</query>\n\t<fields>id; name; lastname; department</fields>\n</request>')

        self.assertEqual(ConvertToJSON('<response>\n\t<verb>GET</verb>\n\t<noun>/resurs/1</noun>\n\t<fields>id; name; email</fields>\n</response>'), '{"verb": "GET", "noun": "/resurs/1", "fields": "id; name; email"}')
        self.assertEqual(ConvertToJSON('<response>\n\t<verb>GET</verb>\n\t<noun>/resurs/1</noun>\n\t<query>name=\'pera\'; type=1</query>\n\t<fields>id; name; lastname</fields>\n</response>'), '{"verb": "GET", "noun": "/resurs/1", "query": "name=\'pera\'; type=1", "fields": "id; name; lastname"}')
        self.assertEqual(ConvertToJSON('<response>\n\t<verb>DELETE</verb>\n\t<noun>/resurs/1</noun>\n\t<query>name=\'pera\'; type=1</query>\n\t<fields>id; name; lastname</fields>\n</response>'), '{"verb": "DELETE", "noun": "/resurs/1", "query": "name=\'pera\'; type=1", "fields": "id; name; lastname"}')
        self.assertEqual(ConvertToJSON('<response>\n\t<verb>POST</verb>\n\t<noun>/resurs/1</noun>\n\t<query>username=\'dekikuki\'; type=1</query>\n\t<fields>id; name; lastname; username</fields>\n</response>'),'{"verb": "POST", "noun": "/resurs/1", "query": "username=\'dekikuki\'; type=1", "fields": "id; name; lastname; username"}')
        self.assertEqual(ConvertToJSON('<response>\n\t<verb>GET</verb>\n\t<noun>/resurs/1</noun>\n\t<query>department=\'EEPSI\'; type=1</query>\n\t<fields>id; name; lastname; department</fields>\n</response>'),'{"verb": "GET", "noun": "/resurs/1", "query": "department=\'EEPSI\'; type=1", "fields": "id; name; lastname; department"}')
