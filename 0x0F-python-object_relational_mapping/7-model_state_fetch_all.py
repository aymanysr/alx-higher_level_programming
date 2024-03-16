#!/usr/bin/python3
"""retrieve & prints all 'State' objects from the database """
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

    # Query the database; retrieve all 'State' objects
    for state in session.query(State).order_by(State.id):
        print("{}: {}".format(state.id, state.name))

    # Close the instance of Session
    session.close()
