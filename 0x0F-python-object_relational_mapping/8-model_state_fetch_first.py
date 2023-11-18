#!/usr/bin/python3
""" script that prints the first State object from
the database hbtn_0e_6_usa """

from sys import argv
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == '__main__':
    """ print the first object """

    engine = create_engine(
            'mysql+mysqldb://{}:{}@localhost/{}'.format(
                argv[1], argv[2], argv[3]))
    Session = sessionmaker(bind=engine)
    session = Session()
    ins = session.query(State).order_by(State.id).first()
    if (ins == NULL):
        print('Nothing')
    else:
        print("{}: {}".format(ins.id, ins.name))
