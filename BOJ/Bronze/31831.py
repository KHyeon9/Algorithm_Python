n, m = map(int, input().split())
stress = list(map(int, input().split()))
now_stress, res = 0, 0

for el in stress:
    now_stress += el

    if now_stress < 0:
        now_stress = 0

    if now_stress >= m:
        res += 1
print(res)
