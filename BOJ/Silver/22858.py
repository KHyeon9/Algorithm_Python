n, k = map(int, input().split())
s = list(map(int, input().split()))
d = list(map(int, input().split()))

for _ in range(k):
    result = [0] * n
    for i in range(n):
        result[d[i] - 1] = s[i]
    s = result
print(*s)