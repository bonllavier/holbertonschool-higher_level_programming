#!/usr/bin/python3
"""
module 3
"""
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
import model_state
Base = declarative_base()


class City(Base):
    """
    class State
    """
    __tablename__ = 'cities'
    id = Column(Integer, primary_key=True, nullable=False)
    name = Column('name', String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'))
