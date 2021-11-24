n = int(input())
m = int(input())
r = 0

for i in range(n):
    car = list(map(int, input().split()))
    m += car[0] - car[1]
    if m < 0:
        r = 0
        break
    if r < m:
        r = m

print(r)