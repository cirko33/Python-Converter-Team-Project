import unittest, sys
sys.path.insert(0, "..")
from ComBus.CheckFormat import check_xml_format

class TestCheckFormat(unittest.TestCase):
    def test_succsess(self):
        self.assertEqual(check_xml_format('<response>\n\t<verb>GET</verb>\n\t<noun>/korisnik/1</noun>\n\t<fields>id; name; username</fields>\n</response>'), "")
        self.assertEqual(check_xml_format('<response>\n\t<verb>GET</verb>\n\t<noun>/student/1</noun>\n</response>'), "")
        self.assertEqual(check_xml_format('<response>\n\t<verb>GET</verb>\n\t<noun>/student/1</noun>\n\t<query>name=\'Aleksandar\'; type=\'1\'</query>\n\t<fields>id; name; lastname</fields>\n</response>'), "")
        self.assertEqual(check_xml_format('<response>\n\t<verb>DELETE</verb>\n\t<noun>/profesor/1</noun>\n\t<query>name=\'Petar\'; type=\'1\'</query>\n</response>'), "")
        self.assertEqual(check_xml_format('<response>\n\t<verb>POST</verb>\n\t<noun>/korisnik/1</noun>\n\t<query>id=\'22\'; name=\'Jovan\'; lastname=\'Jovanovic\'; username=\'jova\'; year_of_study=\'1\'; type=\'1\'</query>\n</response>'), "")
        self.assertEqual(check_xml_format('<response>\n\t<verb>GET</verb>\n\t<noun>/profesor/1</noun>\n\t<query>department=\'EEPSI\'; type=\'1\'</query>\n\t<fields>id; name; lastname; department</fields>\n</response>'), "")
        self.assertEqual(check_xml_format('<request>\n\t<verb>PATCH</verb>\n\t<noun>/profesor/1</noun>\n\t<query>name=\'Luka\'; department=\'EEPSI\'</query>\n\t<fields>department=\'ACS\'</fields>\n</request>'), "")

    def test_failure(self):
        self.assertEqual(check_xml_format('<response>\n\t<noun>/korisnik/1</noun>\n\t<fields>id; name; username</fields>\n</response>'), "<response><status>BAD_FORMAT</status><status_code>5000</status_code><payload>Verb and noun are required</payload></response>")
        self.assertEqual(check_xml_format('<response>\n\t<verb>GET</verb>\n\t<fields>id; name; username</fields>\n</response>'), "<response><status>BAD_FORMAT</status><status_code>5000</status_code><payload>Verb and noun are required</payload></response>")
        self.assertEqual(check_xml_format('<response>\n\t<verb>ADD</verb>\n\t<noun>/student/1</noun>\n\t<query>name=\'Aleksandar\'; type=\'1\'</query>\n\t<fields>id; name; lastname</fields>\n</response>'), "<response><status>BAD_FORMAT</status><status_code>5000</status_code><payload>Verb not valid</payload></response>")
        self.assertEqual(check_xml_format('<response>\n\t<verb>POST</verb>\n\t<noun>/korisnik/1</noun>\n</response>'), "<response><status>BAD_FORMAT</status><status_code>5000</status_code><payload>Query is required for POST verb</payload></response>")
        self.assertEqual(check_xml_format('<response>\n\t<verb>GET</verb>\n\t<noun>/student/1</noun>\n\t<query>name=\'Aleksandar\'; study_of_year>\'1\'</query>\n\t<fields>id; name; lastname</fields>\n</response>'), "<response><status>BAD_FORMAT</status><status_code>5000</status_code><payload>Invalid characters in query</payload></response>")
        self.assertEqual(check_xml_format('<response>\n\t<verb>DELETE</verb>\n\t<noun>/profesor/1</noun>\n\t<query>name \'Petar\'; type=\'1\'</query>\n</response>'), "<response><status>BAD_FORMAT</status><status_code>5000</status_code><payload>Missing '=' in query</payload></response>")
        self.assertEqual(check_xml_format('<request>\n\t<verb>PATCH</verb>\n\t<noun>/profesor/1</noun>\n\t<query>name=\'Luka\'; department=\'EEPSI\'</query>\n</request>'), "<response><status>BAD_FORMAT</status><status_code>5000</status_code><payload>Fields are required for PATCH verb</payload></response>")
        self.assertEqual(check_xml_format('<response>\n\t<verb>DELETE</verb>\n\t<noun>/korisnik/1</noun>\n\t<query>name=\'Petar\'; type=\'1\'</query>\n\t<fields>id; username;</fields>\n</response>'), "<response><status>BAD_FORMAT</status><status_code>5000</status_code><payload>DELETE can't have fields</payload></response>")
        self.assertEqual(check_xml_format('<request>\n\t<verb>PATCH</verb>\n\t<noun>/student/1</noun>\n\t<query>name=\'Luka\'; username=\'luksuza\'</query>\n\t<fields>*=\'ACS\'</fields>\n</request>'), "<response><status>BAD_FORMAT</status><status_code>5000</status_code><payload>Invalid character in patch fields</payload></response>")
        self.assertEqual(check_xml_format('<request>\n\t<verb>PATCH</verb>\n\t<noun>/student/1</noun>\n\t<query>name=\'Luka\'; username=\'luksuza\'</query>\n\t<fields>lastname \'Ciric\'</fields>\n</request>'), "<response><status>BAD_FORMAT</status><status_code>5000</status_code><payload>Missing '=' in patch fields</payload></response>")
        self.assertEqual(check_xml_format('<request>\n\t<verb>GET</verb>\n\t<noun>/korisnk/1</noun>\n\t<query>name=\'Luka\'; username=\'luksuza\'</query>\n\t<fields>lastname=\'Ciric\'</fields>\n</request>'), "<response><status>BAD_FORMAT</status><status_code>5000</status_code><payload>Invalid character in fields</payload></response>")