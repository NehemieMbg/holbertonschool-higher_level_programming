#!/usr/bin/python3
"""
Script that list all states with name starting with N
"""
from sys import argv
import MySQLdb

if __name__ == "__main__":

    db = MySQLdb.connect(user=argv[1], passwd=argv[2], db=argv[3])
    cur = db.cursor()
    cur.execute("SELECT * FROM states WHERE name LIKE "N%" ORDER BY state.id ASC;")
    query_rows = cur.fetchall()
    for row in query_rows:
        if row[1][0] == 'N':
            print(row)
    cur.close()
    db.close()
