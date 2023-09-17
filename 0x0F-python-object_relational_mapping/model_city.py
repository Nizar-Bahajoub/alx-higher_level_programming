#!/usr/bin/python3
"""
City class table
"""

from sys import argv
from model_state import Base, State
from sqlalchemy import Column, Integer, String
from sqlalchemy import ForeignKey


class City(Base):
    """Creates the City Class"""

    __tablename__ = 'cities'

    id = Column(Integer, nullable=False, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'))
