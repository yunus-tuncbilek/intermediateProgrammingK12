for _ in range(int(input())):
    N = int(input())
    nums = [int(input()) for _ in range(N)]

    branch = []
    need = 1
    for curr in reversed(nums):
        while branch and branch[-1] == need:
            branch.pop()
            need += 1

        if curr == need:
            need += 1
        else:
            branch.append(curr)
    
    while branch and branch[-1] == need:
        branch.pop()
        need += 1

    res = need == N + 1

    if res:
        print("Y")
    else:
        print("N")