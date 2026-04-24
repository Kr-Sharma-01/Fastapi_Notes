
# This file contains the Pydantic model for the product data.
# It defines the structure of the product data that will be used in the API endpoints. 

from pydantic import BaseModel

class product(BaseModel):

    id : int 
    name : str
    description : str 
    price : float
    quantity : int 

