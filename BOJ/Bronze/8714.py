n = int(input())
a = list(map(int, input().split()))
r = 0
for i in range(n):
    if a[i] == 1:
        r += 1

if n - r >= r:
    print(r)
else:
    print(n - r)