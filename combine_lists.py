# Two-pointer approach
def combine_lists(list1, list2):
    if not list1: # empty list1 case
        return list2
    if not list2: # empty list2 case
        return list1
    
    i1, i2 = 0, 0
    res = []
    while i1 < len(list1) and i2 < len(list2): # indices are valid (no IndexError)
        a, b = list1[i1], list2[i2]

        if a > b: # list1 is ahead
            res.append(b)
            i2 += 1
        else: # list2 is ahead
            res.append(a)
            i1 += 1
    
    while i1 < len(list1): # exhaust list1
        res.append(list1[i1])
        i1 += 1

    while i2 < len(list2): # exhaust list2
        res.append(list2[i2])
        i2 += 1
    
    return res