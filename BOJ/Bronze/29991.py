from sys import stdin
input = stdin.readline

d, c, r = map(int, input().split())
c_list = [int(input()) for _ in range(c)]
r_list = [int(input()) for _ in range(r)]
d += sum(r_list)
res = r
idx = 0

for cost in c_list:
    if d >= cost:
        d -= cost
        res += 1
    else:
        break

print(res)