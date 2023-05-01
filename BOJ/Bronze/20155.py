n, m = map(int, input().split())
brands = list(map(int, input().split()))
res = [0] * (n + 1)

for i in brands:
    res[i] += 1

print(max(res))