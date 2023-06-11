points = [10, 8, 6, 5, 4, 3, 2, 1, 0]
times = sorted([list(input().split()) for _ in range(8)])
b, r = 0, 0

for i in range(8):
    if times[i][1] == 'B':
        b += points[i]
    else:
        r += points[i]
print("Red" if r > b else "Blue")