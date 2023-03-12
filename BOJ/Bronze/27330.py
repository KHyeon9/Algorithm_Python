n = int(input())
nList = list(map(int, input().split()))
m = int(input())
mList = list(map(int, input().split()))

res = 0

for i in nList:
    res += i
    for j in mList:
        if res == j:
            res = 0
            break
print(res)