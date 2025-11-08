word = input()

vowels = [s for s in word if s in 'aeiouAEIOU']
vowels = vowels[::-1]

"""hello -> vowels = ['o', 'e']
I have to pop the first element of vowels.
The issue is popping the left element of a list using the method .pop(0),
    a new index is constructed -> a long runtime. """

# deque = double-ended queue
from collections import deque # Using deque for efficient O(1) popleft operation
vowels = deque(vowels)

res = []

for s in word:
    if s in 'aeiouAEIOU':
        res.append(vowels.popleft())
    else:
        res.append(s)

print(''.join(res))