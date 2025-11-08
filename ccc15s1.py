# Runtime: O(N), N=number of integers given
# Space complexity: O(N) in the worst case (when there are no zeros)

N = int(input())

stack = [] # stacks are lists in Python
for _ in range(N):
    num = int(input())

    if num == 0:
        stack.pop() # pop = popping the last element of list stack
    
    else:
        stack.append(num) # push = inserting to the end of list stack

if stack:
    print(sum(stack))

else:
    print(0)