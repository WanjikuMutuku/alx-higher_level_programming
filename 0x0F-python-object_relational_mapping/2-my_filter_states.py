#!/usr/bin/python3
"""
script that takes in an argument and displays all values in the states table of hbtn_0e_0_usa where name matches the argument.
"""
import MySQLdb
import sys

# Get the command-line arguments
mysql_username = sys.argv[1]
mysql_password = sys.argv[2]
database_name = sys.argv[3]
state_name = sys.argv[4]

# Connect to the MySQL server
db = MySQLdb.connect(host="localhost", port=3306, user=mysql_username,
                     passwd=mysql_password, db=database_name)

# Create a cursor object to execute SQL queries
cursor = db.cursor()

# Execute the SQL query to retrieve states matching the argument
query = "SELECT * FROM states WHERE name = %s ORDER BY id ASC"
cursor.execute(query, (state_name,))

# Fetch all the rows returned by the query
rows = cursor.fetchall()

# Print the states
for row in rows:
    print(row)

# Close the cursor and database connection
cursor.close()
db.close()
