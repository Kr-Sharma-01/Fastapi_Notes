
# This file contains the database connection and session management for the application.
# It uses SQLAlchemy to connect to a PostgreSQL database and manage sessions for database operations.

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker 

Session = sessionmaker()
db_url = "postgresql://postgres:Krish2425@localhost:5432/first_db"
engine = create_engine(db_url)
session = sessionmaker(autoflush=False , autocommit=False  , bind=engine)
