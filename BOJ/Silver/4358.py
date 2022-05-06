from sys import stdin
forest = {}
l = 0
while 1:
    tree_name = stdin.readline().rstrip()
    if not tree_name:
        break
    if tree_name not in forest:
        forest[tree_name] = 1
    else:
        forest[tree_name] += 1
    l += 1
forest = sorted(list(forest.items()))

for i, j in forest:
    print("%s %.4f" % (i, j / l * 100))

