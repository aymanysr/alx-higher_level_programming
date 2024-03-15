#!/usr/bin/python3

"""
Lists all states with a name starting with N (upper N)
from the database hbtn_0e_0_usa
"""

import sys
import MySQLdb

if __name__ == "__main__":
    # Check if the correct number of arguments were passed
    if len(sys.argv) != 4:
        print(f"Usage: {sys.argv[0]} username password database_name")
        sys.exit(1)

    try:
        # Connect to MySQL server
        db = MySQLdb.connect(host="localhost", user=sys.argv[1],
                             passwd=sys.argv[2], db=sys.argv[3], port=3306)

        # Create a cursor object
        cur = db.cursor()

        # Execute SQL query to retrieve states starting with 'N'
        cur.execute("SELECT * FROM states WHERE name LIKE BINARY 'N%' "
                    "ORDER BY id ASC")

        # Fetch all the rows in a list of tuples
        rows = cur.fetchall()

        # Display results
        for row in rows:
            print(row)

    except MySQLdb.Error as e:
        print(f"MySQL Error {e.args[0]}: {e.args[1]}")
        sys.exit(1)

    finally:
        # Close cursor and database connection
        if 'cur' in locals() or 'cur' in globals():
            cur.close()
        if 'db' in locals() or 'db' in globals():
            db.close()
