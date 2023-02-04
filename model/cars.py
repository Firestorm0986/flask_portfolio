from random import randrange
from datetime import date
import os, base64
import json

from __init__ import app, db
from sqlalchemy.exc import IntegrityError
from werkzeug.security import generate_password_hash, check_password_hash

class Cars(db.Model):
    __tablename__ = 'cars'  # table name is plural, class name is singular

    # Define the User schema with "vars" from object
    id = db.Column(db.Integer, primary_key=True)
    _name = db.Column(db.String(255), unique=False, nullable=False)
    _car = db.Column(db.String(255), unique=False, nullable=False)
    _password = db.Column(db.String(255), unique = False, nullable = True)
    # Defines a relationship between User record and Notes table, one-to-many (one user to many notes)
    # constructor of a User object, initializes the instance variables within object (self)
    def __init__(self, name, car, id):
        self.id = id
        self._name = name    # variables with self prefix become part of the object, 
        self._car = car
        self._password = password

    @property
    def name(self):
        return self._name
    
    # a setter function, allows name to be updated after initial object creation
    @name.setter
    def name(self, name):
        self._name = name

    @property
    def password(self):
        return self._password
    
    # a setter function, allows name to be updated after initial object creation
    @password.setter
    def password(self,password):
        self._password = password

    @property
    def car(self):
        return self._car
    
    # a setter function, allows name to be updated after initial object creation
    @name.setter
    def name(self, car):
        self._name = car

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
            "name": self.name,
            "car": self.car,
            "password": self.passwords,
        }

    # CRUD update: updates user name, password, phone
    # returns self
    def update(self, name="", car="", password =""):
        """only updates values with length"""
        if len(name) > 0:
            self.name = name
        if len(car) > 0:
            self.car = car
        if len(password) > 0:
            self.password = password
        db.session.commit()
        return self

    # CRUD delete: remove self
    # None
    def delete(self):
        db.session.delete(self)
        db.session.commit()
        return None
"""CRUD DONE"""

def initCars():
    """Create database and tables"""
    db.create_all()
    """Tester data for table"""
    u1 = Cars(id = 1, name='Thomas Edison', car='Tesla Model y', password = 'idk')
    u2 = Cars(id = 2, name='Nicholas Tesla', car='Pagani', password = 'idk')
    u3 = Cars(id = 3, name='Alexander Graham Bell', car='Ferrari', password = 'idk')
    u4 = Cars(id = 4, name='Eli Whitney', car='Lexus', password = 'idk')
    u5 = Cars(id = 5, name='John Mortensen', car='NIO', password = 'idk')

    cars = [u1, u2, u3, u4, u5]

    for car in cars:
        try:
            car.create()
        except IntegrityError:
            db.session.remove()
            print(f"Records exist, duplicate email, or error: {car.id}")

    """Builds sample user/note(s) data"""
    