n = int(input())
a_list = list(map(int, input().split()))
b_list = list(map(int, input().split()))
res = 0

for i in range(n):
    if a_list[i] > b_list[i]:
        res += 3
    elif a_list[i] == b_list[i]:
        res += 1

print(res)