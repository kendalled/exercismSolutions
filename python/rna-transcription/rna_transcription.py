def to_rna(n):

    res = ''
    
    for elem in n:
        if(elem == 'G'):
            res += 'C'
        if(elem == 'C'):
            res += 'G'
        if(elem == 'T'):
            res += 'A'
        if(elem == 'A'):
            res += 'U'
        if(elem not in 'GCTA'):
            return('')
        
    return(res)
