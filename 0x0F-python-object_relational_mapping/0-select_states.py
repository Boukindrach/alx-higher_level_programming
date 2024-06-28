#!/usr/bin/python3

import MySQLdb
from sys import argv

# Connect to the database
db = MySQLdb.connect(host='localhost', port=3306, user=argv[1], passwd=argv[2], db=argv[3])

cur = db.cursor()

# Execute the query
cur.execute("SELECT id, name FROM states")

# Fetch all the rows from the query
rows = cur.fetchall()

# Print the results
for row in rows:
    print(row)

# Close the cursor and the connection
cur.close()
db.close()

