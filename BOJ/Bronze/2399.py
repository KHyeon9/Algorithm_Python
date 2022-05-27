n = int(input())
d = list(map(int, input().split()))
res = 0

for i in range(n):
    for j in range(i + 1, n):
        res += abs(d[i] - d[j])
print(res * 2)