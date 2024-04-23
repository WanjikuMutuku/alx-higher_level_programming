#!/usr/bin/python3
"""Prints the State object with the given name from the database hbtn_0e_6_usa
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    # Check if all arguments are provided
    if len(sys.argv) != 5:
        print("Usage: ./10-model_state_my_get.py\
                <mysql username> <mysql password>\
                <database name> <state name>")
        sys.exit(1)

    # Get the arguments
    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]
    state_name = sys.argv[4]

    # Create the engine
    engine = create_engine(
        f'mysql+mysqldb://{mysql_username}:\
                {mysql_password}@localhost:3306/{database_name}',
        pool_pre_ping=True
    )

    # Create a session factory
    Session = sessionmaker(bind=engine)

    # Create a session
    session = Session()

    # Query the State object with the given name
    state = session.query(State).filter(State.name == state_name).first()

    # Print the result
    if state is not None:
        print(state.id)
    else:
        print("Not found")

    # Close the session
    session.close()
