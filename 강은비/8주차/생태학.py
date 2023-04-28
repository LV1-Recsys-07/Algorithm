import sys

trees=dict()
while True:
    name=sys.stdin.readline().strip()
    if not name:
        break
    trees[name]=trees.get(name, 0)+1

total=sum(trees.values())
trees=sorted(trees.items())
for k, v in trees:
    print(f"{k} {(v/total)*100:.4f}")
