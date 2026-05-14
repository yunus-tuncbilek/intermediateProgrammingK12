books = input()

# count the number of misplaced books
count_l, count_m, count_s = 0, 0, 0
for book in books:
    if book == "L":
        count_l += 1
    elif book == "M":
        count_m += 1
    elif book == "S":
        count_s += 1

# calculate the number of misplaced books
# misplaced_l = count_l - books[:count_l].count("L")
l_m, l_s = books[:count_l].count("M"), books[:count_l].count("S")
# misplaced_m = count_m - books[count_l:count_l+count_m].count("M")
m_l, m_s = books[count_l:count_l+count_m].count("L"), books[count_l:count_l+count_m].count("S")
# misplaced_s = count_s - books[count_l+count_m:].count("S")
s_m, s_l = books[count_l+count_m:].count("M"), books[count_l+count_m:].count("L")

# print(f"l_m: {l_m}, l_s: {l_s}, m_l: {m_l}, m_s: {m_s}, s_l: {s_l}, s_m: {s_m}")
moves = 0

# swap misplaced Ls and Ms in each other's region
moves += min(l_m, m_l)
temp = min(l_m, m_l)
l_m -= temp
m_l -= temp

# swap L and S
moves += min(l_s, s_l)
temp = min(l_s, s_l)
l_s -= temp
s_l -= temp

# swap M and S
moves += min(m_s, s_m)
temp = min(m_s, s_m)
m_s -= temp
s_m -= temp

# for every remaining three books, we need two moves to swap
moves += 2 * (l_m + l_s + m_l + m_s + s_l + s_m) // 3

print(moves)