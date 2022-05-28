create database if not exists res;
use res;

create table if not exists korisnik(
    id integer primary key,
    name varchar(50) not null,
    lastname varchar(50) not null,
    username varchar(50) not null unique,
    email varchar(50) not null unique check (email like '%@%.%')
);

create table if not exists student(
    id varchar(10) primary key,
    name varchar(50) not null,
    lastname varchar(50) not null,
    username varchar(50) not null unique,
    email varchar(50)  not null unique check (email like '%@%.%'),
    year_of_study integer not null
);

create table if not exists profesor(
    id integer primary key,
    name varchar(50) not null,
    lastname varchar(50) not null,
    username varchar(50) not null unique,
    email varchar(50)  not null unique check (email like '%@%.%'),
    department varchar(50) not null
);

