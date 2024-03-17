#!/usr/bin/python3
"""  script that lists all states from hbtn_0e_0_usa the database  """
import MySQLdb
import sys


if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3], port=3306)
    cur = db.cursor()

    similar = sys.argv[4]
    cur.execute("SELECT * FROM states WHERE name LIKE %s", (similar, ))
    rows = cur.fetchall()

    for row in rows:
        print(row)

    cur.close()
    db.close()
