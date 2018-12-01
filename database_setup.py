import sys

from sqlalchemy import Column, ForeignKey, Integer, String

from sqlalchemy.ext.declarative import declarative_base

from sqlalchemy.orm import relationship

from sqlalchemy import create_engine

Base = declarative_base()


class User(Base):
    __tablename__ = 'user'
    email = Column(String(80), nullable=False, )
    id = Column(Integer, primary_key=True)


class Event(Base):
    __tablename__ = 'event'
    id = Column(Integer, primary_key=True)
    items = Column(String(1000), nullable=True, )
    name = Column(String(80), nullable=False, )
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(User)


engine = create_engine('sqlite://dontForget.db')

Base.metadata.create_all(engine)
