#!/usr/bin/python3
"""
contains the class definition of a State and an instance
Base = declarative_base()
"""
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    """ State class """
    __tablename__ == 'states'
    id = Column(Integer, primary_key=True, nullable=False,
            autoincrement=True)
    name = Column(String(128), nullable=False)

if __name__ == "__main__":
    import sys
    from sqlalchemy import create_engine

    #create the engine
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
            .format(sys.argv[1], sys.argv[2], sys.argv[3])
            pool_pre_ping=True)
    
    #create the tables
    Base.metadata.create_all(engine)
