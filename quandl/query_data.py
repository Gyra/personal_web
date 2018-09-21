# -*- coding: utf-8 -*-

'''
This is to query data from quandl.com
'''
import numpy as np
import quandl

# get the list from the db
# get the last date from the db

# query data
quandl.ApiConfig.api_key = "4G_ca1goT6skQGee258K"
mydata = quandl.get("FRED/GDP", start_date="2001-12-31", end_date="2005-12-31", returns="numpy")

# update date in the db
# update data in the db

# calculation

# update the result in the db