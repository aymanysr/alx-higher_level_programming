#!/usr/bin/python3
"""retrieve & prints a State object with the name passed as argument
from the database
"""
import sys
from model_state import Base, State
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

if __name__ == "__main__":
    # Create a new instance of Engine with the following arguments
    # echo=True provides a debug output
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)

    # Generate new Session objects when called
    Session = sessionmaker(bind=engine)

    # Create a new instance of Session
    session = Session()

    # Query the database; retrieve the specific 'State' objects
    states = session.query(State).order_by(State.id)

    # check if state is the one that has been written
    found = False
    for state in states:
        if state.name == sys.argv[4]:
            print("{}".format(state.id))
            found = True
            break

    if not found:
        print("Nothing")

    # Close the instance of Session
    session.close()
