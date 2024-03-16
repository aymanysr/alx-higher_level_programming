#!/usr/bin/python3
"""
displays all values in the states table of hbtn_0e_0_usa
where name matches the argument.
"""

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
        sql_query = """
            SELECT cities.name
            FROM cities
            WHERE state_id = (SELECT id FROM states WHERE name = %s)
            ORDER BY id ASC
        """

        # Execute SQL query with sys.argv[4] as the state_name parameter
        cur.execute(sql_query, (sys.argv[4],))

        # Fetch all the rows in a list of tuples
        rows = cur.fetchall()

        # Display results
        if rows:
            print(', '.join(row[0] for row in rows))
        else:
            print("No cities found for the state '{}'".format(sys.argv[4]))

    except MySQLdb.Error as e:
        print("MySQL Error {}: {}".format(e.args[0], e.args[1]))
        sys.exit(1)

    finally:
        # Close cursor and database connection
        if 'cur' in locals() or 'cur' in globals():
            cur.close()
        if 'db' in locals() or 'db' in globals():
            db.close()
