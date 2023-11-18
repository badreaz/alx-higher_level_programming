#!/usr/bin/python3
""" script that list all 'states' with
a 'name' starting with 'N' from the database
hbtn_0e_0_usa """

import MySQLdb
from sys import argv


if __name__ == '__main__':
    """ list names that start with 'N' """

    db = MySQLdb.connect(
            host="localhost", user=argv[1],
            passwd=argv[2], db=argv[3], port=3306)

    cur = db.cursor()
    cur.execute("SELECT * FROM states WHILE name like 'N%' \
            ORDER BY states.id ACS")
    rows = cur.fetchall()
    for row in rows:
        print(row)