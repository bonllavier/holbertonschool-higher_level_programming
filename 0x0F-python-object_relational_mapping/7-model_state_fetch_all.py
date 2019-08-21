#!/usr/bin/python3
"""
module 7
"""
import sys
from model_state import Base, State

from sqlalchemy import (create_engine)

if __name__ == "__main__":
    cont = 0
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)
    q = engine.execute("SELECT * FROM states ORDER BY states.id ASC")
    content = q.fetchall()
    for iter in content:
        for iter2 in iter:
            if cont > 0:
                print(": ", end='')
            print(iter2, end='')
            cont = cont + 1
        cont = 0
        print()
