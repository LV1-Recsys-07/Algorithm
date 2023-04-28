import sys
# sys.stdin = open("input.txt")
input = sys.stdin.readline


dict = {}
total = 0
while True:
    tree = input().rstrip()
    if tree == "":
        break
    if tree not in dict:
        dict[tree] = 1
    else:
        dict[tree] += 1
    total += 1


trees = list(dict.keys())
trees.sort()
for tree in trees:
    print(f"{tree} {(dict[tree] / total) * 100:.4f}")