R, C, M = int(input()), int(input()), int(input())


'''returns the cost of the entry in row i and column j (zero indexed)'''
def cost(i, j):
    num_entries_before = 0

    #  add the entries in previous rows
    num_entries_before += C * i

    # add the entries in the current row
    num_entries_before += j

    result = num_entries_before % M + 1 # [0-(M-1)] -> [1-M]

    return result
'''
Algorithm: One-Dimensional Dynamic Programming

Starting with the lowest row, calculate the lowest cost of continuously 
  reaching every entry in the row. An array dp will hold the lowest costs.

  This amount can be calculated as:

   dp[current] = 
     min(dp[bottom left], dp[bottom], dp[bottom right]) + cost(current)
'''
dp = [0] * C

for i in reversed(range(R)): # [R-1, R-2, ... , 1, 0]
    prev = dp.copy() # record the bottom row's dp

    for j in range(C):
        if j > 0 and j < C - 1: # if we're away from the edges
            dp[j] = min(prev[j - 1], prev[j], prev[j + 1]) + cost(i, j)
        elif j == 0:
            dp[j] = min(prev[j], prev[j + 1]) + cost(i, j)
        elif j == C - 1:
            dp[j] = min(prev[j - 1], prev[j]) + cost(i, j)

print(dp) # top row's costs

print(min(dp))
