from pydantic import BaseModel

class notes (BaseModel):
    sub_code : int 
    sub_name : str
    unit : int
    summary : str 

class config :
    from_attributes = True





