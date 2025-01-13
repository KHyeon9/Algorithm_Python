n, m = map(int, input().split())
a_list = map(int, input().split())
b_list = map(int, input().split())

res = sum(a_list)

for el in b_list:
    if el == 0:
        continue
    res *= el

print(res)