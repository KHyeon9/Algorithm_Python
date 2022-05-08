n = int(input())
tree = list(map(int, input().split()))
glow = list(map(int, input().split()))
total_tree = []
result = 0
for i in range(n):
    total_tree.append((tree[i], glow[i]))
total_tree = sorted(total_tree, key=lambda x: x[1])
for i in range(n):
    cut_tree = total_tree[i][0] + total_tree[i][1] * i
    result += cut_tree
print(result)