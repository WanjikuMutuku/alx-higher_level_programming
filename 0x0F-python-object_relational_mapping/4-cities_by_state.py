#!/usr/bin/python3
"""
script that lists all cities from the database hbtn_0e_4_usa
"""
import MySQLdb
import sys

if __name__ == "__main__":
    # Get the command-line arguments
    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]

    # Connect to the MySQL server
    db = MySQLdb.connect(host="localhost", port=3306, user=mysql_username,
                         passwd=mysql_password, db=database_name)

    # Create a cursor object to execute SQL queries
    cursor = db.cursor()

    # Execute the SQL query to retrieve the states
    cursor.execute("SELECT cities.id, cities.name, states.name FROM cities\
            INNER JOIN states ON cities.state_id = states.id\
            ORDER BY cities.id ASC")

    # Fetch all the rows returned by the query
    rows = cursor.fetchall()

    # Print the states
    for row in rows:
        print(row)

    # Close the cursor and database connection
    cursor.close()
    db.close()
