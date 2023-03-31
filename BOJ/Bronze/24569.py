n = int(input())
res = 0

for _ in range(n):
    p = int(input())
    f = int(input())
    if p * 5 - f * 3 > 40:
        res += 1

print(f"{res}+" if res == n else res)