k = int(input())
input()
a_list = list(map(int, input().split()))
input()
b_list = list(map(int, input().split()))
res = 0

for a in a_list:
    if a + k in b_list:
        res += b_list.count(a + k)

print(res)