#!/usr/bin/python3
"""  lists all states with a name starting with N (upper N)
 from the database hbtn_0e_0_usa

 Attributes:
    username (string): variable username
    password (string): variable password
 """

import MySQLdb as mysql
import sys

username = sys.argv[1]
password = sys.argv[2]
database = sys.argv[3]
'''string: string type variable'''


if __name__ == '__main__':
    db = mysql.connect(host='localhost',
                       user=username,
                       passwd=password,
                       db=database)
    cursor = db.cursor()
    cursor.execute("SELECT * FROM states WHERE name LIKE BINARY 'N%'")
    data = cursor.fetchall()
    for elem in data:
        print(elem)
    cursor.close()
    db.close()