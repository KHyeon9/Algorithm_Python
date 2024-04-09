arr = [0] * 1001
t = int(input())
max_n, min_n = 1001, 0
for _ in range(t):
    a, b = map(int, input().split())
    min_n = min(min_n, a)
    max_n = max(max_n, b)

    for i in range(a, b + 1):
        arr[i] += 1

res = "edward is right"

for i in range(min_n, max_n):
    if arr[i] == t:
        res = "gunilla has a point"
        break

print(res)
