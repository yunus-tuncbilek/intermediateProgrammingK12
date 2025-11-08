total_triangles = int(input())
row1 = input()
row2 = input()

row1 = row1.split()
row2 = row2.split()

# count the number of RED lines
red = 0

# Type 1: the for loop counts the number of RED lines within a row
for t in range(total_triangles - 1):
    if row1[t] == row1[t + 1] == "1":
        red += 1

    if row2[t] == row2[t + 1] == "1":
        red += 1

# Type 2: 
for t in range(total_triangles):
    if row1[t] == row2[t] == "1":
        if t % 2 == 0:
            red += 1

number_of_colored_triangles = row1.count('1') + row2.count('1')

green = 3 * number_of_colored_triangles - 2 * red

print(green)
    
