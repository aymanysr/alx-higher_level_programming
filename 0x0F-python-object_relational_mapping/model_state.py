#!/usr/bin/python3
"""
Module that defines the States class
representing the states table in the database hbtn_0e_6_usa
"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    """Represents the states table in MySQL database.
    __tablename__ (str): The name of the MySQL table to store States.
    id (int): The state's id.
    name (str): The state's name.
    """
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
