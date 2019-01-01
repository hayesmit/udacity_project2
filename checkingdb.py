from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, User, Event
engine = create_engine('sqlite:///dontForget.db')
Base.metadata.bind=engine
DBSession = sessionmaker(bind=engine)
session = DBSession()

thisuser = session.query(User).filter_by(email='email1')
thisone = thisuser.id
myevents = session.query(Event).filter_by(user_id=thisone).all()

for eachevent in myevents:
    print(eachevent)
