points = {1: 0, 2: 0, 4: 0, 8: 0, 16: 0, 32: 0, 64: 0, 128: 0,
          256: 0, 512: 0}
point = 512

a, b = map(int, input().split())

for p in range(10):
    if a // point > 0:
        points[point] += 1
        a -= point
    if b // point > 0:
        points[point] += 1
        b -= point
    point //= 2

res = 0
for key,val in points.items():
    if val == 1:
        res += key

print(res)