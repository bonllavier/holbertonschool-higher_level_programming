#!/usr/bin/python3
"""
module task 0
"""
import MySQLdb
import sys

db = MySQLdb.connect(host="localhost", user=sys.argv[1],
                     passwd=sys.argv[2], db=sys.argv[3])
cur = db.cursor()
numrows = cur.execute(
    "SELECT * FROM states GROUP BY states.name ORDER BY states.id")
for row in cur.fetchall():
    print(row)
db.close()
