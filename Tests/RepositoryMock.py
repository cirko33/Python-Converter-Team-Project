from unittest import TestCase
from mysql.connector import Error
from mock import patch
import mysql.connector, sys
sys.path.insert(0,"..")
from Repository import RepositoryCommands

mysql_host = "localhost"
mysql_user, mysql_password = "res_projekat", "restim20"
mysql_database = "res_test"
mysql_port = "3306"

class database_mock(TestCase):
    @classmethod
    def setUpClass(cls):
        connection = mysql.connector.connect(host=mysql_host, user=str(mysql_user), password=str(mysql_password), port=mysql_port)
        cursor = connection.cursor()

        try:
            cursor.execute("create database if not exists res_test;")
            connection.commit()
            cursor.close()
        except Error as err:
            print(err)

        create_query = """use res_test;
                    create table if not exists korisnik_test(
                        id integer primary key,
                        name varchar(50) not null,
                        lastname varchar(50) not null,
                        username varchar(50) not null unique,
                        email varchar(50) not null unique check (email like '%@%.%')
                    );
                    create table if not exists student_test(
                        id varchar(10) primary key,
                        name varchar(50) not null,
                        lastname varchar(50) not null,
                        username varchar(50) not null unique,
                        email varchar(50)  not null unique check (email like '%@%.%'),
                        year_of_study integer not null
                    );
                    create table if not exists profesor_test(
                        id integer primary key,
                        name varchar(50) not null,
                        lastname varchar(50) not null,
                        username varchar(50) not null unique,
                        email varchar(50)  not null unique check (email like '%@%.%'),
                        department varchar(50) not null
                        );"""

        create_queries = create_query.split(";")

        for cquery in create_queries:
            cursor = connection.cursor()
            try:
                cursor.execute(cquery)
                connection.commit()
                cursor.close()

            except Error as err:
                print(err)
        
        
        insert_query = """insert into korisnik_test values(1, 'Luka', 'Ciric', 'lukaciric', 'luka.ciric@yahoo.com'),
                        (2, 'Milorad', 'Markovic', 'mikipaok', 'mikipaok@yahoo.com'),
                        (3, 'Dejan', 'Kurdulija', 'dekikuki', 'kurdulijad@yahoo.com'),
                        (4, 'Zdravko', 'Milinkovic', 'kozdrav', 'milinkovicz@yahoo.com');
                        insert into student_test values('PR108/2019', 'Nemanja', 'Malinovic', 'malina', 'nemanjamalinovic@yahoo.com', 3),
                        ('PR12/2019', 'Jelena', 'Ilic', 'ilicka', 'ilicka00@gmail.com', 3),
                        ('PR30/2019', 'Vladimir', 'Stanojevic', 'vlox', 'stanojeviccc@yahoo.com', 3),
                        ('PR43/2019', 'Nikola', 'Bajagic', 'bajaga', 'bajagicnikola10@gmail.com', 3),
                        ('PR62/2019', 'Aleksandar', 'Zaric', 'zare00', 'zaric00@yahoo.com', 3),
                        ('PR15/2020', 'Katarina', 'Marinkovic', 'katarina', 'marinkovickaca@gmail.com', 2),
                        ('PR22/2018', 'Milan', 'Mastilovic', 'mastamozesvasta', 'mastilovicmilan@yahoo.com', 4),
                        ('PR12/2018', 'Nebojsa', 'Gordic', 'gorda', 'gordicn@yahoo.com', 4);
                        insert into profesor_test values(1, 'Petar', 'Maric', 'zlipera', 'petar.maric@uns.ac.rs', 'ACS'),
                        (2, 'Branislav', 'Atlagic', 'branislav', 'atlagic@uns.ac.rs', 'ESI'),
                        (3, 'Marina', 'Stanojevic', 'marinas', 'marinas@uns.ac.rs', 'EEPSI'),
                        (4, 'Bojana', 'Despotovic', 'despotovic', 'bojanadespotovic@uns.ac.rs', 'DEPT'),
                        (5, 'Aleksandar', 'Erdeljan', 'erdeljan', 'aleksandar.erdeljan@uns.ac.rs', 'ESI'),
                        (6, 'Luka', 'Strezovski', 'lukaaa', 'lukastrezovski@uns.ac.rs', 'EEPSI'),
                        (7, 'Srdjan', 'Popov', 'jelovopopov', 'popovsrdjan@uns.ac.rs', 'ACS'),
                        (8, 'Imre', 'Lendak', 'imre', 'lendak.imre@uns.ac.rs', 'ESI');"""

        insert_queries = insert_query.split(";")

        for iquery in insert_queries:
            cursor = connection.cursor()
            try:
                cursor.execute(iquery)
                connection.commit()
                cursor.close()
            except Error as err:
                print(err)

        testconfig = {
            'host' : mysql_host,
            'database' : mysql_database,
            'user' : mysql_user,
            'password' : mysql_password
        }
        cls.mock_db_config = patch.dict(RepositoryCommands.config, testconfig)

    @classmethod
    def tearDownClass(cls):
        connection = mysql.connector.connect(host=mysql_host, user=mysql_user, password=mysql_password)
        cursor = connection.cursor()
        query = "drop database res_test;"
        try:
            cursor.execute(query)
            connection.commit()
        except Error as err:
            print(err)
        
        cursor.close()
        connection.close()
