#!/usr/bin/python3
""" Lists all states from the database hbtn_0e_0_usa"""

import MySQLdb
import sys

if __name__ == "__main__":
    try:
        # Connect to MySQL server
        db = MySQLdb.connect(host="localhost", user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3], port=3306)

        # Create a cursor object
        cur = db.cursor()

        # Execute SQL query to retrieve states
        cur.execute("SELECT * FROM states ORDER BY id ASC")

        # Fetch all the rows in a list of tuples
        rows = cur.fetchall()

        # Display results
        for row in rows:
            print(row)

    except MySQLdb.Error as e:
        print("MySQL Error {}: {}".format(e.args[0], e.args[1]))
        sys.exit(1)

    finally:
        # Close cursor and database connection
        if 'cur' in locals() or 'cur' in globals():
            cur.close()
        if 'db' in locals() or 'db' in globals():
            db.close()
