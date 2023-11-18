#!/usr/bin/python3
""" script that display all values in the
'states' table of hbtn_0e_0_usa where 'name'
matches the argument """

import MySQLdb
from sys import argv


if __name__ == '__main__':
    """ list values that match the argument """

    db = MySQLdb.connect(
            host="localhost", user=argv[1],
            passwd=argv[2], db=argv[3], port=3306)

    cur = db.cursor()
    cur.execute("""SELECT * FROM states WHERE name LIKE BINARY %(name)s\
            ORDER BY states.id ASC""", {'name': argv[4]})
    rows = cur.fetchall()
    for row in rows:
        print(row)
