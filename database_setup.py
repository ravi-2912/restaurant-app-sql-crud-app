# configuration
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy import create_engine

# configuration
Base = declarative_base()

# class for sql table
class Restaurant(Base):
    # table name
    __tablename__ = "restaurant"
    # mapper
    name = Column(String(80), nullable=False)
    id = Column(Integer, primary_key=True)

# class for sql table
class MenuItem(Base):
    # table name
    __tablename__ = "menu_item"
    # mapper
    name = Column(String(80), nullable=False)
    id = Column(Integer, primary_key=True)
    course = Column(String(250))
    description = Column(String(250))
    price = Column(String(8))

    # relationships
    restaurant_id = Column(Integer, ForeignKey("restaurant.id"))
    restaurant = relationship(Restaurant)

if __name__ == "__main__":
    # configuration end of file
    engine = create_engine('sqlite:///restaurantmenu.db')
    # for PostgreSQL
    # engine = create_engine("postgresql://ravi_:ravi_@localhost:5432/restaurantmenu", echo=True)
    Base.metadata.create_all(engine)
