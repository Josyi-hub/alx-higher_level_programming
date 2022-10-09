#!/usr/bin/python3
import sys
import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if len(sys.argv) > 4 or len(sys.argv) < 4:
    print("The script take three arguments: mysql username, password, dbname")
    print("Exemple : /7-model_state_fetch_all.py root root hbtn_0e_6_usa")
    exit()
else:
    username = sys.argv[1]
    password = sys.argv[2]
    dbname = sys.argv[3]

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(username, password, dbname)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session(engine)
    for state in session.query(State).order_by(State.id).all():
        print("{}: {}".format(state.id, state.name))
    session.close()
