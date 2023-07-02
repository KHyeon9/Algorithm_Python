n, m = map(int, input().split())

a_list = set(list(map(int, input().split())))
b_list = list(map(int, input().split()))

res = []

for a in a_list:
    if a in b_list:
        res.append(a)

for r in sorted(res):
    print(r)