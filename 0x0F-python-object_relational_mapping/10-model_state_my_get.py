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

    try:
        # Query the database; retrieve the specific 'State' objects
        states = session.query(State).filter(State.name == sys.argv[4]).first()

        # check if state is found
        if states is not None:
            print("{}".format(states.id))
        else:
            print("Nothing")

    except Exception as e:
        print("Error", e)

    finally:
        # Close the instance of Session
        session.close()
