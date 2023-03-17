#!/usr/bin/python3
"""
List all cities
from the database hbtn_0e_4_usa
"""
import sys
import MySQLdb


def main():
    connectionDb = MySQLdb.connect(
                                host="localhost",
                                port=3306,
                                user=sys.argv[1],
                                passwd=sys.argv[2],
                                db=sys.argv[3],
                                charset="utf8"
                                    )
    cur = connectionDb.cursor()
    query = """SELECT cities.id, cities.name, states.name
                FROM cities INNER JOIN states ON cities.state_id=states.id"""
    cur.execute(query)
    row = cur.fetchall()
    for n in row:
        print(n)
    cur.close()
    connectionDb.close()


if __name__ == "__main__":
    main()
