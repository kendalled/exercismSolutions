def is_pangram(n):
    alph_lis = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
                'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    n = n.lower()
    for elem in n:
        if elem in alph_lis:
            alph_lis.remove(elem)
    if(alph_lis == []):
        return True
    else:
        return False
