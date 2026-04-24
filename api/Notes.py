from fastapi import FastAPI , Depends 
from Fastapi.api.notes_structure import notes 
from Fastapi.api import notes_db_structure
from Fastapi.api.notes_db import engine , session
from sqlalchemy.orm import Session
from sqlalchemy import asc

app = FastAPI()

notes_db_structure.Base.metadata.create_all(bind=engine)

Summary = [
    notes(sub_code = 1 , sub_name = "Fastapi" , unit = 1 , summary = "Fastapi is a modern day web framework for building API's with python that is fast, easy to use and production ready. It is built on top of Starlette for the web parts and Pydantic for the data parts. Fastapi is designed to be easy to use and learn, while also being powerful and flexible enough to handle complex applications."),
    notes(sub_code = 2 , sub_name = "SQLAlchemy" , unit = 1 , summary = "SQLAlchemy is a powerful ORM (Object-Relational Mapping) library for Python that provides a high-level interface for working with databases. It allows developers to interact with databases using Python objects and classes, abstracting away the underlying SQL queries."),
    notes(sub_code = 3 , sub_name = "Pydantic" , unit = 1 , summary = "Pydantic is a data validation and settings management library for Python. It provides a way to define data models using Python classes, and then validate and serialize data based on those models. Pydantic is often used in conjunction with FastAPI to define request and response models for API endpoints."),
    notes(sub_code = 4 , sub_name = "PostgreSQL" , unit = 1 , summary = "PostgreSQL is a powerful, open-source relational database management system (RDBMS) that is widely used for storing and managing data. It is known for its robustness, scalability, and support for advanced features such as transactions, concurrency, and extensibility. PostgreSQL is often used in web applications and APIs to store and retrieve data efficiently.")
]

def get_db ():
    db = session()
    try :
        yield db
    finally :
        db.close()    

def init ():
    db = session()
    for notes in Summary :
        db.add (notes_db_structure.notes(**notes.model_dump()))
    db.commit()


@app.get("/" , response_model = list[notes])
def Notes (db : Session = Depends (get_db)):
    db.notes = db.query(notes_db_structure.notes).order_by(asc(notes_db_structure.notes.sub_code)).all()
    return db.notes 
