from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker 
import os 
from dotenv import load_dotenv 

load_dotenv()

db_url = os.getenv("DATABASE_URL")

engine = create_engine(db_url , echo = True)

session = sessionmaker(autoflush= False , autocommit = False , bind = engine )


