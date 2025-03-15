m, n = map(int, input().split())
arr = [0] * m

for _ in range(n):
    l, r = map(int, input().split())

    for i in range(l - 1, r):
        arr[i] += 1
print("YES" if arr.count(0) == 0 else "NO")