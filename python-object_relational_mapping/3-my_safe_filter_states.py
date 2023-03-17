#!/usr/bin/python3
""" Module Take in argument and display all values """
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
    search = sys.argv[4]
    cur.execute("""SELECT  id, name FROM states where name = %s
            ORDER by id ASC""",(search))
    row = cur.fetchall()
    for n in row:
        print(n)
    cur.close()
    connectionDb.close()


if __name__ == "__main__":
    main()
