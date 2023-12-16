a_list = sorted(list(map(int, input().split())))
b_list = sorted(list(map(int, input().split())))
res = 0

for i in range(3):
    res += a_list[i] * b_list[i]

print(res)