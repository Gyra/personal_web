# -*- coding: utf-8 -*-

'''
This is the ORM connecting MySQL
'''

from sqlalchemy import Column, String, create_engine
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
