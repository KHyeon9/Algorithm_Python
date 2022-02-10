n, k = map(int, input().split())
arr = []
for i in range(1, k + 1):
    r = str(n * i)[::-1]
    arr.append(int(r))
print(max(arr))