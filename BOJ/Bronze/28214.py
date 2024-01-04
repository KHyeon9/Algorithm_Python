n, k, p = map(int, input().split())
bread = list(map(int, input().split()))
res = 0

for i in range(0, n * k, k):
    line = bread[i:i+k]
    no_cream = line.count(0)
    if no_cream < p:
        res += 1
print(res)