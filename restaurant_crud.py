# CRUD operation on database
# C = Create
# R = Read
# U = Update
# D = Delete

# configuration
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from database_setup import Restaurant, MenuItem, Base

engine = create_engine("sqlite:///restaurantmenu.db")
Base.metadata.bind = engine
DBsession = sessionmaker(bind=engine)
session = DBsession()

# Create
def create_restaurant(name):
    restaurant = Restaurant(name=name)
    session.add(restaurant)
    session.commit()

# Read
def get_restaurants():
    restaurants = session.query(Restaurant).all()
    return restaurants

def get_restaurant(id):
    restaurant = session.query(Restaurant).filter_by(id=id).one()
    return restaurant

# Update
def update_restaurant_name(id, new_name):
    restaurant = session.query(Restaurant).filter_by(id=id).one()
    restaurant.name = new_name
    session.add(restaurant)
    session.commit()

# Delete
def delete_restaurant(id):
    restaurant = session.query(Restaurant).filter_by(id=id).one()
    session.delete(restaurant)
    session.commit()
