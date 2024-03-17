#!/usr/bin/python3
"""adds new 'State' objects from the database"""
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

    # Create a new 'State' object for Louisiana
    new_state = State(name='Louisiana')

    # Add the new 'State' object to the database
    session.add(new_state)

    # Commit the new 'State' object to the database
    session.commit()

    # Print id of the newly added state
    print(new_state.id)
