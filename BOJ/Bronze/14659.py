n = int(input())
arr = list(map(int, input().split()))
r, h, c = 0, 0, 0
for i in arr:
    if i > h:
        h = i
        c = 0
    else:
        c += 1
    r = max(r, c)
print(r)