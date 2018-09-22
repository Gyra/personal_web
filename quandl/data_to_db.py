# -*- coding: utf-8 -*-

'''
This is the ORM connecting MySQL
'''

from sqlalchemy import Column, String, DateTime, Float, create_engine, func
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import numpy

# create the base class [?]
Base = declarative_base()

# declare the User class
class FinanceData(Base):
    # name of the table
    __table_name__ = 'finance_data'

    # table structure
    data_date = Column(DateTime, default=func.now(), primary_key=True)
    us_gdp = Column(Float(10,6), default=0.0, nullable=True)
    # initial db connection
    engine = create_engine('mysql+mysqlconnector:/root:password@localhost:3306/personal_web')

    # create DBSession 
    DBSession = sessionmaker(bind=engine)
