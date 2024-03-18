#!/usr/bin/python3
"""
script that lists all states with a name starting with N (upper N) from the database hbtn_0e_0_usa
"""
import MySQLdb
import sys

if __name__ == "__main__":
    # command line arguments
    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]

    # connect to MYSQL server
    db = MySQLdb.connect(host="localhost", port=3306, user=mysql_username,
                         passwd=mysql_password, db=database_name)

    # create cursor object to execute SQL queries
    cursor = db.cursor()

    # executing MYSQL tables
    cursor.execute("SELECT DISTINCT * FROM states WHERE name LIKE BINARY 'N%'")

    # fetch all rows returned by the query
    rows = cursor.fetchall()

    # print the states
    for row in rows:
        print(row)

    # Close the cursor
    cursor.close()
    db.close()
