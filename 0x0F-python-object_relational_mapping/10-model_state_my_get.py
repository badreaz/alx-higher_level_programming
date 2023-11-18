#!/usr/bin/python3
""" script that prints th 'State' object with
the 'name' passed as argument from the databasee """

from sys import argv
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == '__main__':
    """ print the state """

    engine = create_engine(
            'mysql+mysqldb://{}:{}@localhost/{}'.format(
                argv[1], argv[2], argv[3]))
    Session = sessionmaker(bind=engine)
    session = Session()
    ins = session.query(State).filter(State.name == argv[4]).first()
    if ins is None:
        print('Not found')
    else:
        print("{}".format(ins.id))
