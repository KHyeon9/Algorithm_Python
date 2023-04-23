n = int(input())
m = int(input())
target = list(map(int, input().split()))
res = [0] * n

for i in range(m):
    choice = list(map(int, input().split()))
    for j in range(n):
        if target[i] == choice[j]:
            res[j] += 1
        else:
            res[target[i] - 1] += 1
for i in res:
    print(i)