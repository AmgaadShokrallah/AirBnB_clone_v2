#!/usr/bin/python3
""" City Module for HBNB """
from sqlalchemy import Column, ForeignKey, String
from models.base_model import BaseModel, Base
from sqlalchemy.orm import relationship


class City(BaseModel, Base):
    """ city for a MySQL database.

    Attributes:
        __tablename__ (str): name of store Cities.
        name (sqlalchemy String): name of the City.
        state_id (sqlalchemy String): state id of City.
    """
    __tablename__ = "cities"
    name = Column(String(128), nullable=False)
    state_id = Column(String(60), ForeignKey("states.id"), nullable=False)
