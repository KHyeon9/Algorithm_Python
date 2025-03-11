x = int(input())
s = int(input())
p = int(input())
res = x if s == 1 else 0

if p == 1:
    t = 1 if s == 1 else x
    for _ in range(t):
        res += int(input())
print(res)
