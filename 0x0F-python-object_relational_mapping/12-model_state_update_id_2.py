#!/usr/bin/python3
""" script that changes the name of a 'State'
object from the databasse """

from sys import argv
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == '__main__':
    """ update object """

    engine = create_engine(
            'mysql+mysqldb://{}:{}@localhost/{}'.format(
                argv[1], argv[2], argv[3]))
    Session = sessionmaker(bind=engine)
    session = Session()
    ins = session.query(State).filter(State.id == 2).first()
    ins.name = "New Mexico"
    session.commit()
