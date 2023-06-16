#!/usr/bin/python3
"""script should list all state in database"""
import MySQLdb
import sys


def list_all_states(username, password, database):
    """this function list all state from database hbtn_0e_0_usa"""
    db = MySQLdb.connect(host='localhost', port=3306,
                         user=username, passwd=password, db=database)

    cursor = db.cursor()
    cursor.execute('SELECT * FROM states ORDER BY id ASC')
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
        list_all_states(username, password, database)
    else:
        print("Usage: enter username, password and database")
