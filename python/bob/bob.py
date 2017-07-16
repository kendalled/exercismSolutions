# Kendall Jackson
# 07/15/17
# This program solves exercism, python problem 'bob'
# I know that the dedicated methods are not needed, but I needed to practice using them.


def all_caps(y):
    return y.isupper()

def is_question(z):
    return z.endswith('?')

def hey(x):
    if x.strip() == '':
        return('Fine. Be that way!')
    if all_caps(x.strip()):
        return('Whoa, chill out!')
    if is_question(x.strip()):
        return('Sure.')

    return('Whatever.')
