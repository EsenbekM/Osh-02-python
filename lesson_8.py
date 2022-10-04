#  SQL - Structured Query Language
#  СУБД - Система Управления Базой Данных
#  NoSQL - No Relation

#  SQLite

#  CRUD - Create Reed Update Delete

import sqlite3
from sqlite3 import Error


def create_connection(db_name):
    conn = None
    try:
        conn = sqlite3.connect(db_name)
    except Error:
        print(Error)

    return conn


def create_table(conn, sql):
    try:
        cursor = conn.cursor()
        cursor.execute(sql)
    except Error:
        print(Error)


def create_student(conn, student):
    try:
        sql = '''INSERT INTO students 
        (fullname, mark, hobby, birth_date, is_married)
        VALUES (?, ?, ?, ?, ?)'''
        cursor = conn.cursor()
        cursor.execute(sql, student)
        conn.commit()
    except Error:
        print(Error)


def delete_student(conn, id):
    try:
        sql = '''DELETE FROM students WHERE id = ?'''
        cursor = conn.cursor()
        cursor.execute(sql, (id,))
        conn.commit()
    except Error:
        print(Error)


def update_student_mark_and_martial_status(conn, student):
    try:
        sql = '''UPDATE students SET mark = ?, is_married = ? WHERE id = ?'''
        cursor = conn.cursor()
        cursor.execute(sql, student)
        conn.commit()
    except Error:
        print(Error)


def select_all_students(conn):
    try:
        sql = '''SELECT * FROM students'''
        cursor = conn.cursor()
        cursor.execute(sql)

        rows = cursor.fetchall()
        for row in rows:
            print(row)

    except Error:
        print(Error)


def select_students_by_mark(conn, mark):
    try:
        sql = '''SELECT * FROM students WHERE mark > ?'''
        cursor = conn.cursor()
        cursor.execute(sql, (mark,))

        rows = cursor.fetchall()
        for row in rows:
            print(row)

    except Error:
        print(Error)


connection = create_connection("my_db.db")

create_students_table = '''
CREATE TABLE students (
id INTEGER PRIMARY KEY AUTOINCREMENT,
fullname VARCHAR (200) NOT NULL,
mark DOUBLE (5, 2) NOT NULL DEFAULT 0.0,
hobby TEXT DEFAULT NULL,
birth_date DATE NOT NULL,
is_married BOOLEAN DEFAULT FALSE
)
'''

if connection is not None:
    print("Connected!")
    select_students_by_mark(connection, 50)
    # select_all_students(connection)
    # update_student_mark_and_martial_status(connection, (12.01, False, 6))

    # delete_student(connection, 1)

    # create_table(connection, create_students_table)

    # create_student(connection, ("Ivanov SerGey", 30.34, "Dance GO-GO", "2000-05-23", True))
    #
    # create_student(connection, ("Reina Arstanbekova", 98.23, "Tennis", "2004-10-19", False))
    # create_student(connection, ("Mark Daniels", 77.12, "Football", "1999-01-02", False))
    # create_student(connection, ("Alex Brilliant", 77.12, None, "1989-12-31", True))
    # create_student(connection, ("Diana Julls", 99.3, "Tennis", "2005-01-22", True))
    # create_student(connection, ("Michael Corse", 100.0, "Diving", "2001-09-17", True))
    # create_student(connection, ("Jack Moris", 50.2, "Fishing and cooking", "2001-07-12", True))
    # create_student(connection, ("Viola Manilson", 41.82, None, "1991-03-01", False))
    # create_student(connection, ("Joanna Moris", 100.0, "Painting and arts", "2004-04-13", False))
    # create_student(connection, ("Peter Parker", 32.0, "Travelling and bloging", "2002-11-28", False))
    # create_student(connection, ("Paula Parkerson", 77.09, None, "2001-11-28", True))
    # create_student(connection, ("George Newel", 93.0, "Photography", "1981-01-24", True))
    # create_student(connection, ("Miranda Alistoun", 87.55, "Playing computer games", "1997-12-22", False))
    # create_student(connection, ("Fiona Giordano", 66.12, "Driving fast", "1977-01-15", True))

    print("Done")
