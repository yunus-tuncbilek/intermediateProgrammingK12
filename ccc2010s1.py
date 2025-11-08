N = int(input())

scores = {}

for _ in range(N):
    split_line = input().split(" ")
    name = " ".join(split_line[:-3])
    ram = split_line[-3]
    cpu = split_line[-2]
    disk = split_line[-1]
    scores[name] = 2 * int(ram) + 3 * int(cpu) + int(disk)

best_computer = ""
second_best_computer = ""

def beats(a, b):
    '''does computer a beat computer b?'''
    if b == "":
        return True
    
    if scores[a] > scores[b] or \
        (scores[a] == scores[b] and a < b):
        return True
    return False

for c in scores:
    if beats(c, best_computer):
        second_best_computer = best_computer
        best_computer = c
    elif beats(c, second_best_computer):
        second_best_computer = c

print(best_computer)
if second_best_computer:
    print(second_best_computer)