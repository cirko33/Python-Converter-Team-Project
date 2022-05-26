drop table korisnik;
drop table student;
drop table profesor;

create table korisnik(
    id integer not null,
    name varchar2(50) not null,
    lastname varchar2(50) not null,
    username varchar2(50) not null unique,
    email varchar2(50) not null check (email like '%@%.%') unique,
    constraint id_pk primary key (id)
);

create table student(
    ind varchar2(10) not null,
    name varchar2(50) not null,
    lastname varchar2(50) not null,
    username varchar2(50) not null unique,
    email varchar2(50) check (email like '%@%.%') not null unique,
    year_of_study integer not null,
    constraint ind_pk primary key (ind)
);

create table profesor(
    id integer not null,
    name varchar2(50) not null,
    lastname varchar2(50) not null,
    username varchar2(50) not null unique,
    email varchar2(50) check (email like '%@%.%') not null unique,
    department varchar2(50) not null,
    constraint idp_pk primary key (id)
);

