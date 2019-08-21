#!/usr/bin/python3
"""
module 8
"""
import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_city import City
from sqlalchemy import (create_engine)

if __name__ == "__main__":
    cont = 0
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    states = session.query(City, State).order_by(City.id.asc())\
                                       .filter(City.state_id == State.id).all()
    if states is not None:
        for iter1, iter2 in states:
            print("{}: ({}) {}".format(iter2.name, iter1.id, iter1.name))
    else:
        print("Nothing")
