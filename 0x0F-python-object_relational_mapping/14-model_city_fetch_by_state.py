#!/usr/bin/python3
"""
prints all City objects from the database hbtn_0e_14_usa
"""


from sys import argv
from model_state import Base, State
from model_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    engine = create_engine(
            'mysql+mysqldb://{}:{}@localhost/{}'.format(
                argv[1], argv[2], argv[3]
                ),
            pool_pre_ping=True)

    Session = sessionmaker(bind=engine)
    session = Session()

    cities = session.query(City).order_by(City.id)

    for city in cities:
        state = session.query(State).filter(State.id == city.state_id).first()
        if state:
            print("{}: ({}) ({})".format(state.name, city.id, city.name))
