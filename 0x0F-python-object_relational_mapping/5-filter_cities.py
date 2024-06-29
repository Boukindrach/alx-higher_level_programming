#!/usr/bin/python3
"""
Takes the name of a state as an argument and lists all cities in that state.
"""
import MySQLdb
import sys

if __name__ == '__main__':

    db_user = sys.argv[1]
    db_password = sys.argv[2]
    db_name = sys.argv[3]
    state_name = sys.argv[4]

    db = MySQLdb.connect(
        user=db_user,
        password=db_password,
        database=db_name,
        host="localhost",
        port=3306
    )

    cursor = db.cursor()
    cursor.execute("SELECT cities.name FROM cities \
        INNER JOIN states ON cities.state_id = states.id \
        WHERE states.name = %s", (state_name,))
    rows = cursor.fetchall()
    city_names = ", ".join(row[0] for row in rows)
    print(city_names)
    cursor.close()
    db.close()
