#!/usr/bin/python3
"""
module 3
"""
import MySQLdb
import sys

if __name__ == "__main__":
    db = MySQLdb.connect(
        host="localhost",
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3],
        port=3306)
    cur = db.cursor()
    numrows = cur.execute("SELECT cities.name FROM cities, states \
    WHERE states.name = %s AND states.id = cities.state_id", (sys.argv[4],))
    cont = 0
    for row in cur.fetchall():
        for iter2 in row:
            if cont > 0:
                print(", ", end='')
            print("{}".format(iter2), end='')
            cont = cont + 1
    print()
    db.close()
