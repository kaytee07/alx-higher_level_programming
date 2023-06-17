#!/usr/bin/python3
"""list all state with a name starting with N from the db"""
import MySQLdb
import sys


if __name__ == '__main__':
    db = MySQLdb.connect(host="localhost", user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3], port=3306)
    query = "SELECT * FROM states WHERE name LIKE BINARY 'N%' ORDER BY id"
    cursor = db.cursor()
    cursor.execute(query)
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    cursor.close()
    db.close()
