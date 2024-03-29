#!/usr/bin/python3
import MySQLdb
from sys import argv

if len(argv) < 5 or len(argv) > 5:
    print("The script take four arguments")
    print("Exemple: ./5-filter_cities.py root root hbtn_0e_4_usa Texas")
else:
    conn = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                           passwd=argv[2], db=argv[3], charset="utf8")
    cur = conn.cursor()
    query1 = f"SELECT id FROM states WHERE name LIKE '{argv[4]}'"
    query = f"SELECT name FROM cities where state_id=({query1}) \
    ORDER BY id ASC"
    cur.execute(query)
    rows = cur.fetchall()
    print(", ".join(city[0] for city in rows))
    cur.close()
    conn.close()
