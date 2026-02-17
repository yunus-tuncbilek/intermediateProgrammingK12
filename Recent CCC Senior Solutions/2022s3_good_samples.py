import sys

n, m, k = map(int,input().split())

# # only trying to solve the m = 2 case
# if n <= k <= 2*n - 1:
#     alts = k - n
#     if alts == 0:
#         print('1' * n)
#         sys.exit()

#     res = []
    
#     while alts > 0:
#         if not res:
#             res.append("1")
#         else:
#             add = "1" if res[-1] == "2" else "2"

#             res.append(add)
#             alts -= 1

#     while len(res) < n:
#         res.append(res[-1])

#     print(' '.join(res))
# else:
#     print(-1)


# general solution
needed = k - n

if needed < 0 or needed > ((m - 1) * n - (m-1) * (m)//2):
    print(-1)
    sys.exit()

if needed == 0:
    print(' '.join(['1'] * n))
    sys.exit()

res = []
curr = 1
while (needed >= m - 1 or needed >= len(res)) and len(res) < n:
    res.append(curr)
    needed -= min(len(res) - 1, m - 1)
    curr += 1
    if curr == m + 1:
        curr = 1
    # print(res, needed)

if needed > 0:
    assert -needed-1 >= -len(res)

    res.append(res[-needed - 1])
    needed = 0

while len(res) < n:
    res.append(res[-1])

res = [str(x) for x in res]

for x in res:
    assert 1 <= int(x) <= m

print(' '.join(res))