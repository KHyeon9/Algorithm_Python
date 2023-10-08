n = int(input())
a_li = list(map(int, input().split()))
b_li = list(map(int, input().split()))
res = 0

for i in range(n):
    if b_li[i] >= a_li[i]:
        res += 1
print(res)