#!/usr/bin/python3
"""lists all cities from the database hbtn_0e_4_usa"""

import sys
import MySQLdb

if __name__ == "__main__":
    try:
        # Connect to MySQL server
        db = MySQLdb.connect(host="localhost", user=sys.argv[1],
                             passwd=sys.argv[2], db=sys.argv[3], port=3306)

        # Create a cursor object
        cur = db.cursor()

        # SQL query to retrieve states
        sql_query = "SELECT cities.id, cities.name, states.name FROM cities " \
                    "JOIN states ON cities.state_id = states.id " \
                    "ORDER BY cities.id ASC"

        # Execute SQL query to retrieve cities
        cur.execute(sql_query)

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
