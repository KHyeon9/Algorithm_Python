t = int(input())
n = list(map(int, input().split()))
s = 0
temp = 0
num = []

for i in range(t):
    if i == 0:
        num.append(n[0])
        s = n[0]

    else:
        temp = n[i] * (i + 1) - s
        num.append(temp)
        s += temp

for i in range(t):
    print(num[i], end=' ')