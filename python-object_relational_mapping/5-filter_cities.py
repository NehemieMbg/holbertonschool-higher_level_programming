#!/usr/bin/python3
"""
Script that list all states with name starting with N
"""
from sys import argv
import MySQLdb

if __name__ == "__main__":

    db = MySQLdb.connect(user=argv[1], passwd=argv[2], db=argv[3])
    cur = db.cursor()
    cur.execute(
        "SELECT cities.name FROM cities \
                INNER JOIN states WHERE states.id=cities.state_id \
                AND states.name= %s ORDER BY cities.id ASC", (argv[4], )
        )
    query_rows = cur.fetchall()
    display = (', '.join(row[0] for row in rows))
    for row in query_rows:
        print(row)
    cur.close()
    db.close()
