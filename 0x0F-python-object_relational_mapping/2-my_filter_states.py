#!/usr/bin/python3
"""
module 2 fixed
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
    consulta = (("SELECT * FROM states WHERE BINARY name = '{}'") +
                (" ORDER BY id ASC"))
    numrows = cur.execute(consulta.format(sys.argv[4]))

    for row in cur.fetchall():
        print(row)
    db.close()
