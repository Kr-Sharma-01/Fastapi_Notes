
# This file contains the database models for the products table.
# It uses SQLAlchemy to define the structure of the products table and its columns.

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Integer , String , Float , Column 

Base = declarative_base()

class products(Base):

    __tablename__ = "products"

    id = Column(Integer , primary_key= True , index = True) 
    name = Column(String)
    description = Column(String) 
    price = Column(Float)
    quantity = Column(Integer )



