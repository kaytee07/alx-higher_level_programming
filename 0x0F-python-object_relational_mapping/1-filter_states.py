#!/usr/bin/python3
"""list all state with a name starting with N from the db"""
import MySQLdb
import sys


def list_all_state_N(username, password, database):
    """
    list all state that start with capital N from hbtn_0e_0_usa db
    """
    db = MySQLdb.connect(host='localhost', port=3306,
                         user=username, passwd=password, db=database)
    cursor = db.cursor()
    cursor.execute('SELECT * FROM states WHERE name LIKE "N%" ORDER BY id ASC')
    rows = cursor.fetchall()
    for row in rows:
        print(row)

    cursor.close()
    db.close()


if __name__ == '__main__':
    if len(sys.argv) == 4:
        username = sys.argv[1]
        password = sys.argv[2]
        database = sys.argv[3]
        list_all_state_N(username, password, database)
