#!/usr/bin/python3
"""print states where name matches the argument"""
import MySQLdb
import sys


def list_all_search(username, password, database, search):
    """
    print state that matches the name searched
    """
    db = MySQLdb.connect(host='localhost', port=3306,
                         user=username, passwd=password, db=database)

    cursor = db.cursor()
    query = "SELECT * FROM states WHERE name = %s ORDER BY id ASC"
    cursor.execute(query, (search,))
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    cursor.close()
    db.close()


if __name__ == '__main__':
    if len(sys.argv) == 5:
        user = sys.argv[1]
        passwd = sys.argv[2]
        db = sys.argv[3]
        search = sys.argv[4]
        list_all_search(user, passwd, db, search)
    else:
        print("Usage: enter email password db use")
