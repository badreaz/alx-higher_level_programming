#!/usr/bin/python3
""" script that lists all State objects that contain
the letter 'a' from the database hbtn_0e_6_usa """

from sys import argv
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == '__main__':
    """ list objects that start with 'a' """

    engine = create_engine(
            'mysql+mysqldb://{}:{}@localhost/{}'.format(
                argv[1], argv[2], argv[3]))
    Session = sessionmaker(bind=engine)
    session = Session()
    for ins in session.query(State).filter(State.name.contains('a')):
        print("{}: {}".format(ins.id, ins.name))
