#!/usr/bin/python3
"""
Module Lists all states that contain
letter a from database hbtn_0e_6_usa
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from model_state import Base, State


if __name__ == "__main__":
    engine = create_engine(
                            'mysql+mysqldb://{}:{}@localhost/{}'
                            .format(
                                        sys.argv[1],
                                        sys.argv[2],
                                        sys.argv[3]
                                            ),
                            pool_pre_ping=True
                                )
    session = Session(engine)
    found = False
    for state in session.query(State):
        if state.name == sys.argv[4]:
            print("{}".format(state.id))
            found = True
            break
    if found is False:
        print("Not found")

    session.close()
