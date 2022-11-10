#!/usr/bin/python3
"""
Script that list all states with name starting with N
"""
from sys import argv
import MySQLdb

if __name__ == "__main__":

    db = MySQLdb.connect(user=argv[1], passwd=argv[2], db=argv[3])
    cur = db.cursor()
    check = (argv[4],)
    cur.execute("SELECT * FROM states WHERE name = '{}' ORDER BY id ASC".format(check))
    query_rows = cur.fetchall()
    for row in query_rows:
        print(row)
    cur.close()
    db.close()
