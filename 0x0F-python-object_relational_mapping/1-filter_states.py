#!/usr/bin/python3
"""
python script that lists all states from the database hbtn_0e_0_usa with a name
starting with N
"""


import sys
import MySQLdb

username = sys.argv[1]
passwd = sys.argv[2]
dbname = sys.argv[3]

if __name__ == "__main__":
    conn = MySQLdb.connect(host="localhost", port=3306, user=username,
                       passwd=passwd, db=dbname, charset="utf8")
    cur = conn.cursor()
    cur.execute("SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id ASC")
    rows = cur.fetchall()
    for row in rows:
        if row[1][0] == 'N':
            print(row)
    cur.close()
    conn.close()
