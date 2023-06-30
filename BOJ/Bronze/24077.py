n, m = map(int, input().split())
a_list = list(map(int, input().split()))
b_list = list(map(int, input().split()))

res = 0

for a in a_list:
    for b in b_list:
        if a <= b:
            res += 1

print(res)
