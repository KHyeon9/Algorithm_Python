a, b, c = map(int, input().split())

cost = 0
r = 0

while cost < c:
    cost += a
    r += 1
    if r % 7 == 0:
        cost += b

print(r)
