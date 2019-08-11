#!/usr/bin/python3
"""
module 8
"""
import sys
from model_state import Base, State

from sqlalchemy import (create_engine)

if __name__ == "__main__":
    cont = 0
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)
    q = engine.execute("SELECT * FROM states ORDER BY states.id ASC LIMIT 1")
    tmp_list = list(q)
    if tmp_list is not None or len(tmp_list) == 0:
        for iter in tmp_list:
            for iter2 in iter:
                if cont > 0:
                    print(": ", end='')
                print(iter2, end='')
                cont = cont + 1
            cont = 0
            print()
    else:
        print("Nothing")
