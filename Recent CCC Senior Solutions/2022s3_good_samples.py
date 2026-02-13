n, m, k = map(int,input().split())

# only trying to solve the m = 2 case
if n <= k <= 2*n - 1:
    alts = k - n
    res = []
    
    while alts > 0:
        if not res:
            res.append("1")
        else:
            add = "1" if res[-1] == "2" else "2"

            res.append(add)
            alts -= 1

    while len(res) < n:
        if not res: 
            res.append("1")
        else:
            res.append(res[-1])

    print(' '.join(res))
else:
    print(-1)

