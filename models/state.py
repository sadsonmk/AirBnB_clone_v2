#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy.orm import relationship
from sqlalchemy import Column, String
from models.city import City


class State(BaseModel, Base):
    """ State class """
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)
    cities = relationship('City', back_populates="state")

    @property
    def cities(self):
        from models import storage
        towns = storage.all(City)

        obj = {}
        if len(towns) > 1:
            for key, value in towns.items():
                if value.state_id == self.id:
                    obj[key] = value
        return obj
