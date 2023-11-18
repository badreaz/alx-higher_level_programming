#!/usr/bin/python3
""" script that takes in the name of a state as
an argument and lists all 'cities' of that state """

import MySQLdb
from sys import argv


if __name__ == '__main__':
    """ list the cities in the state """

    db = MySQLdb.connect(
            host="localhost", user=argv[1],
            passwd=argv[2], db=argv[3], port=3306)

    cur = db.cursor()
    cur.execute("""SELECT cities.name, cities.id FROM cities JOIN states\
            ON cities.state_id = states.id\
            WHERE states.name LIKE BINARY %(state)s\
            ORDER BY cities.id ASC""", {'state': argv[4]})
    cities = cur.fetchall()
    print(", ".join([city[0] for city in cities]))
