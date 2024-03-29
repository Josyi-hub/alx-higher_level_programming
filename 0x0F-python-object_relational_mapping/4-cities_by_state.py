#!/usr/bin/python3
import sys
import MySQLdb

if len(sys.argv) > 4 or len(sys.argv) < 4:
    print("The script take three arguments: mysql username, password, dbname")
    print("Exemple : ./4-cities_by_state.py root root hbtn_0e_4_usa")
    exit()
else:
    username = sys.argv[1]
    password = sys.argv[2]
    dbname = sys.argv[3]
    conn = MySQLdb.connect(host="localhost", port=3306, user=username,
                           passwd="root", db=dbname, charset="utf8")
    cur = conn.cursor()
    comm = "SELECT cities.id, cities.name, states.name FROM cities, states wh\
ere cities.state_id=states.id ORDER BY id ASC"
    cur.execute(comm)
    query_rows = cur.fetchall()
    for row in query_rows:
        print(row)
    cur.close()
    conn.close()
