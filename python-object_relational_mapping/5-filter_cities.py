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
    state_name = sys.argv[4]
    cur.execute("SELECT cities.name FROM cities \
    JOIN states ON cities.state_id = states.id WHERE states.name LIKE %s \
    ORDER BY cities.id", (state_name,))
    row = cur.fetchall()
    re = ""
    for n in row:
        re += n[0] + ", "
    print(re[0:-2:])
    cur.close()
    connectionDb.close()


if __name__ == "__main__":
    main()
