import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    # PK
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    email = Column(String(250), unique=True)
    #CHILDREN
    favorites= relationship('favorites', back_populates='user')

class Character(Base):
    __tablename__ = 'character'
    # PK
    id = Column(Integer, primary_key=True)
    name = Column(String(250))
    age = Column(Integer)
    heigth = Column(Integer)
    eye_color = Column(Integer)
    #CHILDREN
    favorite= relationship('favorites', back_populates='characters')

class Planet(Base):
    __tablename__ = 'planet'
   # PK
    id = Column(Integer, primary_key=True)
    diameter = Column(Integer)
    gravity = Column(Integer)
    population = Column(Integer)
    climate = Column(String(250))
    #CHILDREN
    favorites= relationship('favorite', back_populates='planets')

class Starship(Base):
    __tablename__ = 'starship'
   # PK
    id = Column(Integer, primary_key=True)
    model = Column(String(250))
    starship_class = Column(String(250))
    crew = Column(Integer)
    passengers = Column(Integer)
    #CHILDREN
    favorites= relationship('favorite', back_populates='starships')

class Favorite(Base):
    __tablename__ = 'favorites'
    # PK
    id = Column(Integer, primary_key=True)

    # FK USER.
    user = relationship('user', back_populates='favorites')
    user_id = Column(Integer, ForeignKey('user.id'))
    # FK CHARACTERS.
    character = relationship('characters', back_populates='favorites')
    character_id = Column(Integer, ForeignKey('character.id'))
    # FK PLANETS.
    planet = relationship('planet', back_populates='favorites')
    planet_id = Column(Integer, ForeignKey('planet.id'))
    # FK STARSHIPS.
    starship = relationship('starship', back_populates='favorites')
    starship_id = Column(Integer, ForeignKey('starship.id'))

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
