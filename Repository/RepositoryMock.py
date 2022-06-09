
from unittest import TestCase
import mysql.connector
from mysql.connector import Error
from mock import patch
from Repository import RepositoryCommands

# def load():
#     file = open("RepositoryAuthentication.txt")
#     username = file.readline()
#     password = file.readline()
#     file.close()
#     return username, password

mysql_host = "localhost"
mysql_user, mysql_password = "res_projekat", "restim20"
mysql_database = "res"

class database_mock(TestCase):
    @classmethod
    def setUp(cls):
        connection = mysql.connector.connect(host=mysql_host, database=mysql_database, user=str(mysql_user), password=str(mysql_password))
        cursor = connection.cursor()
        query = """create database if not exists res;
                    use res;
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

        try:
            cursor.execute(query)
            connection.commit()

        except Error as err:
            print(err)
        
        query = """insert into korisnik_test values(1, 'Luka', 'Ciric', 'lukaciric', 'luka.ciric@yahoo.com');
                    insert into korisnik_test values(2, 'Milorad', 'Markovic', 'mikipaok', 'mikipaok@yahoo.com');
                    insert into korisnik_test values(3, 'Dejan', 'Kurdulija', 'dekikuki', 'kurdulijad@yahoo.com');
                    insert into korisnik_test values(4, 'Zdravko', 'Milinkovic', 'kozdrav', 'milinkovicz@yahoo.com');


                    insert into student_test values('PR108/2019', 'Nemanja', 'Malinovic', 'malina', 'nemanjamalinovic@yahoo.com', 3);
                    insert into student_test values('PR12/2019', 'Jelena', 'Ilic', 'ilicka', 'ilicka00@gmail.com', 3);
                    insert into student_test values('PR30/2019', 'Vladimir', 'Stanojevic', 'vlox', 'stanojeviccc@yahoo.com', 3);
                    insert into student_test values('PR43/2019', 'Nikola', 'Bajagic', 'bajaga', 'bajagicnikola10@gmail.com', 3);
                    insert into student_test values('PR62/2019', 'Aleksandar', 'Zaric', 'zare00', 'zaric00@yahoo.com', 3);
                    insert into student_test values('PR15/2020', 'Katarina', 'Marinkovic', 'katarina', 'marinkovickaca@gmail.com', 2);
                    insert into student_test values('PR22/2018', 'Milan', 'Mastilovic', 'mastamozesvasta', 'mastilovicmilan@yahoo.com', 4);
                    insert into student_test values('PR12/2018', 'Nebojsa', 'Gordic', 'gorda', 'gordicn@yahoo.com', 4);

                    insert into profesor_test values(1, 'Petar', 'Maric', 'zlipera', 'petar.maric@uns.ac.rs', 'ACS');
                    insert into profesor_test values(2, 'Branislav', 'Atlagic', 'branislav', 'atlagic@uns.ac.rs', 'ESI');
                    insert into profesor_test values(3, 'Marina', 'Stanojevic', 'marinas', 'marinas@uns.ac.rs', 'EEPSI');
                    insert into profesor_test values(4, 'Bojana', 'Despotovic', 'despotovic', 'bojanadespotovic@uns.ac.rs', 'DEPT');
                    insert into profesor_test values(5, 'Aleksandar', 'Erdeljan', 'erdeljan', 'aleksandar.erdeljan@uns.ac.rs', 'ESI');
                    insert into profesor_test values(6, 'Luka', 'Strezovski', 'lukaaa', 'lukastrezovski@uns.ac.rs', 'EEPSI');
                    insert into profesor_test values(7, 'Srdjan', 'Popov', 'jelovopopov', 'popovsrdjan@uns.ac.rs', 'ACS');
                    insert into profesor_test values(8, 'Imre', 'Lendak', 'imre', 'lendak.imre@uns.ac.rs', 'ESI');"""
        
        try:
            cursor.execute(query)
            connection.commit()
        except Error as err:
            print(err)

        cursor.close()
        connection.close()

        testconfig = {
            'host' : mysql_host,
            'database' : mysql_database,
            'user' : mysql_user,
            'password' : mysql_password
        }
        cls.mock_db_config = patch.dict(RepositoryCommands.config, testconfig)

    @classmethod
    def tearDownClass(cls):
        connection = mysql.connector.connect(host=mysql_host, database=mysql_database, user=mysql_user, password=mysql_password)
        cursor = connection.cursor()
        query = """drop table korisnik_test;
                    drop table student_test;
                    drop table profesor_test;"""
        try:
            cursor.execute(query)
            connection.commit()
        except Error as err:
            print(err)
        
        cursor.close()
        connection.close()
