'''

good?f f f f t  t  t  t  t
L = [1,2,5,7,10,14,15,18,20] # strictly increasing list of numbers
    [1,2,5,7,10] 
         ^
           [7,10]
            ^
              [10]

target = 10

At every turn, we remove half of the possibilities.
So, imagine len(L) = 2^k. In that case, binary search would halt in k steps.
Time complexity: O(log n)
Space complexity: O(1)

'''