n = int(input())
num = list(map(int, input().split()))

r = 0
p = 0

for i in range(n):

    if num[i] == 1:
        p += 1
        r += p

    else:
        p = 0

print(r)