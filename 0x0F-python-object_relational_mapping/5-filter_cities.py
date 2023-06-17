#!/usr/bin/python3
"""print states where name matches the argument"""
import MySQLdb
import sys


if __name__ == '__main__':
    db = MySQLdb.connect(host="localhost", user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3], port=3306)
    cursor = db.cursor()
    cursor.execute("""SELECT c.name FROM
                cities AS c INNER JOIN states AS s ON s.id=c.state_id
                WHERE s.name=%s""", (sys.argv[4],))
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    cursor.close()
    db.close()
