n, k = list(map(int, input().split()))
r = []

for i in range(1, n + 1):
    num = n % i

    if num == 0:
        r.append(i)

if len(r) < k:
    print(0)
else:
    print(r[k - 1])