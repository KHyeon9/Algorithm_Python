import sys
sys.setrecursionlimit(10 ** 6)

def dfs(p):
    for i in tree[p]:
        if parents[i] == 0:
            parents[i] = p
            dfs(i)


n = int(input())
tree = [[] for _ in range(n + 1)]
parents = [0] * (n + 1)
for _ in range(n - 1):
    x, y = map(int, input().split())
    tree[x].append(y)
    tree[y].append(x)

dfs(1)

for i in range(2, n + 1):
    print(parents[i])