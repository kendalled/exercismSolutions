# Kendall Jackson
# 06/28/17 - 3rd day of code every day self swear
# This program solves exercism, python problem 'word-count'

def word_count(n):

    # Makes string words separated by spaces only
    for char in ('!@#$%^&*(),./;:_-+={}[]"'):
        n = n.replace(char, ' ')

    word_list = n.lower().split()
    res_dict = {}

    for elem in word_list:
        
        if(elem not in '!@#$%^&*(),./;'):
            dict_key = elem
            res_dict[elem] = word_list.count(elem)

    return res_dict
