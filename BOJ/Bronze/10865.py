from sys import stdin
n, m = map(int, stdin.readline().split())
friends = [0] * (n + 1)
for _ in range(m):
    a, b = map(int, stdin.readline().split())
    friends[a] += 1
    friends[b] += 1
for i in friends[1:]:
    print(i)