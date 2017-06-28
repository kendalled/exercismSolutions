# Kendall Jackson
# 06/27/17 - 2nd day of code every day self swear
# This program solves exercism, python problem 'leap'

def is_leap_year(n):
    return((n % 400 == 0) or (n % 100 != 0 and n % 4 == 0))

    
