#!/usr/bin/python3
""" script that adds the 'State' object
'Louisiana' to the database """

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
    ins = State(name="Louisiana")
    session.add(ins)
    session.commit()
    print("{}".format(ins.id))
