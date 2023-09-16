#!/usr/bin/python3
"""
lists all cities from the database hbtn_0e_4_usa
"""


import MySQLdb
from sys import argv

if __name__ == "__main__":
    """SQL query using MySQLdb securng SQL injctions"""
    db = MySQLdb.connect(
            host="localhost", port=3306, user=argv[1],
            passwd=argv[2], db=argv[3])

    cur = db.cursor()

    query = "SELECT cities.id, cities.name AS city_name, \
            tates.name AS state_name \
            FROM cities JOIN states ON cities.state_id = states.id\
            ORDER BY cities.id ASC"
    cur.execute(query)

    rows = cur.fetchall()

    for row in rows:
        print(row)
