n = int(input())
now = int(input())
res = 0

for _ in range(n):
    turn = int(input())
    res += min(
        abs(now - turn),
        360 - abs(now - turn)
    )
    now = turn

print(res)