n, m, k = map(int, input().split())
res = [0] * (n + 1)

for _ in range(2):
    for i in list(map(int, input().split())):
        res[i] = 1

print(n - m - k)
for i in range(1, n + 1):
    if res[i] == 0:
        print(i, end=" ")