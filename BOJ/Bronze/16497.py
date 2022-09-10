day = [0] * 101
res = 1

for _ in range(int(input())):
    a, b = map(int, input().split())
    for i in range(a, b):
        day[i] += 1

book = int(input())

for i in day:
    if i > book:
        res = 0
        break
print(res)