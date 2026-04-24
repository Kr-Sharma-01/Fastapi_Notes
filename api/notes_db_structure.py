from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column , Integer , String

Base = declarative_base()

class notes (Base):
    __tablename__ = "notes"
    sub_code  = Column (Integer, primary_key=True, index=True)
    sub_name = Column(String)
    unit = Column(Integer)
    summary = Column(String)
