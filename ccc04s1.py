import sys

input = sys.stdin.readline # faster input function

N = int(input())

words = []

for _ in range(N):
    # word1 = input()
    # word2 = input()
    # word3 = input()

    L = [input() for _ in range(3)]
    L.sort(key=len)

    words.append(L)

for w1,w2,w3 in words:
    if w2.startswith(w1) or w2.endswith(w1) or w3.startswith(w1) \
        or w3.endswith(w1) or w3.endswith(w2) or w3.startswith(w2):
        print("No")
    else:
        print("Yes")

# Data Structure specific for this kind of prefix/suffix check -> Trie