import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String,Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

# class Person(Base):
#     __tablename__ = 'person'
#     # Here we define columns for the table person
#     # Notice that each column is also a normal Python instance attribute.
#     id = Column(Integer, primary_key=True)
#     name = Column(String(250), nullable=False)

# class Address(Base):
#     __tablename__ = 'address'
#     # Here we define columns for the table address.
#     # Notice that each column is also a normal Python instance attribute.
#     id = Column(Integer, primary_key=True)
#     street_name = Column(String(250))
#     street_number = Column(String(250))
#     post_code = Column(String(250), nullable=False)
#     person_id = Column(Integer, ForeignKey('person.id'))
#     person = relationship(Person)


class User(Base):
    __tablename__ = 'user'
    id = Column(Integer,primary_key=True)
    username = Column(String(250),nullable=False)
    email = Column(String(250),nullable=False)
    password = Column(String(250),nullable=False)
    user_adm = Column(Boolean(True))

class Pet(Base):
    __tablename__ = 'pet'
    id = Column(Integer,primary_key=True)
    name = Column(String(250),nullable=False)
    type_pet = Column(String(250),nullable=False)
    age = Column(String(250),nullable=False)
    history = Column(String(250),nullable=False)
    behaviour = Column(String(250),nullable=False)
    breed = Column(String(250),nullable=False)
    size = Column(String(250),nullable=False)
    other = Column(String(250),nullable=False)

class Adopt(Base):
    __tablename__ = 'adopt'
    id = Column(Integer,primary_key=True)
    name = Column(String(250),nullable=False)
    address = Column(String(250),nullable=False)
    telephone = Column(String(250),nullable=False)
    mobile_phone = Column(String(250),nullable=False)
    email = Column(String(250),nullable=False)
    pet_id = Column(Integer, ForeignKey('pet.id'))
    pet = relationship(Pet)

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')