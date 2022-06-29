from math import ceil
n, m = map(int, input().split())
res = []
six_cost, one_cost = 1e9, 1e9
for _ in range(m):
    six, one = map(int, input().split())
    six_cost = min(six, six_cost)
    one_cost = min(one, one_cost)
six_div = n / 6
one_rem = n % 6
res.append(one_cost * n)
res.append(ceil(six_div) * six_cost)
res.append(int(six_div) * six_cost + one_rem * one_cost)
print(min(res))