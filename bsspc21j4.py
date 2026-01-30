import sys

input = sys.stdin.readline

X, N = map(int,input().split())

# map(function, list):
#   maps function onto list of items
#   returns another "list-like" object with the results
#       of the mapping

# X = int(X)
# N = int(N)

soups = []
for i in range(N):
    t, f = map(int, input().split())
    soups.append([t,f])

# print(soups)

soups.sort(key=lambda x: x[1]) # sort soups based on the second component

# current time = 0
# [[5, 1], -> current time allows me to drink at minute 1, but the soup is too hot
# [3, 2], -> current time again allows me to drink this and it'll cool enough
    # current time = 2 + 1 = 3
# [2, 3]] -> current time (3) does allow me to drink at minute 3, the soup is cool
    # current time = 3 + 1 = 4

# X = 5
# 50 50 -> drinkable. Drink at minute 50-5 = 45. Current time = 45 + 1 = 46
# 50 50 -> drinkable. 
#   Drink at minute max(current time, t_i - X) = max(46, 50-5) = 46. 
#   Current time = 46 + 1 = 47
# 50 50 -> minute 47

# print(soups)


# Solution function
def solve():
    # Fast I/O
    input = sys.stdin.read().split()
    if not input:
        return
    
    X = int(input[0])
    N = int(input[1])
    
    soups = []
    idx = 2
    for _ in range(N):
        T_i = int(input[idx])
        F_i = int(input[idx+1])
        idx += 2
        
        # Earliest time it's cool enough
        earliest = max(0, T_i - X)
        
        # Only consider bowls that can actually reach the threshold
        if earliest <= F_i:
            soups.append((earliest, F_i))

    # Sort by deadline (F_i) to drink bowls that expire soonest first
    soups.sort(key=lambda x: (x[1], x[0]))

    count = 0
    current_time = 0
    
    for earliest, deadline in soups:
        # We drink it at either current time or when it's cool enough
        drink_at = max(current_time, earliest)
        
        if drink_at <= deadline:
            count += 1
            current_time = drink_at + 1
            
    print(count)

solve()