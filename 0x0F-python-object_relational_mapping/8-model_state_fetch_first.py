#!/usr/bin/python3
"""
prints the first State object from the database hbtn_0e_6_usa
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    # create engine
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)

    # create session factory
    Session = sessionmaker()
    session = sessionmaker(bind=engine)

    # create session
    session = Session()

    # query to print the firs state
    state = session.query(State).order_by(State.id).first()

    # Print the result
    if state is not None:
        print("{}: {}".format(state.id, state.name))

    # Close the session
    session.close()
