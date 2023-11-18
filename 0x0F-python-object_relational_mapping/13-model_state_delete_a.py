#!/usr/bin/python3
""" script that deletes all 'State' objects
with a name containing the letter 'a' """

from sys import argv
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == '__main__':
    """ delete objects containig 'a' """

    engine = create_engine(
            'mysql+mysqldb://{}:{}@localhost/{}'.format(
                argv[1], argv[2], argv[3]))
    Session = sessionmaker(bind=engine)
    session = Session()
    for ins in session.query(State).filter(State.name.contains('a')):
        session.delete(ins)
    session.commit()
    session.close()
