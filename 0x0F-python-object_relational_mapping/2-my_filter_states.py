#!/usr/bin/python3
"""print states where name matches the argument"""
import MySQLdb
import sys


def search_states(username, password, database, state_name):
    """
    print state that matches the name searched
    """
    db = MySQLdb.connect(host='localhost', port=3306,
                         user=username, passwd=password, db=database)

    cursor = db.cursor()
    query = f"SELECT * FROM states WHERE name = '{state_name}' ORDER BY id ASC"
    cursor.execute(query)
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
        state_name = sys.argv[4]
        search_states(user, passwd, db, state_name)
    else:
        print("Usage: enter email password db use")
