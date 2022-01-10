a, b, c = map(int, input().split())
cars = [list(map(int, input().split())) for _ in range(3)]
MAX = max(cars[0][1], cars[1][1], cars[2][1])
arr = [0] * (MAX - 1)
r = 0
for t in cars:
    for i in range(t[0] - 1, t[1] - 1):
        arr[i] += 1
for i in arr:
    if i == 1:
        r += a
    elif i == 2:
        r += b * 2
    elif i == 3:
        r += c * 3
print(r)