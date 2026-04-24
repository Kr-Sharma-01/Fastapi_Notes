from fastapi import FastAPI , Depends
from Fastapi.api.models import product
from Fastapi.api.database import session , engine
from Fastapi.api import database_models
from sqlalchemy.orm import Session 
from sqlalchemy import asc


app = FastAPI()

database_models.Base.metadata.create_all(bind=engine)

@app.get("/")
def Welcome():
    return "Welcome !"

products = [
    product(id=1, name="Laptop", description="A high-performance laptop", price=29999.99, quantity=10),
    product(id=2, name="Smartphone", description="A latest model smartphone", price=6999.99, quantity=20),
    product(id=3, name="Headphones", description="Noise-cancelling headphones", price=1999.99, quantity=15),
    product(id=4, name ="Smartwatch", description="A latest model smartwatch", price = 1499.99, quantity = 25),
    product(id=5, name= "Speaker", description = "Great bass", price= 1999.99, quantity = 30)
]
#python database code to insert data into database

def get_db ():
    db = session()
    try:
        yield db
    finally :
        db.close()     


def db_init():
    db = session()
    for product in products:
        db.add(database_models.products(**product.model_dump()))
    db.commit()

#get all products

@app.get("/products")
def get_all_products(db : Session = Depends(get_db) ):
    db_products = db.query(database_models.products).order_by(database_models.products.id.asc()).all()
    return db_products

#index specific

@app.get("/products/{id}")
def specific_product(id :int , db : Session = Depends(get_db) ):
    db_product = db.query(database_models.products).filter(database_models.products.id == id).first()
    if db_product:
         return db_product
    else:
        return "Product not found"

#create a new product

@app.post("/products")
def add_product(product : product , db : Session = Depends(get_db) ):
    db.add(database_models.products(**product.model_dump()))
    db.commit()
    return "Product added"

#update a product

@app.put("/products/{id}")
def update_product(id :int , product : product , db : Session = Depends(get_db) ):
       db_product = db.query(database_models.products).filter(database_models.products.id == id).first()
       if db_product :
        db_product.name = product.name 
        db_product.description = product.description
        db_product.price = product.price
        db_product.quantity = product.quantity
        db.commit()

        return "Product updated"
       else :
         return "Not found"  

#delete a product

@app.delete("/products/{id}")
def delete_product(id :int  , db : Session = Depends(get_db) ):
    db_product = db.query(database_models.products).filter(database_models.products.id == id).first()
    if db_product:
        db.delete(db_product)
        db.commit()
        return "Product deleted"
    return "Not found"
            