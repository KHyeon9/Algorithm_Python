n, q = map(int, input().split())
slot = [0] * n

for i in range(1, q + 1):
    l, m = map(int, input().split())
    for j in range(l - 1, n, m):
        slot[j] = i

print(slot.count(0))