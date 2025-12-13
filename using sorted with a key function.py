def sorting_key(t):
    return t[1]

d = {1:3, 3:1 , 4:1}

print(sorted(d.items(), key = sorting_key))