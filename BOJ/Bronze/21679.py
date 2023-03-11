n = int(input())
limit = list(map(int, input().split()))
k = int(input())
keyDown = list(map(int, input().split()))

keyTotal = [0] * n

for i in keyDown:
    keyTotal[i - 1] += 1

for i in range(n):
    res = "yes" if limit[i] < keyTotal[i] else "no"
    print(res)