n = int(input())
arr = sorted(list(map(int, input().split())))
for k in range(n, -1, -1):
    if arr[-k] >= k:
        print(k)
        break
