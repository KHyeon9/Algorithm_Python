res = 0
l1, r1, l2, r2, k = map(int, input().split())

for i in range(1, 50001):
    if l1 <= i <= r1 and l2 <= i <= r2 and i % k != 0:
        res += 1
print(res)
