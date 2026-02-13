N = int(input())

res = 0
rem = N
while rem >= 0:
    if rem % 5 == 0:
        res += 1

    rem -= 4

print(res)