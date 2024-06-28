#!/usr/bin/python3
"""
Script takes in the name of a state as
an argument and lists all cities of that state
"""
import MySQLdb
import sys

if __name__ == '__main__':

    db = MySQLdb.connect(
        user=sys.argv[1],
        password=sys.argv[2],
        database=sys.argv[3],
        host="localhost",
        port=3306)

    cursor = db.cursor()
    cursor.execute("SELECT cities.id, cities.name, states.name \
                FROM cities INNER JOIN states \
                ON cities.state_id=states.id")
    for row in cursor.fetchall():
        print(row)
    cursor.close()
    db.close()
