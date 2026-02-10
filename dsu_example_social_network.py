import sys

# Increase recursion depth for deep trees
sys.setrecursionlimit(200000)

# Fast I/O: Reads all input at once and splits by whitespace
input = sys.stdin.readline

n, m = map(int, input().split())  # Number of people

# TODO: Initialize your DSU structures here
# Hint: You need an array to keep track of parents
parent = [] 

def find(i):
    # TODO: Implement find with Path Compression
    # 1. If i is its own parent, return i
    # 2. Otherwise, recursively find the parent and 
    #    update parent[i] (Path Compression)
    pass

def union(i, j):
    # TODO: Implement union
    # 1. Find the roots of both i and j
    # 2. If roots are different, point one to the other
    pass

# Processing the operations
idx = 2
for _ in range(m):
    op_type, u, v = map(int, input().split())
    
    if op_type == 1:
        # Task: Link user u and v
        union(u, v)
    elif op_type == 2:
        # Task: Check if u and v are in the same set
        # TODO: Use your find function to check if they share a root
        if ...: # Replace with your condition
            print("YES")
        else:
            print("NO")