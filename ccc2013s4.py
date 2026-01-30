from collections import deque
import sys

input = sys.stdin.readline

nm = sys.stdin.readline()
n, m = map(int, nm.split())

# adjacency list representation of graph
#   other options: adjacency matrix, edge list
visited = set()
adjlist = []
# [[1], [2], [0] ] -> 3 nodes, 3 edges (looks like a triangle)
for i in range(n+1):
    adjlist.append(set())

for i in range(m):
    comparison = sys.stdin.readline()
    pa, c = map(int,comparison.split())
    adjlist[pa].add(c)

pq = sys.stdin.readline()
pq = map(int,pq.split())
pq = list(pq)
# q = deque()

# edge cases
if pq[0] == pq[1]:
    print('unknown')
    sys.exit()
if len(adjlist[pq[0]]) == 0 and len(adjlist[pq[1]]) == 0:
    print('unknown')
    sys.exit()

for i in range(2):
    q = deque([pq[i]]) #pipeline
    visited.add(pq[i]) #visited set
    while q:
        curr = q.popleft() #current node on pipeline 

        # # Option 1: process current node here
        # if curr == pq[1-i]:
        #     if i == 0:
        #         print('yes')
        #     else:
        #         print('no')
        #     sys.exit()

        for nei in adjlist[curr]: #children/neighbors of current node
            if nei not in visited: #verify the child is not visited
                q.append(nei) #add child to pipeline
                visited.add(nei) #mark child as visited

                # Option 2: process neighbor here
                if nei == pq[i-1]: #if we found the other node
                    if nei == pq[0]:
                        print('no')
                        sys.exit()

                    else:
                        print('yes')
                        sys.exit()
                
    visited = set()

print('unknown')