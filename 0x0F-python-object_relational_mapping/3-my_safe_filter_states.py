#!/usr/bin/python3
"""
Python script that takes in an argument and displays all values in the states
table of hbtn_0e_0_usa where name matches the argument safe from MySQL injections
"""

import MySQLdb
from sys import argv

conn = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                       passwd=argv[2], db=argv[3], charset="utf8")
cursor = conn.cursor()
cursor.execute("SELECT * FROM states WHERE name LIKE %s ORDER BY id ASC", (argv[4],))
rows = cursor.fetchall()
for row in rows:
    if row[1] == argv[4]:
        print(row)
cursor.close()
conn.close()
