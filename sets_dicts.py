
#set definition can be done in two ways
s = set() # empty set 
print(s)
s = {1,2}
print(s)


# dictionaries can be defined similarly
d = {}
print(d)
d = {"Yunus": "Vancouver", "Chris": "NYC"}
print(d)

# the main difference between a set and a dict
#  is a set doesn't contain values for the keys

#### O(1) lookup of a key

# value lookup in a dict
print(d["Yunus"])
print(d.get("Yunus", "Not Found"))

# membership lookup in a set
print(1 in s)
print(50 in s) 

#### O(1) addition/removal of a key

# add key to a dict
d["Yahia"] = "Seattle"
print(d)

# add to a set
s.add(50)
print(50 in s)

# remove key from a dict
del d["Yahia"]
print(d)

# remove from a set
#   NOT del s[50], because s does not have a indexing or key,value pairs
s.remove(50)
print(50 in s)
