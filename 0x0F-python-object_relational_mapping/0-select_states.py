#!/usr/bin/python3
"""  lists all states from the database hbtn_0e_0_usa """

import MySQLdb as mysql
import sys

username = sys.argv[1]
password = sys.argv[2]
database = sys.argv[3]


def read_db(uname, pwd, db_name):
    """ READS DATA FROM A DATABASE:
    - Returns a tuple containing the data
    """
    db = mysql.connect(host='localhost',
                       port=3306,
                       user=uname,
                       passwd=pwd,
                       db=db_name)
    cursor = db.cursor()
    cursor.execute('SELECT * FROM states')
    reader = cursor.fetchall()
    return reader


def print_db(data):
    """ PRINT CONTENTS OF A DATABASE:
    - Print format: (##, ##, ...)
    """
    for row in data:
        print('(', end='')
        for index in range(0, len(row)):
            if type(row[index]) == 'string':
                print('\'' + row[index] + '\'', end='')
            else:
                print(row[index], end='')
            if index < len(row) - 1:
                print(', ', end='')
            else:
                print(')')


if __name__ == "__main__":
    reader = read_db(username, password, database)
    print_db(reader)
    print(print_db.__doc__)
