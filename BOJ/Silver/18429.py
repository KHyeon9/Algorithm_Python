from itertools import permutations

n, k = map(int, input().split())
BDS_up = list(map(int, input().split()))
days = list(permutations([i for i in range(n)]))
cnt = 0
for day in days:
    BDS = 500
    for i in day:
        BDS = BDS - k + BDS_up[i]
        if BDS < 500:
            break
    else:
        cnt += 1
print(cnt)