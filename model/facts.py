from random import randrange
from datetime import date
import os, base64
import json

from __init__ import app, db
from sqlalchemy.exc import IntegrityError


class Facts(db.Model):
    __tableindustry__ = 'facts'  # table industry is plural, class industry is singular

    # Define the User schema with "vars" from object
    id = db.Column(db.Integer, primary_key=True)
    _car = db.Column(db.String(255), unique=False, nullable=False)
    _industry = db.Column(db.String(255), unique=False, nullable=False)
    _knew = db.Column(db.String(255), unique = False, nullable = False)
    # Defines a relationship between User record and Notes table, one-to-many (one user to many notes)
    # constructor of a User object, initializes the instance variables within object (self)
    def __init__(self, car, industry, id, knew):
        self.id = id
        self._industry = industry   # variables with self prefix become part of the object, 
        self._car = car
        self._knew = knew

    @property
    def industry(self):
        return self._industry
    
    # a setter function, allows industry to be updated after initial object creation
    @industry.setter
    def industry(self, industry):
        self._industry = industry

    @property
    def knew(self):
        return self._knew
    
    # a setter function, allows industry to be updated after initial object creation
    @knew.setter
    def knew(self, knew):
        self._knew = knew

    @property
    def car(self):
        return self._car
    
    # a setter function, allows industry to be updated after initial object creation
    @car.setter
    def industry(self, car):
        self._car = car

    def __str__(self):
        return json.dumps(self.read())

    def create(self):
        try:
            # creates a person object from User(db.Model) class, passes initializers
            db.session.add(self)  # add prepares to persist person object to Users table
            db.session.commit()  # SqlAlchemy "unit of work pattern" requires a manual commit
            return self
        except IntegrityError:
            db.session.remove()
            return None

    # CRUD read converts self to dictionary
    # returns dictionary
    def read(self):
        return {
            "id": self.id,
            "industry": self.industry,
            "car": self.car,
            "knew": self.knew,
        }

    # CRUD update: updates user industry, knew, phone
    # returns self
    def update(self, industry="", car="", knew = ""):
        """only updates values with length"""
        if len(industry) > 0:
            self.industry = industry
        if len(car) > 0:
            self.car = car
        if len(knew) > 0:
            self.knew = knew
        db.session.commit()
        return self

    # CRUD delete: remove self
    # None
    def delete(self):
        db.session.delete(self)
        db.session.commit()
        return None
"""CRUD DONE"""

def initFacts():
    """Create database and tables"""
    db.create_all()
    """Tester data for table"""
    u1 = Facts(id = 1, industry='Thomas Edison', car='Tesla Model y', knew = 'False')
    u2 = Facts(id = 2, industry='Nicholas Tesla', car='Pagani', knew = 'False')
    u3 = Facts(id = 3, industry='Alexander Graham Bell', car='Ferrari', knew = 'False')
    u4 = Facts(id = 4, industry='Eli Whitney', car='Lexus', knew = 'False')
    u5 = Facts(id = 5, industry='John Mortensen', car='NIO', knew = 'False')

    facts = [u1, u2, u3, u4, u5]

    for fact in facts:
        try:
            fact.create()
        except IntegrityError:
            db.session.remove()
            print(f"Records exist, duplicate email, or error: {fact.id}")

    """Builds sample user/note(s) data"""
    