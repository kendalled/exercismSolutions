# Kendall Jackson
# 06/27/17 - 2nd day of code every day self swear
# This program solves exercism, python problem 'isogram'
# letter_list revision thanks to user 'jarhill0' on exercism

def is_isogram(n):
    letter_list = list(n.lower())
    for elem in letter_list:
        if(letter_list.count(elem) > 1 and elem not in '!@#$%^&*() -'):
            return False
    return True
        
