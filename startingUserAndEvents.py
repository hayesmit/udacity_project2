from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, User, Event
engine = create_engine('sqlite:///dontForget.db')
Base.metadata.bind=engine
DBSession = sessionmaker(bind=engine)
session = DBSession()

newuser = User(email='mitchell.hayes.portland@gmail.com')
session.add(newuser)
session.commit()

newevent = Event(name='camping', category='overnight', items='tent, sleepingbag, food, chainsaw, dog supplies, ')


