#!/usr/bin/python3
'''  Prints only states contaning a search string'''

import MySQLdb as mysql
import sys


if __name__ == '__main__':
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    tag = sys.argv[4]

    db = mysql.connect(host='localhost',
                       user=username,
                       passwd=password,
                       db=database)
    cursor = db.cursor()
    cursor.execute("SELECT * FROM states WHERE name='{}'".format(tag))
    data = cursor.fetchall()
    for elem in data:
        print(elem)
    cursor.close()
    db.close()
