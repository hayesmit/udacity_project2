from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
import os
import sys

Base = declarative_base()


class User(Base):
    __tablename__ = 'user'
    email = Column(String(80), nullable=False, unique=True)
    id = Column(Integer, primary_key=True)

    @property
    def serialize(self):
        return{
            'email': self.email,
            'id': self.id,
        }

class Event(Base):
    __tablename__ = 'event'
    id = Column(Integer, primary_key=True)
    category = Column(String(20), nullable=False,)
    items = Column(String(1000), nullable=True, )
    name = Column(String(80), nullable=False, )
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(User)

    @property
    def serialize(self):
        return {
            'id': self.id,
            'items': self.items,
            'name': self.name,
            'category': self.category,
        }


engine = create_engine('sqlite:///dontForget.db')

Base.metadata.create_all(engine)