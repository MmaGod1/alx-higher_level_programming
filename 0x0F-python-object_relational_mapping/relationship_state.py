#!/usr/bin/python3
"""
Contains State class from the Base class
"""
from sqlalchemy import Column, Integer, String, MetaData
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

meta = MetaData()
Base = declarative_base(metadata=meta)


class State(Base):
    """
    Defined class attributes, id and name of each state
    """
    __tablename__ = 'states'
    id = Column(Integer, unique=True, nullable=False, primary_key=True)
    name = Column(String(128), nullable=False)
    cities = relationship("City", backref="states", cascade="all, delete")
