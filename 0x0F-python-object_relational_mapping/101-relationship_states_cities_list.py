#!/usr/bin/python3
""" script that lists all 'State' objects, and
corresponding 'City' objects """

from sys import argv
from relationship_state import Base, State
from relationship_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == '__main__':
    """ list objects """

    engine = create_engine(
            'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
                argv[1], argv[2], argv[3]))
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    rows = session.query(State).outerjoin(City)
    .order_by(State.id, City.id).all()
    for row in rows:
        print("{}: {}".format(row.id, row.name))
        for cities in row.cities:
            print("\t{}: {}".format(cities.id, cities.name))
    session.close()
