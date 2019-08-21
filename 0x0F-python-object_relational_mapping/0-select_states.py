#!/usr/bin/python3
"""
module task 0
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
    numrows = cur.execute(
        "SELECT * FROM states ORDER BY id ASC")
    for row in cur.fetchall():
        print(row)
    db.close()
