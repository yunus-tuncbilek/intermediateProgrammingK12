import sys

A, B, K, T = [int(input()) for _ in range(4)]

if A == B:
    if T == 1:
        print(0)
    elif T == 2:
        print(2)

    sys.exit()

# make sure A is to the left of B on the number line 
if A > B:
    A, B = B, A

# The frog can get from A to B only with only giant hops
if (B - A) % K == 0:
    if T == 1:
        print((B - A) // K)
    elif T == 2:
        print(min((B - A) // K + 2, (B - A) // K + K - 1))

    sys.exit()

giant = (B - A) // K
rem = (B - A) % K

alt1 = giant + rem
alt2 = giant + 1 + ((giant + 1) * K - (B - A))
alt3 = alt1 + 2
alt4 = alt2 + 2

alts = [alt1,alt2,alt3,alt4]
alts.sort()

if T == 1:
    print(alts[0])
else:
    if alts[1] == alts[0]:
        print(alts[2])
    else:
        print(alts[1])