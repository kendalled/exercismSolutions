# Kendall Jackson
# 07/15/17
# This program solves exercism, python problem 'gigasecond'
# timedelta takes argument 'seconds' rather than default - 'days'

import datetime as dt

def add_gigasecond(x):
   return x + dt.timedelta(seconds=10**9)


    
