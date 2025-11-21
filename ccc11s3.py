def crystal(m, x, y):
    '''
    CCC '11 S3: Alice Through the Looking Glass

    crystal returns the possibility of a crystal at (x,y)
        at magnification level m

    Return values: 
        3: success
        2: not success, but a higher mag. level may yield a crystal
        1: not success, even at a higher mag. level
    '''

    # base case
    if m == 1:
        if (x,y) in [(1,0), (2,0), (3,0), (2,1)]:
            return 3
        if (x,y) in [(1,1), (2,2), (3,1)]:
            return 2
        return 1 

    # the coordinates (x,y) in magnification m-1
    x_prev, y_prev = x//5, y//5
    res = crystal(m-1, x_prev, y_prev)
    
    if res == 3:
        return 3
    if res == 1:
        return 1
    
    # res must be 2 here
    # further analysis needed

    mini_sq_x, mini_sq_y = x % 5, y % 5
    return crystal(m-1, mini_sq_x, mini_sq_y)

T = int(input())

for _ in range(T):
    m,x,y = [int(x) for x in input().split()]
    res = crystal(m,x,y)

    if res == 3:
        print("crystal")
    else:
        print("empty")