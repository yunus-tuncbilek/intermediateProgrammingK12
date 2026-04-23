n = 10000
res = 2
for num in range(2,n):

    count = 0
    for div in range(2,num):
        if num % div == 0:
            count += 1

    if count == 1:
        res = num
        print(num)
print(res)