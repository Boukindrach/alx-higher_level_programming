#!/usr/bin/python3
"""
Lists all State objects and corresponding
City objects contained in the database.
"""
import sys
from relationship_state import Base, State
from relationship_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == '__main__':
    db_user = sys.argv[1]
    db_password = sys.argv[2]
    db_name = sys.argv[3]

    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.
                           format(db_user, db_password, db_name),
                           pool_pre_ping=True)

    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    s = session.query(State).outerjoin(City).order_by(State.id, City.id).all()
    for state in s:
        print(f"{state.id}: {state.name}")
        for city in state.cities:
            print(f"    {city.id}: {city.name}")
    session.close()
