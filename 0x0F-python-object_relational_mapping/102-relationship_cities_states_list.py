#!/usr/bin/python3
""" script that lists all 'City' objects """

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
    rows = session.query(State).join(City).order_by(City.id).all()
    for row in rows:
        for cities in row.cities:
            print("{}: {} -> {}".format(cities.id, cities.name, row.name))
    session.close()
