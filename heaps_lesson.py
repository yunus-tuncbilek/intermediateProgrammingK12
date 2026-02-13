import heapq

heap = []

for i in range(10**6):
    heapq.heappush(heap, i)

print(heap[:5])


for i in range(50):
    x = heapq.heappop(heap)
    print(x, heap[:5])