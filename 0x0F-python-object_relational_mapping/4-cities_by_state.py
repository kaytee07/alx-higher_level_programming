#!/usr/bin/python3
"""script should list all state in database"""
import MySQLdb
import sys


if __name__ == '__main__':
    db = MySQLdb.connect(host='localhost', port=3306,
                         user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])

    cursor = db.cursor()
    cursor.execute("""SELECT c.id, c.name, s.name FROM
                cities AS c INNER JOIN states AS s ON s.id=c.state_id""")
    rows = cursor.fetchall()

    for row in rows:
        print(row)

    cursor.close()
    db.close()
