#!/usr/bin/python3
"""
takes in an argument and displays all values
in the states table of hbtn_0e_0_usa where name matches the argument
"""


import MySQLdb
from sys import argv

if __name__ == "__main__":
    """SQL query using MySQLdb"""
    try:
        db = MySQLdb.connect(
            host="localhost", port=3306, user=argv[1], passwd=argv[2], db=argv[3])

        cur = db.cursor()

        query = "SELECT * FROM states WHERE name = '{}'\
                ORDER BY id".format(argv[4])
        cur.execute(query)

        rows = cur.fetchall()

        for row in rows:
            print(row)

    except MySQLdb.Error as e:
        print("Error: {}".format(e))

    finally:
        if cur:
            cur.close()
        if db:
            db.close()
