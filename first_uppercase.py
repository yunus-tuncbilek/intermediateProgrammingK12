# Exercise:
# Given a string find the index of its first uppercase letter.
# Use recursion.

def firstUppercase(s):
    if s[0].isupper(): # "A" <= s[0] <= "Z"
        return 0
    
    return 1 + firstUppercase(s[1:])

print(firstUppercase("downtown Vancouver"))