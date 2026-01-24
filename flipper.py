# Flipper solution

user_input = input()

num_vertical_flips = 0
for c in user_input:
    if c == 'V':
        num_vertical_flips += 1

# horizontal flips are the rest of the flips
num_horizontal_flips = len(user_input) - num_vertical_flips

if num_vertical_flips % 2 == 0 and num_horizontal_flips % 2 == 0:
    print(1, 2)
    print(3, 4)
elif num_vertical_flips % 2 == 1 and num_horizontal_flips % 2 == 0:
    print(2, 1)
    print(4, 3)
elif num_vertical_flips % 2 == 0 and num_horizontal_flips % 2 == 1:
    print(3, 4)
    print(1, 2)
else:
    print(4, 3)
    print(2, 1)