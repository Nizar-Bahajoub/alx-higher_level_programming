#!/usr/bin/python3
"""
takes in the name of a state as an argument and
lists all cities of that state
"""


import MySQLdb
from sys import argv

if __name__ == "__main__":
    """SQL query using MySQLdb securng SQL injctions"""
    db = MySQLdb.connect(
            host="localhost", port=3306, user=argv[1],
            passwd=argv[2], db=argv[3])

    cur = db.cursor()

    query = "SELECT cities.name \
            FROM cities JOIN states ON cities.state_id = states.id \
            WHERE states.name LIKE %s \
            ORDER BY cities.id ASC"

    state = argv[4]
    cur.execute(query, (state,))

    rows = cur.fetchall()

    if rows is not None:
        print(", ".join([row[0] for row in rows]))
