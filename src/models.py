import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class FavoriteCharacter(Base):
    __tablename__ = 'favoritecharacter'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'), nullable=False)
    character_id = Column(Integer, ForeignKey('character.id'), nullable=False)

    def to_dict(self):
        return {}
    
class FavoritePlanet(Base):
    __tablename__ = 'favoriteplanet'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'), nullable=False)
    planet_id = Column(Integer, ForeignKey('planet.id'), nullable=False)

    def to_dict(self):
        return {}


class User(Base):
    __tablename__ = 'user'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    email = Column(String(100), nullable=False)
    password = Column(String(250), nullable=False)
    favorite_character = relationship(FavoriteCharacter)
    favorite_planet = relationship(FavoritePlanet)


class Character(Base):
    __tablename__ = 'character'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    heigth = Column(Integer, nullable=False)
    mass = Column(Integer, nullable=False)
    hair_color = Column(String(10), nullable=False)
    skin_color = Column(String(10), nullable=False)
    eye_color= Column(String(10), nullable=False)
    birth_year = Column(String(10), nullable=False)
    gender = Column(String(10), nullable=False)
    favorite_character = relationship(FavoriteCharacter)


    def to_dict(self):
        return {}

class Planet(Base):
    __tablename__ = 'planet'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    diameter = Column(Integer, nullable=False)
    rotation_period = Column(Integer, nullable=False)
    orbital_period = Column(Integer, nullable=False)
    gravity = Column(String(20), nullable=False)
    population= Column(String(10), nullable=False)
    favorite_planet = relationship(FavoritePlanet)

    def to_dict(self):
        return {}



## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
