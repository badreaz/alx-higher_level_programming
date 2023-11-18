#!/usr/bin/python3
""" script that prints all 'City' objects
from the databse """

from sys import argv
from model_state import Base, State
from model_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == '__main__':
    """ print all object """

    engine = create_engine(
            'mysql+mysqldb://{}:{}@localhost/{}'.format(
                argv[1], argv[2], argv[3]))
    Session = sessionmaker(bind=engine)
    session = Session()
    ins = session.query(City, State).join(State)
    for city, state in ins.all():
        print("{}: ({}) {}".format(state.name, city.id, city.name))
    session.close()
