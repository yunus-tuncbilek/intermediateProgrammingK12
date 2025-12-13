def sorting_key(t):
    return t[1]

d = {1:3, 3:1 , 4:1}

print(sorted(d.items(), key = sorting_key))

# d.items() returns a list of (key, value) pairs in d. The pairs are tuples
# d.keys() returns a list of the keys in d
# d.values() returns a list of the values in d

# A method is a part of a class. Anything that is called with a period is a method
#   d.items()
#   l.sort()
# A function is more general and applies to any function but mostly we use
#   this term for callables that are not methods
#   len(l) 
#   sorted(d.items)