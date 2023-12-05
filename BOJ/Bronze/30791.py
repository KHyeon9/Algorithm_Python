votes = list(map(int, input().split()))
rank = votes[0]
res = 0

for v in votes[1:]:
    if rank - v <= 1000:
        res += 1

print(res)